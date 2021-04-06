import numpy as np
import random


class World:
    def __init__(self):
        self.empty = 0.0
        self.world_edge = 1.0
        self.food = 2.0
        self.creature = 3.0

        self.world_x = 10
        self.world_y = 10
        self.world_map = self.__generate_map()
        self.food_per_day = 10

    def spawn_food(self):
        for _ in range(0, self.food_per_day):
            while True:
                x = random.randint(1, self.world_x - 2)
                y = random.randint(1, self.world_y - 2)
                if self.world_map[x][y] == self.empty:
                    self.world_map[x][y] = self.food
                    break

    def __generate_map(self):
        world = np.ones((self.world_x, self.world_y))
        world[1:-1, 1:-1] = self.empty
        return world
