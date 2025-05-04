import numpy as np
import matplotlib.pyplot as plt

class McCullohPittsNeuron:
    def __init__(self, weights, threshold):
        self.weights = np.array(weights)
        self.threshold = threshold

    def activate(self, inputs):
        return 1 if np.dot(self.weights,inputs) >= self.threshold else 0

def XOR_Gate():
    print("\nXOR Gate (using NAND, OR, AND neurons):")
    nand = McCullohPittsNeuron([-1, -1], -1)
    or_n = McCullohPittsNeuron([1, 1], 1)
    and_n = McCullohPittsNeuron([1, 1], 2)

    def xor_logic(x1, x2):
        return and_n.activate([nand.activate([x1,x2]), or_n.activate([x1,x2])])

    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for x1,x2 in inputs:
        result = xor_logic(x1, x2)
        print(f"{x1} XOR {x2} = {result}")
        color = 'red' if result else 'blue'
        plt.scatter(x1, x2, c=color)

    plt.title("XOR Gate Output")
    plt.xlabel("Input X1")
    plt.ylabel("Input X2")
    plt.legend(["Output = 1 (red)", "Output = 0 (blue)"])
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    XOR_Gate()
