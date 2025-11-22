import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

y1 = [2, 4, 6, 8]
y2 = [1, 3, 5, 7]

plt.plot(x, y1)
plt.plot(x, y2)

plt.legend(["Line 1", "Line 2"])
plt.title("Two Lines in One Graph")

plt.show()
