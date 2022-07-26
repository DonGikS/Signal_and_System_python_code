import matplotlib.pyplot as plt
import unitStepFunction as uSF
import unitRampFunction as uRF

def main():
    uSF.unitStepFunction()
    uRF.unitRampFunction()
    plt.tight_layout()
    plt.show()

main()
