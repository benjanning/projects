import unittest,importlib.util,json,tempfile,hashlib,urllib.error
from pathlib import Path
from unittest.mock import patch
BASE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('sync_projects',BASE/'sync-projects.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class SyncSafetyTests(unittest.TestCase):
    def setUp(self):
        self.p=json.loads((BASE/'projects.json').read_text(encoding='utf-8'))[0].copy()
        self.p.update(image='hero.png',extra='',gallery=[],demo='')
        self.sha='a'*40;self.image=b'\x89PNG\r\n\x1a\n'+b'synthetic fixture bytes'
        self.package=dict(schema_version=1,source_repository='benjanning/data-representation-project',source_revision=self.sha,verification_run=123,project=self.p,assets=[dict(name='hero.png',sha256=hashlib.sha256(self.image).hexdigest(),bytes=len(self.image),provenance='Unit-test image fixture; never published')])
        self.run=dict(status='completed',conclusion='success',head_branch='main',head_sha=self.sha,path='.github/workflows/portfolio-release.yml')
    def test_rejects_unverified_or_mismatched_source(self):
        for field,value in [('head_sha','b'*40),('conclusion','failure'),('head_branch','feature'),('path','unexpected.yml')]:
            run={**self.run,field:value}
            with self.assertRaises(ValueError):m.validate_package(self.package,'car-rental','data-representation-project',run)
    def test_rejects_paths_and_unregistered_destinations(self):
        for mutation in ['path','demo','repo']:
            package=json.loads(json.dumps(self.package))
            if mutation=='path':package['assets'][0]['name']='../hero.png'
            if mutation=='demo':package['project']['demo']='https://unapproved.example/'
            if mutation=='repo':package['project']['repo']='unregistered'
            with self.assertRaises(ValueError):m.validate_package(package,'car-rental','data-representation-project',self.run)
    def api(self,path):
        if '/commits/' in path:return dict(sha='c'*40)
        if '/actions/runs/' in path:return self.run
        if '/compare/' in path:return dict(status='identical')
        raise AssertionError('Unexpected API request')
    def test_imports_complete_version_and_hashes(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'supporting-site-files').mkdir();(root/'supporting-site-files/projects.json').write_text(json.dumps([self.p]),encoding='utf-8')
            with patch.object(m,'REGISTRY',{'car-rental':'data-representation-project'}),patch.object(m,'api',side_effect=self.api),patch.object(m,'fetch',side_effect=lambda url,limit=0:json.dumps(self.package).encode() if url.endswith('manifest.json') else self.image):
                result=m.sync(root)
            p=json.loads((root/'supporting-site-files/projects.json').read_text(encoding='utf-8'))[0]
            self.assertEqual(p['source_revision'],self.sha)
            self.assertEqual((root/'assets'/p['image']).read_bytes(),self.image)
            self.assertEqual(len(result['updated']),1)
    def test_bad_hash_cannot_replace_manifest(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'supporting-site-files').mkdir();manifest=root/'supporting-site-files/projects.json';original=json.dumps([self.p]);manifest.write_text(original,encoding='utf-8')
            with patch.object(m,'REGISTRY',{'car-rental':'data-representation-project'}),patch.object(m,'api',side_effect=self.api),patch.object(m,'fetch',side_effect=lambda url,limit=0:json.dumps(self.package).encode() if url.endswith('manifest.json') else b'tampered'):
                with self.assertRaises(ValueError):m.sync(root)
            self.assertEqual(manifest.read_text(encoding='utf-8'),original)
            self.assertFalse((root/'assets').exists())
if __name__=='__main__':unittest.main()
