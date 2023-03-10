import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')

# subplots - This function can generate one or more plots in the same figure
# fig represents the entire figure or collection of plots that are generated
# ax represents a single plot in the figure
fig, ax = plt.subplots()

# plot() will try to plot the data
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()