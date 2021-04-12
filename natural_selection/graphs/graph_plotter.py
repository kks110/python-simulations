import matplotlib.pyplot as plt


class GraphPlotter:
    @classmethod
    def plot_path_of_creature(cls, creature, world):
        creature_y_location = []
        creature_x_location = []
        for location in creature.move_history['locations']:
            creature_y_location.append(location[0])
            creature_x_location.append(location[1])
        # x axis values
        x = creature_x_location
        # corresponding y axis values
        y = creature_y_location

        # plotting the points
        plt.plot(x, y, label="Creature Path")

        # naming the x axis
        plt.xlabel('X Location')
        # naming the y axis
        plt.ylabel('Y Location')

        # giving a title to my graph
        plt.title('Creatures Path')

        plt.ylim([0, world.world_y - 1])
        plt.xlim([0, world.world_x - 1])

        plt.grid()

        # function to show the plot
        plt.show()

    @classmethod
    def plot_creature_mutations(cls, stats, mutation_type):
        mutation = list(stats.keys())
        counts = list(stats.values())

        # x axis values
        x = mutation
        # corresponding y axis values
        y = counts

        # plotting the points
        plt.bar(x, y)

        # naming the x axis
        plt.xlabel(mutation_type)
        # naming the y axis
        plt.ylabel('Amounts')

        # giving a title to my graph
        plt.title(f"{mutation_type} mutation")

        # function to show the plot
        plt.show()

    @classmethod
    def plot_creature_count(cls, cycle_and_count):
        cycle_data = []
        count_data = []
        for data in cycle_and_count:
            cycle, count = data
            cycle_data.append(cycle)
            count_data.append(count)

        # x axis values
        x = cycle_data
        # corresponding y axis values
        y = count_data

        # plotting the points
        plt.plot(x, y)

        # naming the x axis
        plt.xlabel('Cycle')
        # naming the y axis
        plt.ylabel('Creature Count')

        # giving a title to my graph
        plt.title('Creature Count')

        plt.ylim([0, max(count_data) + 5])
        plt.xlim([0, len(cycle_data) + 5])

        # function to show the plot
        plt.show()
