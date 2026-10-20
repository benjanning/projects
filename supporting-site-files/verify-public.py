"""Accept publication only when the public receipt and six pages match the build."""
from pathlib import Path
import os,json,time,urllib.request,hashlib
from importlib.util import spec_from_file_location,module_from_spec
root=Path(__file__).resolve().parents[1]
spec=spec_from_file_location('site_validation',Path(__file__).with_name('validate-site.py'));mod=module_from_spec(spec);spec.loader.exec_module(mod)
def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Portfolio-release-verification','Cache-Control':'no-cache'}),timeout=30) as r:return r.read()
def verify():
    base='https://benjanning.github.io/projects/';expected=os.environ['GITHUB_SHA'];receipt=json.loads(fetch(base+'release.json?revision='+expected))
    if receipt['portfolio_revision']!=expected:raise ValueError('Public deployment receipt is not the expected revision')
    projects=json.loads((root/'supporting-site-files/projects.json').read_text(encoding='utf-8'))
    for p in projects:
        doc=mod.Document(fetch(base+'projects/'+p['slug']+'/?revision='+expected).decode('utf-8'))
        if doc.meta.get('og:image')!=base+'assets/'+p['image']:raise ValueError('Public metadata mismatch: '+p['slug'])
        for a in p.get('provenance',[]):
            if hashlib.sha256(fetch(base+'assets/'+a['name'])).hexdigest()!=a['sha256']:raise ValueError('Public asset mismatch')
        fetch('https://github.com/benjanning/'+p['repo'])
        if p.get('demo'):fetch(p['demo'])
    print(json.dumps({'published_revision':expected,'project_pages':len(projects),'status':'verified'},indent=2))
for attempt in range(12):
    try:verify();break
    except Exception as error:
        if attempt==11:raise
        print('Publication not yet verified:',type(error).__name__,'retry',attempt+1);time.sleep(15)
