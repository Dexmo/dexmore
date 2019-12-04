import matplotlib.pyplot as plt

plt.scatter(2,4, s=200)

plt.title("Punkt", fontsize=24)
plt.xlabel("Axis X", fontsize=12)
plt.ylabel("Axis Y", fontsize=12)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
