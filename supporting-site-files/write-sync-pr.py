from pathlib import Path
import json,os
r=Path(__file__).resolve().parents[1];result=json.loads((r/'sync-result.json').read_text())
text='Refresh the portfolio from tested public source releases. No source-project code is executed by the synchroniser. Image hashes, source identities and successful verification runs are checked before generation.\n\n'
for item in result['updated']:
 text+='- '+item['repository']+': `'+item['source_revision']+'` · https://github.com/benjanning/'+item['repository']+'/actions/runs/'+str(item['verification_run'])+'\n'
text+='\nThis update passed the synchronisation workflow tests, page generation, metadata checks and local asset/link validation. Merge only after reviewing the source changes and genuine visual evidence. A main-branch merge starts the single Pages workflow and public revision verification.\n\nSync run: https://github.com/'+os.environ['GITHUB_REPOSITORY']+'/actions/runs/'+os.environ['GITHUB_RUN_ID']+'\n'
(r/'sync-pr-body.md').write_text(text,encoding='utf-8')
