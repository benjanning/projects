const {test,expect}=require('@playwright/test');
const fs=require('node:fs');
const projects=require('../projects.json');
const pages=[{slug:'home',title:'Useful technology.',path:''},...projects.map(p=>({...p,path:'projects/'+p.slug+'/'}))];
for(const width of [1440,390])for(const p of pages){
test(`${p.slug} at ${width}px`,async({page})=>{
  test.setTimeout(60000);await page.setViewportSize({width,height:width===390?844:1000});
  const errors=[];page.on('pageerror',e=>errors.push(e.message));
  const response=await page.goto(p.path+'?revision='+(process.env.GITHUB_SHA||'local'),{waitUntil:'networkidle'});expect(response.status()).toBe(200);
  await expect(page.getByRole('heading',{level:1})).toContainText(p.title);
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=document.documentElement.clientWidth)).toBe(true);
  for(const img of await page.locator('main img').all()){
    await img.scrollIntoViewIfNeeded();await expect(img).toBeVisible();
    await expect.poll(()=>img.evaluate(el=>el.complete&&el.naturalWidth>0)).toBe(true);
  }
  if(p.slug!=='home'){
    expect(p.source_revision).toMatch(/^[0-9a-f]{40}$/);
    await expect(page.locator(`a[href="https://github.com/benjanning/${p.repo}/commit/${p.source_revision}"]`)).toBeVisible();
    await page.getByRole('link',{name:'Technical details',exact:true}).click();await expect(page.locator('#technical')).toBeVisible();
    await page.locator('#technical summary').filter({hasText:'Try it locally'}).click();await expect(page.locator('#technical')).toContainText(p.run);
  }
  await page.getByRole('heading',{level:1}).scrollIntoViewIfNeeded();
  fs.mkdirSync('verification/screenshots',{recursive:true});await page.screenshot({path:`verification/screenshots/${p.slug}-${width}.jpg`,type:'jpeg',quality:82,fullPage:true});
  await page.evaluate(()=>window.scrollTo(0,0));await page.screenshot({path:`verification/screenshots/${p.slug}-${width}-overview.jpg`,type:'jpeg',quality:85});
  expect(errors).toEqual([]);
});}
test('homepage filters and navigation',async({page})=>{
  await page.goto('');await expect(page.locator('.project-card:visible')).toHaveCount(6);
  await page.locator('[data-filter="Web application"]').click();await expect(page.locator('.project-card:visible')).toHaveCount(2);
  await page.locator('[data-filter="Algorithms"]').click();await expect(page.locator('.project-card:visible')).toHaveCount(1);
  await page.locator('[data-filter="All"]').click();await expect(page.locator('.project-card:visible')).toHaveCount(6);
  await page.getByRole('link',{name:'Iris dataset exploration',exact:true}).click();await expect(page.getByRole('heading',{level:1})).toContainText('Iris');
});
