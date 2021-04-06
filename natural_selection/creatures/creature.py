
class Creature:
    def __init__(self, world):
        self.vision = 1
        self.speed = 1
        self.food_consumed = 0
        self.location = world.spawn_creature()

    def __movement_options(self, world):
        my_x = self.location[0]
        my_y = self.location[1]
        movement_options = {
            'food': [],
            'free_space': []
        }
        for x in range(-self.vision, self.vision + 1):
            for y in range(-self.vision, self.vision + 1):
                potential_location = world.world_map[my_x + x][my_y + y]
                if potential_location == world.FOOD:
                    movement_options['food'].append((my_x + x, my_y + y))
                if potential_location == world.EMPTY:
                    movement_options['free_space'].append((my_x + x, my_y + y))
        return movement_options