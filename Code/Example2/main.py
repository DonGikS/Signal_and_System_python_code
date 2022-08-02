import matplotlib.pyplot as plt
import exponential_t
import impulse_t
import convolution_t
def main():
    exponential_t.exponential_t()
    impulse_t.impulse_t()
    convolution_t.convolution_t()
    plt.tight_layout()
    plt.show()

main()
