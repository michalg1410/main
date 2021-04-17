import numpy as np
import matplotlib.pyplot as plt
#punkt 2

c = 0
f = 0

n=4
x_0=0
x_p=1


#węzły i elementy
wezly = np.array([[1,0],
                [2,1],
                [3,0.5],
                [4,0.75]])
elementy  =  np.array([[1,1,3],
                   [2,4,2],
                   [3,3,4]])
#warunki brzegowe
twb_L  =  'D'
twb_P  =  'D'

wwb_L  =  0
wwb_P = 1



n=len(wezly)


def genWezly(x_0,x_p,n):
    
    wezly_glob = np.array([1])
    
    for i in range (2,n+1,1):
        wezly_glob = np.block([[wezly_glob], [i]])
    
    wezly_loc = np.array([x_0])
    temp = (x_p - x_0)/n
    
    for i in range (1,n,1):
        wezly_loc = np.block([[wezly_loc], [i*temp+x_0]])
    
    wezly = np.block([wezly_glob,wezly_loc])
    
    return wezly
        


def genElementy(n):
    elementy_iwp = np.array([1])
    
    lp=np.array([1])
    for i in range (2,n,1):
        lp = np.block([[lp], [i]])
    
  
    for i in range (2,n,1):
        elementy_iwp = np.block([[elementy_iwp], [i]])
        
    elementy_iwk = np.array([1])
    
    for i in range (2,n,1):
        elementy_iwk = np.block([[elementy_iwk], [i]])
        
    elementy=np.block([lp,elementy_iwp,elementy_iwk])
    
    return elementy




def rysGeo(wezly,elementy):
    
    wezly_local = wezly[0,1]
    wezly_global = wezly[0,0]
    
    for i in range(1,len(wezly),1):
        wezly_local = np.block([wezly_local,wezly[i,1]])#nr lokalne węzłów
        
    plt.plot(wezly_local,np.zeros(len(wezly)),'|')
    plt.plot(np.block([min(wezly_local),max(wezly_local)]),[0,0])
    
    
    for i in range(1,len(wezly),1):
        wezly_global = np.block([wezly_global,wezly[i,0]])#nr globalne węzłów
        
    wezly_local = np.sort(wezly_local)
    wezly_global = np.sort(wezly_global)
        
        
    for i in range(0,len(wezly_local),1):
        plt.text(wezly_local[i],+0.005,wezly_local[i])
        plt.text(wezly_local[i],-0.01,wezly_global[i])
        
    ###########################################
    elementy_iwp = elementy[0,1]
    elementy_iwk = elementy[0,2]
    

    for i in range(1,len(elementy),1):
        elementy_iwp = np.block([elementy_iwp,elementy[i,1]])#nr globalne węzłów    
    
    for i in range(1,len(elementy),1):
        elementy_iwk = np.block([elementy_iwk,elementy[i,2]])#nr globalne węzłów
        
    for i in range(0,len(elementy),1):
        plt.text(wezly_local[i]+(wezly_local[i+1]-wezly_local[i])/2,+0.005,elementy_iwp[i])
        plt.text(wezly_local[i]+(wezly_local[i+1]-wezly_local[i])/2,-0.01,elementy_iwk[i])
        
    plt.show()
    return 0


#wezly = genWezly(x_0,x_p,n)
#elementy = genElementy(n)
rysGeo(wezly,elementy)