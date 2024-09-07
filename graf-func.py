from matplotlib import pyplot as plt

x = range(1, 11, 1)
plt.plot(x, [(val ** 3 + 1 ) for val in x])

plt.show()