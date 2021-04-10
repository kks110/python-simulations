from natural_selection.world.world import World
from natural_selection.creatures.creature import Creature


def run():
    world = World()

    creatures = []
    for _ in range(0, 1):
        creatures.append(Creature(world))

    world.spawn_food()
    print(creatures[0].location)
    print(world.world_map)
    print(creatures[0].nearest_food(world))
