import matplotlib.pyplot as plt

x_values = [x for x in range(1, 1001)]
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# ax.scatter(x_values, y_values, s=10)
# Scatter with color
# ax.scatter(x_values, y_values, c='red', s=10)
# Scatter with RGB color
# ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)
# Scatter with colormap
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
# to-do not displaying correctly last number
ax.axis([0, 1100, 0, 1100000])

plt.show()

# Uncomment if you want to save to a file
# plt.savefig('squares_plot.png', bbox_inches='tight')
