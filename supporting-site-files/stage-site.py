"""Stage only public website files, with an exact deployment revision receipt."""
from pathlib import Path
import shutil,os,json,subprocess
root=Path(__file__).resolve().parents[1];out=root/'dist';out.mkdir(exist_ok=True)
for name in ['index.html','404.html','.nojekyll']:shutil.copy2(root/name,out/name)
for name in ['assets','projects']:shutil.copytree(root/name,out/name,dirs_exist_ok=True)
revision=os.getenv('GITHUB_SHA') or subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
locks=root/'supporting-site-files/source-lock.json'
(out/'release.json').write_text(json.dumps({'portfolio_revision':revision,'projects':json.loads(locks.read_text()) if locks.exists() else {}},indent=2)+'\n',encoding='utf-8')
print('Staged public website:',revision)
