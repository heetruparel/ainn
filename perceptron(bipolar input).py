import numpy as np

def activation(yin, theta):
    if yin > theta:
        return 1
    elif yin > -theta:
        return 0
    else:
        return -1

def train_perceptron(X, Y, w, b, lr=1.0, epochs=3, theta=0.2):
    for epoch in range(epochs):
        print(f"\nEpoch {epoch+1}")
        for i in range(len(X)):
            yin = np.dot(X[i], w) + b
            out = activation(yin, theta)
            error = Y[i] - out
            if error != 0:
                w += lr * Y[i] * X[i]
                b += lr * Y[i]
            print(f"Iter {i+1}: Weights = {w}, Bias = {b}")
    return w, b

def predict(X, w, b, theta=0.2):
    print("\nPredictions:")
    for x in X:
        yin = np.dot(x, w) + b
        out = activation(yin, theta)
        print(f"Input: {x}, Output: {out}")

# --- Main Program ---
if __name__ == "__main__":
    n = int(input("Enter number of features (e.g., 2 for x1 x2): "))
    m = int(input("Enter number of training samples: "))

    X = []
    Y = []

    print("Enter each input vector (space-separated) followed by target value:")
    for i in range(m):
        row = input(f"Sample {i+1} X (space-separated {n} values): ").strip().split()
        x_values = list(map(float, row[:n]))
        target = int(input(f"Sample {i+1} Y (target): "))
        X.append(x_values)
        Y.append(target)

    X = np.array(X)
    Y = np.array(Y)

    theta = float(input("Enter theta value: "))
    lr = float(input("Enter learning rate: "))
    epochs = int(input("Enter number of epochs: "))

    w = np.zeros(n)
    b = 0.0

    weights, bias = train_perceptron(X, Y, w, b, lr=lr, epochs=epochs, theta=theta)
    predict(X, weights, bias, theta)
