# p1.py

# Other neurons will sent outputs to this neuron as inputs
inputs = [1.2, 5.1, 2.1]
# inputs will also have uniques weights attached
weights = [3.1, 2.1, 8.7]
# every neuron (this) will have a unique bias
bias = 3

output = 0
# output = input 1 * bias 1 + input 2 * bias 2 etc...
for element1, element2 in zip(inputs, weights):
    output += element1 * element2

print(output+bias)
