import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def unitRampFunction():
    #Print Plot location
    plt.subplot(2,3,2);
    
    # make data
    t = np.arange(-5,10,0.1)
    c = np.maximum(0,t)

    #Graph Range Setting
    plt.xlim(-5,10)
    plt.ylim(-1,10.0)
    plt.xlabel('time[sec]')
    plt.ylabel('Unit Ramp Function')
    plt.plot(t,c)
    plt.grid()
    #plt.show()
