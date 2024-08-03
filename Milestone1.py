import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import sys
sys.path.append(r'c:\users\robah\appdata\roaming\python\python310\site-packages')


t=np.linspace(0,3,12*1024)
F=[130.81,146.83,164.81,174.61,196,220]
f=[261.63,293.66,329.63,349.23,392,440]
ti=[0,0.5,1,1.5,2,2.5]
Ti=[0.2,0.2,0.2,0.2,0.2,0.2]

N =len(F)

sum=0
for i in range(N):
    x1=np.sin(2*np.pi*F[i]*t)
    x2=np.sin(2*np.pi*f[i]*t)
    u1=np.where(t-ti[i]<=0,0,1)
    u1_2=np.where(t-ti[i]-Ti[i]<=0,0,1)
    xtotal=x1+x2
    ytotal=u1-u1_2
    yres=xtotal*ytotal
    sum=sum+yres
    
    
plt.plot(t,sum)
sd.play(sum,3*1024)
    
    












