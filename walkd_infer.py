import numpy as np
from scipy import stats
import pandas as pd
from pylab import *
#import
'''
a=np.array([[1,2],[4,5],[7,8]])
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        a[i][j]+=2
b=np.full((3,4), 12)
print(b)
print(a)
'''
df=pd.read_csv('walkd.txt')
################################# distance (y)
y=[x for x in df['distance'] if x!=0]
############################### moving average distance (avgdis)
avgdis=[]
avgd=0
n=0
for d in y:
    avgd+=d
    n+=1
    avgdis.append(avgd/n)
####################   cumulative distance  (Cdfdis)
acc=0
Cdfdist=[]
for d in y:
    acc+=d
    Cdfdist.append(acc)
dis=np.array(y)
################################### absolute average distance  (avgd)
avgd=[np.mean(dis) for x in range(len(y))]
################################ time   (T)
T=[int(t/60)+((t%60)/60) for t in df['time'] if t!=0]
####################################################### velocity(V)
V=[s[0]/s[1] for s in zip(y,T) if (s[1]!=0)]
############################################## velocity(vel)
vel=np.array(V)
############################################ moving average velocity (mavgV)
acc=0
mavgV=[]
n=0
for v in vel:
    acc+=v
    n+=1
    mavgV.append(acc/n)


########################################### absolute average velocity (avgV)
avgV=[np.mean(vel) for x in range(len(vel))]
####################################################
plt.figure(figsize=(8,8))
#x=df['time']
#plt.plot(y)
#plt.plot(V)
import seaborn as sns
plt.barh(width=y, y=Cdfdist)
#plt.plot(avgV)
#plt.plot(avgd)
#plt.plot(avgV)
#plt.plot(avgdis)
#plt.plot(Cdfdist)
#plt.scatter(T, V)
#plt.plot(T,V)
#plt.plot(mavgV)
plt.xlabel('dist')
plt.ylabel('total dist')
#plt.legend([''])
print('Average Speed= ', str(np.mean(vel))+' km')
print('Average Distance= ', str(np.mean(dis))+' km')
plt.show()

'''
x=[1,2,3,4,5,6,7]
y=[]
acc=0
ne=0
for n in x:
    acc+=n
    ne+=1
    y.append(acc/ne)
print(y)
'''












   

