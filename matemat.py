# First program with matplotlib ^o^
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values,squares, linewidth=5)

#defining title and axis labels
plt.title("Squares of numbers", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Squares of values", fontsize=14)

#defining the label's dimentions
plt.tick_params(axis='both', labelsize=14)

plt.show()
