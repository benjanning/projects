"""Validate generated links, anchors, metadata, source locks and image integrity."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
class Document(HTMLParser):
    def __init__(self,text):
        super().__init__();self.refs=[];self.ids=set();self.meta={};self.canonical=None;self.images=[];self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'):self.ids.add(a['id'])
        if tag=='meta':self.meta[a.get('property') or a.get('name')]=a.get('content')
        if tag=='link' and a.get('rel')=='canonical':self.canonical=a.get('href')
        if tag in ['a','link','script','img']:
            ref=a.get('href') if tag in ['a','link'] else a.get('src')
            if ref:self.refs.append(ref)
        if tag=='img':
            if 'alt' not in a:raise ValueError('Image missing alt attribute')
            self.images.append(a)
def validate(root=ROOT):
    projects=json.loads((root/'supporting-site-files/projects.json').read_text(encoding='utf-8'));errors=[];count=0
    docs={p:Document(p.read_text(encoding='utf-8')) for p in [root/'index.html',root/'404.html',*sorted((root/'projects').glob('*/index.html'))]}
    for file,doc in docs.items():
        for ref in doc.refs:
            parts=urlsplit(ref)
            if parts.scheme or parts.netloc:continue
            path=unquote(parts.path)
            target=(root/path.removeprefix('/projects/')) if path.startswith('/projects/') else (file.parent/path if path else file)
            if target.is_dir():target=target/'index.html'
            if not target.exists():errors.append(str(file.relative_to(root))+' missing '+ref)
            elif parts.fragment and target.suffix=='.html':
                target_doc=docs.get(target) or Document(target.read_text(encoding='utf-8'))
                if unquote(parts.fragment) not in target_doc.ids:errors.append('Missing anchor '+ref)
            count+=1
    for p in projects:
        file=root/'projects'/p['slug']/'index.html';doc=docs[file];url='https://benjanning.github.io/projects/projects/'+p['slug']+'/'
        expected={'og:title':p['title']+' | Ben Janning','og:description':p['desc'],'og:image':'https://benjanning.github.io/projects/assets/'+p['image'],'og:image:alt':p['alt'],'twitter:card':'summary_large_image'}
        if doc.canonical!=url:errors.append('Wrong canonical '+p['slug'])
        for key,value in expected.items():
            if doc.meta.get(key)!=value:errors.append('Wrong metadata '+p['slug']+' '+key)
        if p.get('source_revision'):
            if not re.fullmatch('[0-9a-f]{40}',p['source_revision']):errors.append('Invalid source revision')
            for a in p.get('provenance',[]):
                f=root/'assets'/a['name']
                if not f.exists() or hashlib.sha256(f.read_bytes()).hexdigest()!=a['sha256']:errors.append('Stale/missing source asset '+a['name'])
    if errors:raise ValueError('\n'.join(errors))
    result={'html_pages':len(docs),'local_references':count,'project_metadata':len(projects),'errors':errors}
    print(json.dumps(result,indent=2));return result
if __name__=='__main__':validate()
