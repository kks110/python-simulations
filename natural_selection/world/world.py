import numpy as np
import random


class World:
    def __init__(self):
        self.EMPTY = 0.0
        self.WORLD_EDGE = 1.0
        self.FOOD = 2.0
        self.CREATURE = 3.0

        self.world_x = 10
        self.world_y = 10
        self.world_map, self.empty_space = self.__generate_map()
        self.food_per_day = 10

    def spawn_food(self):
        for _ in range(0, self.food_per_day):
            food_space_x, food_space_y = self.__find_free_space()
            self.world_map[food_space_x][food_space_y] = self.FOOD

    def spawn_creature(self):
        creature_space_x, creature_space_y = self.__find_free_space()
        self.world_map[creature_space_x][creature_space_y] = self.CREATURE
        return creature_space_x, creature_space_y

    def __find_free_space(self):
        space = self.empty_space[random.randint(0, len(self.empty_space) - 1)]
        self.empty_space.remove(space)
        return tuple(space)

    def __generate_map(self):
        world = np.ones((self.world_x, self.world_y))
        world[1:-1, 1:-1] = self.EMPTY
        free_spaces = []
        for x in range(0, self.world_x - 1):
            for y in range(0, self.world_y - 1):
                if world[x][y] == self.EMPTY:
                    free_spaces.append([x,y])
        return world, free_spaces
