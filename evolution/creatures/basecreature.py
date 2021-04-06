import random


class BaseCreature:
    def __init__(self):
        self.type = 'base'
        self.spawn_rate = 100
        self.death_chance = 10
        self.replication_chance = 5
        self.mutation_chance = 10

    def should_i_spawn(self):
        return random.randint(1, 101) <= self.spawn_rate

    def should_i_die(self):
        return random.randint(1, 101) <= self.death_chance

    def should_i_reproduce(self):
        return random.randint(1, 101) <= self.replication_chance

    def should_i_mutate(self):
        return random.randint(1, 101) <= self.mutation_chance
