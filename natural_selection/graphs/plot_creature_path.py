from natural_selection.graphs.plot_graphs import plot_graph


def plot_path_of_creature(creature, world):
    creature_y_location = []
    creature_x_location = []
    for location in creature.move_history['locations']:
        creature_y_location.append(location[0])
        creature_x_location.append(location[1])
    plot_graph(creature_y_location, creature_x_location, world.world_y, world.world_x)