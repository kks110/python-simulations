from natural_selection.world.world import World
from natural_selection.creatures.creature import Creature


def run():
    world = World()

    creatures = []
    for _ in range(0, 5):
        creatures.append(Creature(world))

    world.spawn_food()
