import numpy as np

class McCullohPittsNeuron:
    def __init__ (self, weights, threshold):
        self.weights = np.array(weights)
        self.threshold = threshold

    def activate(self, input):
        weighted_sum = np.dot(self.weights, input)
        return 1 if weighted_sum>= self.threshold else 0

def AND_gate():
    # Weights for AND gate: w1 = 1, w2 = 1, threshold = 2
    and_neuron = McCullohPittsNeuron([1, 1], 2)
    print("AND Gate:")
    print("0 AND 0 =", and_neuron.activate([0, 0]))  # Output = 0
    print("0 AND 1 =", and_neuron.activate([0, 1]))  # Output = 0
    print("1 AND 0 =", and_neuron.activate([1, 0]))  # Output = 0
    print("1 AND 1 =", and_neuron.activate([1, 1]))  # Output = 1

def OR_gate():
    # Weights for OR gate: w1 = 1, w2 = 1, threshold = 1
    or_neuron = McCullohPittsNeuron([1, 1], 1)
    print("\nOR Gate:")
    print("0 OR 0 =", or_neuron.activate([0, 0]))  # Output = 0
    print("0 OR 1 =", or_neuron.activate([0, 1]))  # Output = 1
    print("1 OR 0 =", or_neuron.activate([1, 0]))  # Output = 1
    print("1 OR 1 =", or_neuron.activate([1, 1]))  # Output = 1

def NOT_gate():
    # Weights for NOT gate: w1 = -1, threshold = 0
    not_neuron = McCullohPittsNeuron([-1], 0)
    print("\nNOT Gate:")
    print("NOT 0 =", not_neuron.activate([0]))  # Output = 1
    print("NOT 1 =", not_neuron.activate([1]))  # Output = 0

if __name__ == "__main__":
    AND_gate()  # Running AND gate
    OR_gate()   # Running OR gate
    NOT_gate()  # Running NOT gate
