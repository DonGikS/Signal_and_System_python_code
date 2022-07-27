import matplotlib.pyplot as plt
import numpy as np

def exponentialFunction():
    #Print Plot location
    plt.subplot(2,3,5);
    
    # make data
    t = np.arange(-5,5,0.1)
    d = np.exp(t)

    #Graph Range Setting
    plt.xlim(-5,5)
    plt.ylim(-1.0,10.0)
    plt.xlabel('time[sec]')
    plt.ylabel('Exponential Function')
    plt.plot(t,d)
    plt.grid(linestyle='--')
    #plt.show()
