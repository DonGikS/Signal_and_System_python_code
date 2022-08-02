import matplotlib.pyplot as plt
import numpy as np


def convolution_t():
    #Print Plot location
    plt.subplot(3,1,3);
    
    # make data
    t1 = np.arange(0,10,.01)
    t2 = np.arange(0,3,.01)
    h = t2/3
    x = np.exp(-t1)
    y = np.convolve(x,h)
    t3 = np.arange(0,12.99,.01)
    plt.xlabel('Output Signal')
    plt.plot(t3,y)
    #plt.show()
