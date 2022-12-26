import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

# subplots - This function can generate one or more plots in the same figure
# fig represents the entire figure or collection of plots that are generated
# ax represents a single plot in the figure
fig, ax = plt.subplots()

# plot() will try to plot the data
ax.plot(squares)

plt.show()