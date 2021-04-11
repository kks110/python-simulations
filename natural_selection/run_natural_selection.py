from natural_selection.world.world import World
from natural_selection.creatures.creature import Creature
from natural_selection.graphs.plot_creature_path import plot_path_of_creature


def run():
    world = World(y=10, x=10, food_per_day=10)
    creatures = []
    for _ in range(0, 10):
        creatures.append(Creature(world))

    for _ in range(0, 2):
        world.spawn_food()
        for _ in range(0, 10):
            for creature in creatures:
                creature.move(world)
        new_creatures = []
        for creature in creatures:
            spawn_new_creature = creature.spawn_new_creature(world)
            if spawn_new_creature:
                new_creatures.append(spawn_new_creature)
        for creature in creatures:
            creature.end_day(world)
        creatures = creatures + new_creatures
        world.end_day()

    plot_path_of_creature(creatures[0], world)
