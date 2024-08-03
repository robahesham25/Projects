import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
import sys
sys.path.append(r'c:\users\robah\appdata\roaming\python\python310\site-packages')


t=np.linspace(0,3,12*1024)
F=[130.81,146.83,164.81,174.61,196,220]
f=[261.63,293.66,329.63,349.23,392,440]
ti=[0,0.5,1,1.5,2,2.5]
Ti=[0.2,0.2,0.2,0.2,0.2,0.2]

Num =len(F)

sum=0
for i in range(Num):
    x1=np.sin(2*np.pi*F[i]*t)
    x2=np.sin(2*np.pi*f[i]*t)
    u1=np.where(t-ti[i]<=0,0,1)
    u1_2=np.where(t-ti[i]-Ti[i]<=0,0,1)
    xtotal=x1+x2
    ytotal=u1-u1_2
    yres=xtotal*ytotal
    sum=sum+yres
    
#original signal    
plt.plot(t,sum)
plt.title ('Time Domain Signal')
plt.xlabel ('Time')
plt.ylabel ('Amplitude')
plt.show ()
plt.figure()
#sd.play(sum,3*1024)

#fourier transform of original signal
N=3*1024
fy=np.linspace(0,512,int(N/2))
fourier=fft(sum) 
y=2/N * np.abs(fourier[0:int(N/2)])
plt.plot(fy,y)  
plt.title('Frequency domain Signal')
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude')
plt.show() 
plt.figure()

#noise creation
noise=np.random.randint(0,512,2)
n=np.sin(2*np.pi*noise[0]*t)+np.sin(2*np.pi*noise[1]*t)
xn=sum+n
#time-domain with noise signal
plt.plot(t,xn)
plt.title ('Time Domain Signal')
plt.xlabel ('Time')
plt.ylabel ('Amplitude')
plt.show ()
plt.figure()
#fourier transform with noise signal
fouriern=fft(xn) 
y2= 2/N * np.abs(fouriern[0:int(N/2)])
plt.plot(fy,y2)  
plt.title('Frequency domain Signal')
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude')
plt.show() 
plt.figure()



#noise cancellation

max=np.max(y)
max2=max
ind1=0
for i in range (len(y2)):
    if (y2[i]>max2):
        ind1=i
        max2=y2[i]
        
    
ind2=0
max3=max
for j in range (len(y2)):
    if (y2[j]>max3 and y2[j]!=y2[ind1]):
        ind2=j
        max3=y2[j]
       


roundf1=np.round(fy[ind1])
roundf2=np.round(fy[ind2])
wave1=np.sin(2*np.pi*roundf1*t)
wave2=np.sin(2*np.pi*roundf2*t)
xfilterted=xn-wave1-wave2
plt.plot(t,xfilterted)
nonoisef=fft(xfilterted)
plt.figure()
y3= 2/N * np.abs(nonoisef[0:int(N/2)])
plt.plot(fy,y3)
sd.play(xfilterted,3*1024)
plt.figure()



plt.subplot(3,1,1)
plt.plot(t,sum)
plt.title ('Time Domain Signal')
plt.xlabel ('Time')
plt.ylabel ('Amplitude')
plt.subplot(3,1,2)
plt.plot(t,xn)
plt.subplot(3, 1,3)
plt.plot(t,xfilterted)
plt.show()

plt.subplot(3,1,1)
plt.plot(fy,y)  
plt.title('Frequency domain Signal')
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude')
plt.subplot(3,1,2)
plt.plot(fy,y2)  
plt.subplot(3,1,3)
plt.plot(fy,y3)
plt.show()











