import matplotlib.pyplot as plt
import unitStepFunction as uSF
import unitRampFunction as uRF
import sineFunction as sF
def main():
    uSF.unitStepFunction()
    uRF.unitRampFunction()
    sF.sineFunction()
    plt.tight_layout()
    plt.show()

main()
