import numpy as np
from scipy import stats
import pandas as pd
from pylab import *
import seaborn as sns
df=pd.read_csv('walkd.txt')                                                 #reading the data file 
y=[x for x in df['distance'] ]                                                  #list of distance traversed on various days
#######
nd=[ a+1 for a in range(len(y))]                                               #list of number of days
#######
mavgdis=[]                                                                            #list of moving average distance                                              
avgd=0
n=0
for d in y:
    avgd+=d
    n+=1
    mavgdis.append(avgd/n)
#######  
acc=0
Cdfdist=[]                                                                              #list of cumulative distance traversed by each day               
for d in y:
    acc+=d
    Cdfdist.append(acc)
dis=np.array(y)
#######
avgd=[np.mean(dis) for x in range(len(y))]                      #absolute average distance (a constant but must have a list for plotting]
#######
T=[int(t/60)+((t%60)/60) for t in df['time'] if t!=0]                #list of different walk durations
#######
V=[s[0]/s[1] for s in zip(y,T) if (s[1]!=0)]                              #list of the various speeds that I had on various days
#######
V1=[s[0]/s[1] for s in zip(y,T) if (s[1]!=0) and s[0]>1]          #list of the various speeds that I had on various days excluding the days I didn't walk/jog
#######)
vel=np.array(V)
#######
acc=0
mavgV=[]                                                                             #moving average velocity
n=0
for v in vel:
    acc+=v
    n+=1
    mavgV.append(acc/n)
#######
avgV=[np.mean(vel) for x in range(len(vel))]                 #absolute average velocity



#fig = plt.figure()
#fig.patch.set_facecolor('xkcd:mint green')

plt.rcParams['axes.facecolor'] = 'black'

#######                                                                             can test now
#plt.figure(figsize=(8,8))
#x=df['time']
#plt.plot(V1)
#plt.plot(y)                                    #distance traversed 
#plt.plot(avgd)                             #absolute average distance
#plt.plot(mavgV)                             #absolute average velocity
#plt.plot(mavgdis)                       #moving average distance
#plt.scatter(V, y)                          #distance vs velocity
#plt.scatter(T, V)
plt.plot(nd, Cdfdist)
#plt.scatter(nd, Cdfdist)
#plt.plot(T, Cdfdist)
#sns.jointplot(x=T, y=y, kind='kde').annotate(stats.pearsonr)
#sns.regplot(x=T, y=y, fit_reg=True).annotate(xy=(T, y), stats.pearsonr)
#plt.bar(nd, Cdfdist)
#plt.scatter(T, V)                          #velocity vs time  
#plt.plot(T)
#plt.scatter(T, y)
plt.xlabel('Number of days')
#plt.xlabel('Time')
plt.ylabel('Cumulative distance (km)')

for i in range(5):
    plt.axvline(x=(i+1)*10, color='red', linestyle='--')
plt.axvline(x=1, color='red', linestyle='--')
plt.axhline(y=Cdfdist[0], color='green', linestyle='--')
for i in range(5):
    plt.axhline(y=Cdfdist[9+10*i], color='green', linestyle='--')
#plt.legend(['distance traversed'])
#plt.title('Net distance traversed')
print(df.iloc[:, :2].corr())
print('Average Speed= ', str(np.mean(vel))+' kmph.')
print('Average Distance= ', str(np.mean(dis))+' km.')
print('Average Duration= ', str(np.mean(T))+ ' hrs.')
print('Total Distance= ', str(sum(y))+'km.')
print('Total number of days= ', str(nd[-1]))
plt.show()






