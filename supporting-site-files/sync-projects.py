"""Read only allowlisted public release packages; never execute source-project code."""
from pathlib import Path
import json,os,re,hashlib,urllib.request,urllib.error
ROOT=Path(__file__).resolve().parents[1]
REGISTRY=json.loads((ROOT/'supporting-site-files/source-registry.json').read_text())
SHA=re.compile(r'[0-9a-f]{40}');NAME=re.compile(r'[a-z0-9-]+\.(?:png|jpg|webp)')
REQUIRED={'slug':str,'repo':str,'title':str,'category':str,'stack':list,'desc':str,'built':str,'why':str,'how':list,'demonstrates':str,'image':str,'alt':str,'caption':str,'result':str,'limits':str,'technical':str,'run':str}
def fetch(url,limit=4_000_001):
    headers={'User-Agent':'Ben-Janning-Portfolio-Sync','Accept':'application/vnd.github+json' if url.startswith('https://api.github.com/') else '*/*'}
    token=os.getenv('GH_TOKEN') or os.getenv('GITHUB_TOKEN')
    if token and url.startswith('https://api.github.com/'):headers['Authorization']='Bearer '+token
    with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=40) as response:
        raw=response.read(limit+1)
        if len(raw)>limit:raise ValueError('Response exceeds package limit')
        return raw
def api(path):return json.loads(fetch('https://api.github.com/'+path,1_000_000))
def validate_package(package,slug,repo,run):
    if package.get('schema_version')!=1 or package.get('source_repository')!='benjanning/'+repo or not SHA.fullmatch(package.get('source_revision','')):raise ValueError('Release identity mismatch')
    if run.get('conclusion')!='success' or run.get('status')!='completed' or run.get('head_branch')!='main' or run.get('head_sha')!=package['source_revision'] or run.get('path')!='.github/workflows/portfolio-release.yml':raise ValueError('Source verification has not succeeded for this exact revision')
    p=package.get('project',{})
    if p.get('slug')!=slug or p.get('repo')!=repo:raise ValueError('Project is not the registered source')
    for key,kind in REQUIRED.items():
        if not isinstance(p.get(key),kind):raise ValueError('Missing/invalid project field: '+key)
    for key in ['stack','how']:
        if not p[key] or len(p[key])>15 or any(not isinstance(v,str) or len(v)>3000 for v in p[key]):raise ValueError('Invalid text list')
    for key,value in p.items():
        if isinstance(value,str) and len(value)>15000:raise ValueError('Project text is too long')
    assets=package.get('assets',[])
    if not 1<=len(assets)<=20:raise ValueError('Invalid asset count')
    names=set()
    for asset in assets:
        if not NAME.fullmatch(asset.get('name','')) or asset['name'] in names or not re.fullmatch('[0-9a-f]{64}',asset.get('sha256','')) or not isinstance(asset.get('provenance'),str):raise ValueError('Unsafe or duplicate asset')
        names.add(asset['name'])
    if p['image'] not in names or p.get('extra','') and p['extra'] not in names:raise ValueError('Missing hero/extra image')
    for row in p.get('gallery',[]):
        if not isinstance(row,list) or len(row)!=2 or row[0] not in names or not isinstance(row[1],str):raise ValueError('Invalid gallery')
    if p.get('demo') and p['demo']!='https://benjanning.github.io/'+repo+'/':raise ValueError('Unexpected demo destination')
    return p
def sync(root=ROOT):
    manifest=root/'supporting-site-files/projects.json';lockfile=root/'supporting-site-files/source-lock.json'
    projects=json.loads(manifest.read_text(encoding='utf-8'));locks=json.loads(lockfile.read_text()) if lockfile.exists() else {};updates=[];pending=[]
    for slug,repo in REGISTRY.items():
        try:export_sha=api('repos/benjanning/'+repo+'/commits/portfolio-published')['sha']
        except urllib.error.HTTPError as e:
            if e.code in (404,422):pending.append({'slug':slug,'reason':'No published verification package yet'});continue
            raise
        if not SHA.fullmatch(export_sha):raise ValueError('Invalid export revision')
        if locks.get(slug,{}).get('export_revision')==export_sha:continue
        base='https://raw.githubusercontent.com/benjanning/'+repo+'/'+export_sha+'/portfolio/export/'
        package=json.loads(fetch(base+'manifest.json',1_000_000))
        run_id=package.get('verification_run')
        if not isinstance(run_id,int) or run_id<=0:raise ValueError('Invalid verification run')
        run=api('repos/benjanning/'+repo+'/actions/runs/'+str(run_id))
        if run.get('status')!='completed' or run.get('conclusion')!='success':pending.append({'slug':slug,'reason':'Latest source verification is not successful/completed'});continue
        p=validate_package(package,slug,repo,run).copy()
        comparison=api('repos/benjanning/'+repo+'/compare/'+package['source_revision']+'...main')
        if comparison.get('status') not in ['identical','ahead']:raise ValueError('Source revision is not on approved main history')
        if p.get('demo'):fetch(p['demo'],1_000_000)
        prefix='releases/'+slug+'/'+package['source_revision']+'/'
        staged=[]
        for asset in package['assets']:
            raw=fetch(base+'assets/'+asset['name'])
            if len(raw)!=asset.get('bytes') or hashlib.sha256(raw).hexdigest()!=asset['sha256'] or not raw.startswith((b'\x89PNG\r\n\x1a\n',b'\xff\xd8\xff',b'RIFF')):raise ValueError('Image integrity/type mismatch')
            staged.append((root/'assets'/prefix/asset['name'],raw))
        # Commit the complete in-memory package only after every asset passed.
        for file,raw in staged:file.parent.mkdir(parents=True,exist_ok=True);file.write_bytes(raw)
        p['image']=prefix+p['image'];p['extra']=prefix+p['extra'] if p.get('extra') else ''
        p['gallery']=[[prefix+image,caption] for image,caption in p.get('gallery',[])]
        p['source_revision']=package['source_revision'];p['verification_run']=run_id
        p['provenance']=[dict(name=prefix+a['name'],sha256=a['sha256'],description=a['provenance']) for a in package['assets']]
        index=next(i for i,item in enumerate(projects) if item['slug']==slug);projects[index]=p
        locks[slug]={'repository':'benjanning/'+repo,'source_revision':package['source_revision'],'export_revision':export_sha,'verification_run':run_id,'assets':package['assets']}
        updates.append({'slug':slug,'repository':repo,'source_revision':package['source_revision'],'verification_run':run_id})
    manifest.write_text(json.dumps(projects,indent=2,ensure_ascii=False)+'\n',encoding='utf-8');lockfile.write_text(json.dumps(locks,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    report={'updated':updates,'pending':pending};(root/'sync-result.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    return report
if __name__=='__main__':sync()
