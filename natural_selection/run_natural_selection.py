from natural_selection.world.world import World
from natural_selection.creatures.creature import Creature
from natural_selection.graphs.graph_plotter import GraphPlotter
from natural_selection.config.config import Config


def run():
    config = Config()
    world = World(y=config.world_y_axis, x=config.world_x_axis, food_per_day=config.world_food_per_day)
    creatures = []
    cycle_and_creature_count = []
    creatures_speed = {}
    creatures_vision = {}
    for _ in range(config.creatures_initial_creature_count):
        creatures.append(Creature(world=world, vision=config.creatures_default_starting_vision, speed=config.creatures_default_starting_speed))

    for cycle in range(config.world_days):
        world.spawn_food()
        for _ in range(config.world_ticks_per_day):
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

        creatures_to_remove =[]
        for creature in creatures:
            if creature.dead:
                creatures_to_remove.append(creature)

        for creature in creatures_to_remove:
            creatures.remove(creature)

        cycle_and_creature_count.append((cycle, len(creatures)))
        world.end_day()

    for creature in creatures:
        if creature.speed not in creatures_speed:
            creatures_speed[creature.speed] = 1
        else:
            creatures_speed[creature.speed] += 1

        if creature.vision not in creatures_vision:
            creatures_vision[creature.vision] = 1
        else:
            creatures_vision[creature.vision] += 1

    GraphPlotter.plot_path_of_creature(creatures[0], world)
    GraphPlotter.plot_creature_count(cycle_and_creature_count)
    GraphPlotter.plot_creature_mutations(stats=creatures_speed, mutation_type='Speed')
    GraphPlotter.plot_creature_mutations(stats=creatures_vision, mutation_type='Vision')
