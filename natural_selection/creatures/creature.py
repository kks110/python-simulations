
class Creature:
    def __init__(self, world):
        self.vision = 1
        self.speed = 1
        self.food_consumed = 0
        self.location = world.spawn_creature()
