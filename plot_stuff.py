import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [12, 5, 7, 2]

plt.figure()
plt.scatter(x, y)
plt.scatter(y, x)
plt.title('Well locations')
# plt.axis([-102.5538, -102.554, 43.015, 43.03])
plt.show()
