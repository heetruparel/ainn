import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Initialize inputs and weights
Xi = [
    np.array([0.5, -1.0, 0.5, 1.0]),
    np.array([1.0, 0.5, -0.5, -1.0]),
    np.array([-0.5, 1.5, 1.0, -0.5])
]

d = np.array([0, 0, 1])  # Target output 
w = np.array([0.2, -0.1, 0.15, -0.05])  # initial weights
alpha = 0.05  # learning rate
errors = [] 

print("Initial Weights:", w)

for i in range(len(d)):
    x = Xi[i]  # Select input vector
    net_input = np.dot(w, x)  # Compute the weighted sum
    y = sigmoid(net_input)  # Compute output using sigmoid
    error = d[i] - y  # Compute error
    y_derivative = sigmoid_derivative(y)  # Compute derivative of sigmoid
    delta_w = alpha * error * y_derivative * x  # Compute weight adjustment
    w += delta_w  # Update weights
    errors.append(abs(error))  # Store absolute error for plotting

    print(f"Iteration {i+1}:")
    print("Input Vector:", x)
    print("Net Output:", net_input)
    print("Prediction (Sigmoid):", y)
    print("Error:", error)
    print("Weight Change:", delta_w)
    print("Updated Weights:", w)
    print("----------------------------------")

print("Final Weights:", w)

# Plot error reduction over iterations
plt.plot(range(1, len(d) + 1), errors, marker='o', linestyle='-', color='r')
plt.xlabel('Iteration')
plt.ylabel('Absolute Error')
plt.title('Error Reduction Over Iterations')
plt.grid()
plt.show()
