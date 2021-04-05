from evolution.creatures.basecreature import BaseCreature
from evolution.graphs.plot_graphs import plot_graph


def run():
    living_creatures = []
    history_of_life = {}
    # Have a mutation chance. Need to use it to mutate on replication.
    # Need to think about crowding and competition so population doesn't grow forever.

    for _ in range(1, 3):
        living_creatures.append(BaseCreature())

    for tick in range(1, 101):
        new_creature = BaseCreature()
        if new_creature.should_i_spawn():
            living_creatures.append(new_creature)

        if len(living_creatures) >= 2:
            creatures_to_add = 0
            for living_creature in living_creatures:
                if living_creature.should_i_reproduce():
                    creatures_to_add += 1
            for _ in range(0, creatures_to_add):
                living_creatures.append(BaseCreature())

        for creature in living_creatures:
            if creature.should_i_die():
                living_creatures.remove(creature)
        history_of_life[tick] = len(living_creatures)
    plot_graph(history_of_life)
