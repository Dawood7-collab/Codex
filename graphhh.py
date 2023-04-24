import numpy as np
import matplotlib.pyplot as plt
a=np.linspace(1,10,100)
b=np.linspace(1,10,100)
c=np.linspace(1,10,100)
d,e=np.meshgrid(a,a)
f=np.sin(a)+np.random.randn(100)
f1=np.cos(a)+np.random.randn(100)
f2=np.tan(a)+np.random.randn(100)
f3=d-d/d**2+e**2
fig,axes=plt.subplots(2,2,figsize=(10,10))
for i in range(30):
 ax=axes[0][0]
 ax.plot(a,f*i)
 ax.set_title('noisy sine')
 ax.set_xlabel('time')
 ax.set_ylabel('amplitude')
 ax=axes[0][1]
 ax.plot(b,f1*i/2)
 ax.set_title('noisy cos')
 ax.set_xlabel('time')
 ax.set_ylabel('amplitude')
 ax=axes[1][0]
 ax.plot(c,f2*-i)
 ax.set_title('noisy tan')
 ax.set_xlabel('time')
 ax.set_ylabel('amplitude')
 ax=axes[1][1]
 ax.contour(d,e,f3)
 ax.set_title(' contour cylindrical wall')
 ax.set_xlabel('time')
 ax.set_ylabel('mean')
plt.show()

