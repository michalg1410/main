import numpy as np

#punkt 2

c=0
f=0

x_0=0
x_p=1

n=4

def wezly_tab(x_i, n):
  
  

# punkt3
def tab_geo(x_p, x_k, n):
    temp=(x_k-x_p) / (n - 1)
    wezly=np.array([x_p, x_k])

    for i in range(1, n-1, 1):
        wezly=np.block([wezly, i * temp + x_p])

    elementy=np.array([])
    n=n-1

    return wezly
print(tab_geo(1,2,5))



