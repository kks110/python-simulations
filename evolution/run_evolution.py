from evolution.creatures.basecreature import BaseCreature
from evolution.creatures.orangecreature import OrangeCreature
from evolution.graphs.plot_graphs import plot_graph


def run():
    base_creatures = []
    orange_creatures = []
    history_of_life = {
        'base_creatures': {},
        'orange_creatures': {}
    }

    for _ in range(1, 3):
        base_creatures.append(BaseCreature())

    for tick in range(1, 10001):
        new_creature = BaseCreature()
        if new_creature.should_i_spawn():
            base_creatures.append(new_creature)

        if len(base_creatures) >= 2:
            base_creatures_to_add = 0
            orange_creatures_to_add = 0
            for living_creature in base_creatures:
                if living_creature.should_i_reproduce():
                    if living_creature.should_i_mutate():
                        orange_creatures_to_add += 1
                    else:
                        base_creatures_to_add += 1

            for _ in range(base_creatures_to_add):
                base_creatures.append(BaseCreature())
            for _ in range(orange_creatures_to_add):
                orange_creatures.append(OrangeCreature())

        if len(orange_creatures) >= 2:
            creatures_to_add = 0
            for living_creature in orange_creatures:
                if living_creature.should_i_reproduce():
                    creatures_to_add += 1
            for _ in range(creatures_to_add):
                orange_creatures.append(OrangeCreature())

        for creature in base_creatures:
            if creature.should_i_die():
                base_creatures.remove(creature)
        for creature in orange_creatures:
            if creature.should_i_die():
                orange_creatures.remove(creature)

        history_of_life['base_creatures'][tick] = len(base_creatures)
        history_of_life['orange_creatures'][tick] = len(orange_creatures)
    plot_graph(history_of_life)
