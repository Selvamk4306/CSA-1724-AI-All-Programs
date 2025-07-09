import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_der(x):
    return x * (1 - x)

inputs = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

outputs = np.array([[0],[1],[1],[0]])

np.random.seed(42)

input_neurons = inputs.shape[1]
hidden_neu = 3
opt_neu = 1

# Initialize weights and biases
hidden_weight = np.random.uniform(size=(input_neurons, hidden_neu))
opt_weight = np.random.uniform(size=(hidden_neu, opt_neu))
hidden_bias = np.random.uniform(size=(1, hidden_neu))
opt_bias = np.random.uniform(size=(1, opt_neu))

epochs = 10000
learning_rate = 0.1

for epoch in range(epochs):
    # Forward propagation
    hidden_layer_input = np.dot(inputs, hidden_weight) + hidden_bias
    hidden_layer_output = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_output, opt_weight) + opt_bias
    predicted_output = sigmoid(output_layer_input)

    # Backpropagation
    error = outputs - predicted_output
    d_predicted_output = error * sigmoid_der(predicted_output)

    error_hidden_layer = d_predicted_output.dot(opt_weight.T)
    d_hidden_layer = error_hidden_layer * sigmoid_der(hidden_layer_output)

    # Updating weights and biases
    opt_weight += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
    opt_bias += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate

    hidden_weight += inputs.T.dot(d_hidden_layer) * learning_rate
    hidden_bias += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

    # Print loss occasionally
    if (epoch+1) % 1000 == 0:
        loss = np.mean(np.square(error))
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss:.4f}")

print("\nFinal predicted output:")
print(predicted_output.round(3))
