import matplotlib.pyplot as plt
import numpy as np

def discrete_Function():
    #Print Plot location
    #plt.subplot(3,1,2);
    
    # make data
    n = np.arange(-5,6,1)
    a = (n == -3)
    b= 3.*(n==-1)
    c=4.*(n==0)
    d=3.*(n==1)
    e=(n==2)
    f=-2.*(n==3)
    g=(n==4)

    z=a+b+c+d+e+f+g
    plt.stem(n,z,label='a')

    #Graph Range Setting
    plt.xlim(-5,6,1)
    plt.ylim(-5.,5.,1)
    plt.xlabel('n')
    plt.ylabel('x[n]')
    plt.yticks(range(-5,6))
    plt.xticks(range(-5,6))
    plt.grid(True,linestyle=':')
    plt.title('Discrete Function')
    plt.show()

discrete_Function()
