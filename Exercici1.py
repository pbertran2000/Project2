import numpy as np
import matplotlib.pyplot as plt

phi=0.05
N=1000
sigma=1
delta=[0.001,0.003,0.01,0.03,0.1,0.3]
L=np.sqrt(np.pi*sigma**2*N/(4*phi))



    
xposini=np.zeros(N)
yposini=np.zeros(N)
    
xposini[0]=np.random.uniform(-L/2,L/2,size=1)
yposini[0]=np.random.uniform(-L/2,L/2,size=1)

for i in range(1,N,1):
    
    xposini[i]=np.random.uniform(-L/2,L/2,size=1)
    yposini[i]=np.random.uniform(-L/2,L/2,size=1)
    
    j=0
    
    while (j<i):
        
        if(np.sqrt((xposini[i]-xposini[j])**2+(yposini[i]-yposini[j])**2)<sigma):
            
            xposini[i] = np.random.uniform(-L/2,L/2,size=1)
            yposini[i] = np.random.uniform(-L/2,L/2,size=1)
            
            j=0
            
        else:
            
            j+=1 

#plt.scatter(xposini,yposini, s=np.pi*(sigma/2)**2)

xpos=[]
for i in range(0,len(xposini)):
    xpos.append(xposini[i])
    
ypos=[]
for i in range(0,len(yposini)):
    ypos.append(yposini[i])


xsave1=[]
xsave2=[]
ysave1=[]
ysave2=[]
T_t=100
D_list=[]



for l in range(0,len(delta),1):
    
    MSD_list=[]
    
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
            
            x_new=xpos[i]+delta[l]*(A[i]-0.5)
            y_new=ypos[i]+delta[l]*(B[i]-0.5)
            xsave1.append(xpos[i])
            ysave1.append(xpos[i])
            
            
            if x_new>L/2:
                       
                x_new=x_new-L
                        
                        
            if x_new<-L/2:
                        
                x_new=x_new+L
                            
                        
            if y_new>L/2:
                        
                y_new=y_new-L
                            
                        
            if y_new<-L/2:
                        
                y_new=y_new+L
    
            for k in range(0,N,1):

                if(np.sqrt((x_new-xpos[k])**2+(y_new-ypos[k])**2)<sigma and i!=k):
                
                
                    deltae=0
                    
                    break
                    
            
                
                
            if(deltae!=0):
                
                xpos[i]=x_new
                ypos[i]=y_new
                    
     
                    
                    
            xsave2.append(xpos[i])
            ysave2.append(ypos[i])
            
            aa[i]=xpos[i]-xposini[i]
            bb[i]=ypos[i]-yposini[i]
            
            if(aa[i]>L/2):
                
                aa[i]=aa[i]-L
                
            if(aa[i]<-L/2):
                
                aa[i]=aa[i]+L
                
            if(bb[i]<-L/2):
                
                bb[i]=bb[i]+L
                
            if(bb[i]>L/2):
                
                bb[i]=bb[i]-L
            

        r2=np.zeros(len(aa))

        for i in range(0,len(aa),1):

            r2[i]=aa[i]**2+bb[i]**2

        P=sum(r2)

        MSD=1/N*P

        MSD_list.append(MSD)
        
    pp=np.mean(MSD_list)
        
    D=pp/(4*T_t)
    D_list.append(D)
            
    t=np.linspace(0,100,100)
    

    plt.plot(t,MSD_list)
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('t')
    plt.ylabel('MSD')


plt.legend([r'$\delta$=0.001', r'$\delta$=0.003', r'$\delta$=0.01', r'$\delta$=0.03', r'$\delta$=0.1', r'$\delta$=0.3'], loc='upper center', bbox_to_anchor=(0.5, 1.35), ncol=3) 
plt.show()
    
    
plt.plot(delta,D_list)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$\delta$')
plt.ylabel('D')
plt.show()


            
        
                
                

            
 
    
    

