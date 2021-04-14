from natural_selection.world.world import World
from natural_selection.creatures.creature import Creature
from natural_selection.graphs.graph_plotter import GraphPlotter
import tkinter as tk
import time
from natural_selection.gui.grid import Grid


def set_up_screen(world):
    window = tk.Tk()
    for y in range(world.world_y):
        window.rowconfigure(y, weight=1, minsize=10)
    for x in range(world.world_x):
        window.columnconfigure(x, weight=1, minsize=10)
    grid = Grid(world)
    return window, grid


def run():
    world = World(y=20, x=20, food_per_day=10)
    creatures = []
    cycle_and_creature_count = []
    creatures_speed = {}
    creatures_vision = {}
    window, grid = set_up_screen(world)
    for _ in range(0, 1):
        creatures.append(Creature(world=world, vision=1, speed=1))

    for cycle in range(0, 2):
        world.spawn_food()
        for _ in range(0, 5):
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

        window.after(1000, grid.update_grid(world))
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

    window.mainloop()
    # GraphPlotter.plot_path_of_creature(creatures[0], world)
    # GraphPlotter.plot_creature_count(cycle_and_creature_count)
    # GraphPlotter.plot_creature_mutations(stats=creatures_speed, mutation_type='Speed')
    # GraphPlotter.plot_creature_mutations(stats=creatures_vision, mutation_type='Vision')
