import matplotlib.pyplot as plt


def plot_graph(data):
    # x axis values
    x = list(data['base_creatures'].keys())
    # corresponding y axis values
    y = list(data['base_creatures'].values())

    # x axis values
    x1 = list(data['orange_creatures'].keys())
    # corresponding y axis values
    y1 = list(data['orange_creatures'].values())

    # plotting the points
    plt.plot(x, y, label="Base Creatures")
    plt.plot(x1, y1, label="Orange Creatures")

    # naming the x axis
    plt.xlabel('Ticks')
    # naming the y axis
    plt.ylabel('Creatures Alive')

    # giving a title to my graph
    plt.title('Amount of Creatures Alive')

    # function to show the plot
    plt.show()
