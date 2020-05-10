import numpy as np
from scipy import stats
import pandas as pd
from pylab import *

df=pd.read_csv('walkd.txt')                                                #reading the data file 
y=[x for x in df['distance'] if x!=0]                                       #list of distance traversed on various days                             
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
T=[int(t/60)+((t%60)/60) for t in df['time'] if t!=0]                #list of different time durations I walked 
#######
V=[s[0]/s[1] for s in zip(y,T) if (s[1]!=0)]                              #list of the various speeds that I had on various days
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



#######                                                                             can test now
#plt.figure(figsize=(8,8))
#x=df['time']
#plt.plot(y)                                    #distance traversed 
plt.plot(y)                                     #velocity 
#plt.plot(avgd)                             #absolute average distance
#plt.plot(avgV)                             #absolute average velocity
#plt.plot(mavgdis)                       #moving average distance
#plt.scatter(V, y)                          #distance vs velocity
#plt.scatter(T, V)                         #velocity vs time
#plt.scatter(T, y)                          #distance vs time
plt.plot(avgd)
plt.xlabel('days')
plt.ylabel('distance(in km)')
plt.legend(['distance traversed', 'average distance traversed'])
print('Average Speed= ', str(np.mean(vel))+' km')
print('Average Distance= ', str(np.mean(dis))+' km')
plt.show()











   

