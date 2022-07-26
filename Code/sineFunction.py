import matplotlib.pyplot as plt
import numpy as np

def sineFunction():
    #Print Plot location
    plt.subplot(2,3,3);
    
    # make data
    t = np.arange(-5,5,0.1)
    d = np.sin(t)

    #Graph Range Setting
    plt.xlim(-5,5)
    plt.ylim(-1.0,1.0)
    plt.xlabel('time[sec]')
    plt.ylabel('Sine Function')
    plt.plot(t,d)
    plt.grid()
    #plt.show()
