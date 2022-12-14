import numpy as np
import matplotlib.pyplot as plt
import math as m


N=400
sigma=1
delta=0.4
Lx=15
Ly=10*Lx
mass=1
g=0.1



    
xposini=np.zeros(N)
yposini=np.zeros(N)
    
xposini[0]=np.random.uniform(-Lx/2+sigma/2,Lx/2-sigma/2,size=1)
yposini[0]=np.random.uniform(-Ly/2+sigma/2,Ly/2-sigma/2,size=1)

for i in range(1,N,1):
    
    xposini[i]=np.random.uniform(-Lx/2+sigma/2,Lx/2-sigma/2,size=1)
    yposini[i]=np.random.uniform(-Ly/2+sigma/2,Ly/2-sigma/2,size=1)
    
    j=0
    
    while (j<i):
        
        if(np.sqrt((xposini[i]-xposini[j])**2+(yposini[i]-yposini[j])**2)<sigma):
            
            xposini[i] = np.random.uniform(-Lx/2+sigma/2,Lx/2-sigma/2,size=1)
            yposini[i] = np.random.uniform(-Ly/2+sigma/2,Ly/2-sigma/2,size=1)
            
            j=0
            
        else:
            
            j+=1 

plt.figure(figsize=(5, 10))
plt.scatter(xposini,yposini, s=np.pi*(sigma*4/2)**2)
plt.xlim(-Lx/2,Lx/2)
plt.ylim(-Ly/2,Ly/2)
plt.show()

xpos=[]
for i in range(0,len(xposini)):
    xpos.append(xposini[i])
    
ypos=[]
for i in range(0,len(yposini)):
    ypos.append(yposini[i])
    
T_t=5000

for j in range(0,T_t,1):
        

    deltae=1
    A=np.random.uniform(0,1,N)
    B=np.random.uniform(0,1,N)
        
    for ii in range(0,N,1):
        
        deltae=1
            
        i = np.random.randint(0,N-1)
            
        x_new=xpos[i]+delta*(A[i]-0.5)
        y_new=ypos[i]+delta*(B[i]-0.5)
        
        for k in range(0,N,1):
            
            if(x_new>Lx/2-sigma/2):
                
                deltae=0
                
                break
            
            if(x_new<-Lx/2+sigma/2):
                
                deltae=0
                
                break
            
            if(y_new>Ly/2-sigma/2):
                
                deltae=0
                
                break
            
            if(y_new<-Ly/2+sigma/2):
                
                deltae=0
                
                break

            if(np.sqrt((x_new-xpos[k])**2+(y_new-ypos[k])**2)<sigma and i!=k):
                
                
                deltae=0
                break
            
            else:
                
                deltae=1
            
                
                
        if(deltae!=0):
            
            prob=m.exp(-mass*g*(y_new-ypos[i]))
            prob2=min(1,prob)
                         
            random=np.random.uniform(0,1,1)
                
            if(prob2>=random):
                    
                xpos[i]=x_new
                ypos[i]=y_new
           
                 
plt.figure(figsize=(5, 10))
plt.scatter(xpos,ypos, s=np.pi*(sigma*4/2)**2)
plt.xlim(-Lx/2,Lx/2)
plt.ylim(-Ly/2,Ly/2)
plt.show()
