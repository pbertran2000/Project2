import numpy as np
import matplotlib.pyplot as plt
import copy

phi=0.05
N=256
sigma=1
delta=0.1
L=np.sqrt(np.pi*sigma**2*N/(4*phi))
xposini=[]
yposini=[]
x_0=-8
y_0=-8
T_t=3500



for j in range(0,16):
    
    for i in range(0,16):
        
        if(j%2==1):
            
            a=sigma/2
            
        if(j%2==0):
            
            a=0
        
        xposini_i=sigma*i+x_0+a
        yposini_i=sigma*j+y_0
        
        
        
        xposini=np.append(xposini,xposini_i)
        yposini=np.append(yposini,yposini_i)
        

plt.scatter(xposini,yposini, s=np.pi*(sigma*3/2)**2)
plt.xlim(-L/2,L/2)
plt.ylim(-L/2,L/2)
plt.show()

xpos=[]
for i in range(0,len(xposini)):
    xpos.append(xposini[i])
    
ypos=[]
for i in range(0,len(yposini)):
    ypos.append(yposini[i])

for j in range(0,T_t,1):
        
    xsave1=[]
    xsave2=[]
    ysave1=[]
    ysave2=[]
    deltae=1
    aa=np.zeros(N)
    bb=np.zeros(N)
    A=np.random.uniform(0,1,N)
    B=np.random.uniform(0,1,N)
        
    for ii in range(0,N,1):
        
        deltae=1
            
        i = np.random.randint(0,N-1)
            
        x_new=xpos[i]+delta*(A[i]-0.5)
        y_new=ypos[i]+delta*(B[i]-0.5)
        
        if x_new>L/2:
                   
            x_new=x_new-L
                    
                    
        if x_new<-L/2:
                    
            x_new=x_new+L
                        
                    
        if y_new>L/2:
                    
            y_new=y_new-L
                        
                    
        if ypos[i]<-L/2:
                    
            y_new=y_new+L
        

        for k in range(0,N,1):

            if(np.sqrt((x_new-xpos[k])**2+(y_new-ypos[k])**2)<sigma and i!=k):
                
                
                deltae=0
                break
            
            else:
                
                deltae=1
            
                
                
        if(deltae!=0):
                
            xpos[i]=x_new
            ypos[i]=y_new
            

            
                 

plt.scatter(xpos,ypos, s=np.pi*(sigma*3/2)**2)
plt.xlim(-L/2,L/2)
plt.ylim(-L/2,L/2)
plt.show()
                        
                    



    


            
        
                
                