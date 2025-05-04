import numpy as np

class McCullohPittsNeuron:
    def __init__ (self, weights, threshold):
        self.weights = np.array(weights)
        self.threshold = threshold

    def activate(self, input):
        weighted_sum = np.dot(self.weights, input)
        return 1 if weighted_sum>= self.threshold else 0

def AND_gate(weights, threshold):
    and_neuron = McCullohPittsNeuron(weights, threshold)
    print("AND Gate:")
    print("0 AND 0 =", and_neuron.activate([0, 0])) 
    print("0 AND 1 =", and_neuron.activate([0, 1]))  
    print("1 AND 0 =", and_neuron.activate([1, 0]))
    print("1 AND 1 =", and_neuron.activate([1, 1]))

def OR_gate(weights, threshold):
    or_neuron = McCullohPittsNeuron(weights, threshold)
    print("\nOR Gate:")
    print("0 OR 0 =", or_neuron.activate([0, 0]))
    print("0 OR 1 =", or_neuron.activate([0, 1])) 
    print("1 OR 0 =", or_neuron.activate([1, 0])) 
    print("1 OR 1 =", or_neuron.activate([1, 1])) 

def NOT_gate(weights, threshold):
    not_neuron = McCullohPittsNeuron(weights, threshold)
    print("\nNOT Gate:")
    print("NOT 0 =", not_neuron.activate([0])) 
    print("NOT 1 =", not_neuron.activate([1])) 

def get_user_input():
    gate = input("Enter the gate")
    num_inputs = int(input("enter number of weights, 2 for AND,NOT, OR. 1 for NOT"))
    weights = []
    for i in range(num_inputs):
        weight = float(input("enter weight"))
        weights.append(weight)
    threshold = float(input("enter threshold"))
    return gate, weights, threshold

if __name__ == "__main__":
    gate, weights, threshold = get_user_input()
    if gate == "AND":
        AND_gate(weights, threshold)
    elif gate == "OR":
        OR_gate(weights, threshold)
    elif gate == "NOT":
        NOT_gate(weights, threshold) 

