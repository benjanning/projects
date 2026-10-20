const {defineConfig}=require('@playwright/test');
const publicBase=process.env.PORTFOLIO_BASE;
module.exports=defineConfig({testDir:'supporting-site-files/browser',testMatch:'*.spec.cjs',workers:3,retries:0,reporter:[['list'],['json',{outputFile:'verification/browser-results.json'}]],use:{baseURL:publicBase||'http://127.0.0.1:8091/',locale:'en-IE',reducedMotion:'reduce'},webServer:publicBase?undefined:{command:'python -m http.server 8091 --bind 127.0.0.1 --directory dist',url:'http://127.0.0.1:8091',reuseExistingServer:false}});
