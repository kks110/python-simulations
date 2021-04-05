import random


class BaseCreature:
    def __init__(self):
        self.spawn_rate = 100
        self.death_chance = 10
        self.replication_rate = 5
        self.mutation_chance = 10

    def should_i_spawn(self):
        return random.randint(1, 101) <= self.spawn_rate

    def should_i_die(self):
        return random.randint(1, 101) <= self.death_chance

    def should_i_reproduce(self):
        return random.randint(1, 101) <= self.replication_rate
