import matplotlib.pyplot as plt
import numpy as np

def convolution_sum():

    n1 = np.arange(-10,30,1)
    x = (n1+1)*(0<=n1)*(n1<=3)
    h = 1*(-1<=n1)*(n1<=2)
    y = np.convolve(x,h)
    n2 = np.arange(-10,69,1)

    
    plt.subplot(3,1,1);
    plt.xlabel('n')
    plt.ylabel('x(n)')
    plt.xlim(-6, 10, 1)
    plt.ylim(-4,6,1)
    plt.stem(n1,x)
    plt.grid(True,linestyle=':')
    plt.title('(a) Input Signal')
    
    plt.subplot(3,1,2);
    plt.xlabel('n')
    plt.ylabel('h(n)')
    plt.xlim(-10, 10, 1)
    plt.ylim(-4,4,1)
    plt.stem(n1,h)
    plt.grid(True,linestyle=':')
    plt.title('(b) Impulse Signal')
    
    plt.subplot(3,1,3);
    plt.xlabel('n')
    plt.ylabel('y(n)')
    plt.xlim(0, 25, 1)
    plt.ylim(-4,15,1)
    plt.stem(n2,y)
    plt.grid(True,linestyle=':')
    plt.title('(c) Output Signal')
    
    plt.tight_layout()
    plt.show()
    

convolution_sum()
