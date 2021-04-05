import matplotlib.pyplot as plt


def plot_graph(data):
    # x axis values
    x = list(data.keys())
    # corresponding y axis values
    y = list(data.values())

    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('Ticks')
    # naming the y axis
    plt.ylabel('Creatures Alive')

    # giving a title to my graph
    plt.title('Amount of Creatures Alive')

    # function to show the plot
    plt.show()
