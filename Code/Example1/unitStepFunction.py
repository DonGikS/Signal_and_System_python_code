import matplotlib.pyplot as plt
import numpy as np

def unitStepFunction():
    #Print Plot location
    plt.subplot(2,3,1);
    
    # make data
    t = np.arange(-5,10,0.1)
    b = np.heaviside(t,0.5)

    #Graph Range Setting
    plt.xlim(-5,10)
    plt.ylim(-1.0,2.0)
    plt.xlabel('time[sec]')
    plt.ylabel('Unit Step Function')
    plt.plot(t,b)
    plt.grid(linestyle='--')
    #plt.show()
