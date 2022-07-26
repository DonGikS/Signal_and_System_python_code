import matplotlib.pyplot as plt
import numpy as np

def sincFunction():
    #Print Plot location
    plt.subplot(2,3,6);
    
    # make data
    t = np.arange(-5,5,0.1)
    d = np.sinc(t)

    #Graph Range Setting
    plt.xlim(-5,5)
    plt.ylim(-1.0,2.0)
    plt.xlabel('time[sec]')
    plt.ylabel('Sinc Function')
    plt.plot(t,d)
    plt.grid(linestyle='--')
    #plt.show()
