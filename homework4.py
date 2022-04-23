# -*- coding: utf-8 -*-
"""homework_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z-404Tzt6iGfloUgjcE_NL9VnzTAHaG5
"""

# ECE 5400: Applied Machine Learning
# Homework 4
# Authors: Raymond Ogunjimi and Cesar Nunez Rodriguez

import numpy as np

# Input
inputs = np.array([[0,0],[0,1],[1,0],[1,1]])

#or_output = np.array([[0],[1],[1],[1]])
#and_output = np.array([[0],[0],[0],[1]])
#nand_output = np.array([[1],[1],[1],[0]])

# Expected output
xor_output = np.array([[0],[1],[1],[0]])

# Initialize neuron size for each layer
input_layer_size = 2
hidden_layer_size = 2
target_layer_size = 1

# Find weights and bias for each layer
hidden_weights = np.random.uniform(size=(input_layer_size,hidden_layer_size))
hidden_bias = np.zeros(hidden_layer_size)

output_weights = np.random.uniform(size=(hidden_layer_size,target_layer_size))
output_bias = np.zeros(target_layer_size)

def sigmoid (x):
    return 1/(1 + np.exp(-x))

# Calculate neuron values
hidden_layer_activation = np.dot(inputs,hidden_weights)
hidden_layer_activation = hidden_layer_activation + hidden_bias

hidden_layer_output = sigmoid(hidden_layer_activation)

output_layer_activation = np.dot(hidden_layer_output,output_weights)
output_layer_activation += output_bias

print("output_layer_activation: ", output_layer_activation)
output_prediction = sigmoid(output_layer_activation)

print("\nInitial output values (before backpropagation):")
print(output_prediction)

def sigmoid_derivative(x):
    return x * (1 - x)

# Backpropagate
passes = 500
for epoch in range(0, passes):
    error = xor_output - output_prediction

    if(epoch == 0):
        print("sigmoid_derivative(output_prediction): ", sigmoid_derivative(output_prediction))
    output_prediction_derived = error * sigmoid_derivative(output_prediction)
    
    error_hidden_layer = output_prediction_derived.dot(output_weights.T)
    hidden_layer_derived = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    output_weights = output_weights + hidden_layer_output.T.dot(output_prediction_derived)
    output_bias = output_bias + np.sum(output_prediction_derived,axis=0,keepdims=True)

    hidden_weights = hidden_weights + inputs.T.dot(hidden_layer_derived)
    hidden_bias = hidden_bias + np.sum(hidden_layer_derived,axis=0,keepdims=True)

    # Calculate neuron values
    hidden_layer_activation = np.dot(inputs,hidden_weights)
    hidden_layer_activation = hidden_layer_activation + hidden_bias

    hidden_layer_output = sigmoid(hidden_layer_activation)

    output_layer_activation = np.dot(hidden_layer_output,output_weights)
    output_layer_activation += output_bias

    output_prediction = sigmoid(output_layer_activation)

print("\nFinal output values (after backpropagation):")
print(output_prediction)
print("\nFinal output (compare to xor):")
print(np.around(output_prediction))