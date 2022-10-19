# Single Neuron
#Inisialisasi numpy
import numpy as np
# Inisialisasi variabel Input
inputs = [2,4,1,6,7,2,3,5,9,11]
# Inisialisasi variabel weights
weights = [  # Neuron
            0.8,0.12,0.5,0.13,0.4,0.2,1,0.6,0.25,0.4
          ]
bias = 3
# Perhitungan output (W1xI1+W2xI2......W10xI10)
output = np.dot(weights, inputs) + bias
#Print Output
print(output)

