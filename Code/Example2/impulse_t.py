import matplotlib.pyplot as plt
import numpy as np

def impulse_t():
    #Print Plot location
    plt.subplot(3,1,2);
    
    # make data
    t = np.arange(0,3,0.01)
    h = t/3

    #Graph Range Setting
    plt.xlim(0,3)
    plt.ylim(0,1,0.1)
    plt.xlabel('Impulse Response')
    #plt.ylabel('Sinc Function')
    plt.plot(t,h)
    #plt.grid(linestyle='--')
    #plt.show()
