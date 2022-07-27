import matplotlib.pyplot as plt
import unitStepFunction as uSF
import unitRampFunction as uRF
import sineFunction as sF
import cosineFunction as cF
import exponentialFunction as eF
import sincFunction as scF

def main():
    uSF.unitStepFunction()
    uRF.unitRampFunction()
    sF.sineFunction()
    cF.cosineFunction()
    eF.exponentialFunction()
    scF.sincFunction()
    plt.tight_layout()
    plt.show()

main()
