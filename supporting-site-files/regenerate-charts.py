from pathlib import Path
import sys,json,shutil
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay,confusion_matrix
root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[2]
out=Path(__file__).resolve().parents[1]/'assets/charts'
plt.rcParams.update({'figure.facecolor':'#f4f5ee','axes.facecolor':'#f4f5ee','axes.edgecolor':'#c7d2c8','axes.labelcolor':'#254b3c','text.color':'#193e31','xtick.color':'#52685b','ytick.color':'#52685b','font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'savefig.facecolor':'#f4f5ee'})
def save(name):plt.tight_layout(pad=2);plt.savefig(out/name,dpi=170,bbox_inches='tight');plt.close()
# A new presentation of authentic Iris data, without a model-performance claim.
df=pd.read_csv(root/'pands-project/iris.csv');fig,ax=plt.subplots(figsize=(9,5.7))
for group,color in zip(df.variety.unique(),['#195d45','#b68132','#668b88']):
 sub=df[df.variety==group];ax.scatter(sub['petal.length'],sub['petal.width'],label=group,color=color,s=44,alpha=.8,edgecolor='white',linewidth=.5)
ax.set(xlabel='Petal length (cm)',ylabel='Petal width (cm)',title='Small measurements. Clear patterns.');ax.legend(frameon=False);save('iris-petals.png')
# Actual PlantGrowth observations; no invented data.
df=pd.read_csv(root/'applied_statistics/PlantGrowth.csv');fig,ax=plt.subplots(figsize=(9,5.7));groups=['ctrl','trt1','trt2'];data=[df[df.group==g].weight for g in groups]
b=ax.boxplot(data,patch_artist=True,tick_labels=['Control','Treatment 1','Treatment 2'],widths=.45,medianprops={'color':'#193e31','linewidth':2})
for patch,color in zip(b['boxes'],['#c6d9c8','#e5d5a8','#8db59f']):patch.set_facecolor(color)
rng=np.random.default_rng(40)
for i,y in enumerate(data,1):ax.scatter(rng.normal(i,.045,len(y)),y,color='#285e47',s=30,zorder=3,alpha=.8)
ax.set(ylabel='Dried plant weight',title='Comparing three growing conditions');save('plant-growth.png')
# Descriptive distribution, rather than stale coursework model scores.
df=pd.read_csv(root/'pfda-Project2/Data/data.csv');fig,ax=plt.subplots(figsize=(9,5.7))
for value,label,color in [('B','Benign (dataset label)','#286d50'),('M','Malignant (dataset label)','#bd9455')]:
 ax.hist(df.loc[df.diagnosis==value,'radius_mean'],bins=22,alpha=.7,label=label,color=color)
ax.set(xlabel='Mean radius (dataset feature)',ylabel='Number of observations',title='Exploring features before modelling');ax.legend(frameon=False);save('classification-features.png')
# Verified benchmark produced by benchmark_verified.py.
df=pd.read_csv(root/'Sorting-Algorithms-Project/verified_timings.csv');fig,ax=plt.subplots(figsize=(9,5.7))
for (name,sub),color in zip(df.groupby('algorithm'),['#b68132','#648e7c','#195d45','#798eb4','#a86858']):ax.plot(sub['size'],sub.median_ms,marker='o',label=name,color=color,linewidth=2)
ax.set(xlabel='Input size (non-negative integers)',ylabel='Median runtime (ms, logarithmic scale)',yscale='log',title='Five algorithms. The same input samples.');ax.legend(frameon=False,ncol=3);ax.grid(axis='y',alpha=.16);save('sorting-benchmark.png')
shutil.copy(root/'Sorting-Algorithms-Project/verified_timings.csv',out/'verified_timings.csv')
print('Charts regenerated from source CSVs and verified timings.')
