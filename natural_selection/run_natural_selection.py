from natural_selection.world.world import World


def run():
    world = World()
    print(world.world_map)
    world.spawn_food()
    print(world.world_map)