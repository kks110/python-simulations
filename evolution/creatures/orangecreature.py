from evolution.creatures.basecreature import BaseCreature


class OrangeCreature(BaseCreature):
    def __init__(self):
        super().__init__()
        self.type = 'orange'
        self.spawn_rate = 0
        self.death_chance = 10
        self.replication_chance = 10
        self.mutation_chance = 10
