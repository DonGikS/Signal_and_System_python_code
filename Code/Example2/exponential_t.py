import matplotlib.pyplot as plt
import numpy as np

def exponential_t():
    #Print Plot location
    plt.subplot(3,1,1);
    
    # make data
    t = np.arange(-5,10,0.1)
    x = np.exp(-t)

    #Graph Range Setting
    plt.xlim(0,10)
    plt.ylim(0,1,0.1)
    plt.xlabel('Input Signal')
    #plt.ylabel('Sinc Function')
    plt.plot(t,x)
    #plt.grid(linestyle='--')
    #plt.show()
