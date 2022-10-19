# Multi Neuron
import numpy as np
inputs = [2.0,-1.4,3.9,-2.15,4.-0,7.1,5.2,6.4,7.5,-1.12]
weights = [
            #Neuron 1
            [0.4,-0.8,0.1,0.2,0.5,-2.0,0.7,0.13,-0.45,0.6],
            #Neuron 2
            [0.26,0.91,0.14,-0.25,0.54,0.52,0.21,-0.82,0.31,-0.42],
            #Neuron 3
            [-0.51,0.44,0.17,-0.32,0.46,0.67,-0.12,0.19,0.34,-0.71],
            #Neuron 4
            [0.2,-0.41,0.3,-0.6,0.52,0.72,0.35,0.66,-0.82,0.12],
            #Neuron 5
            [0.14,0.8,0.75,-0.86,0.41,0-.65,0.22,0.6,0.7,-0.55]] 
biases = [2.0,4.0,1.5,3.0,0.5]
# Perhitungan output
layer_outputs = np.dot(weights, inputs) + biases
# Print layer_output
print(layer_outputs)