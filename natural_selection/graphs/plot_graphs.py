import matplotlib.pyplot as plt


def plot_graph(y_location, x_location, world_y, world_x):
    # x axis values
    x = x_location
    # corresponding y axis values
    y = y_location

    # plotting the points
    plt.plot(x, y, label="Creature Path")

    # naming the x axis
    plt.xlabel('X Location')
    # naming the y axis
    plt.ylabel('Y Location')

    # giving a title to my graph
    plt.title('Creatures Path')

    plt.ylim([0, world_y - 1])
    plt.xlim([0, world_x - 1])

    plt.grid()

    # function to show the plot
    plt.show()
