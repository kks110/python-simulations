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
            food_space_y, food_space_x = self.__find_free_space()
            self.world_map[food_space_y][food_space_x] = self.FOOD

    def spawn_creature(self):
        creature_space_y, creature_space_x = self.__find_free_space()
        self.world_map[creature_space_y][creature_space_x] = self.CREATURE
        return creature_space_y, creature_space_x

    def __find_free_space(self):
        space = self.empty_space[random.randint(0, len(self.empty_space) - 1)]
        self.empty_space.remove(space)
        return tuple(space)

    def __generate_map(self):
        world = np.ones((self.world_y, self.world_x))
        world[1:-1, 1:-1] = self.EMPTY
        free_spaces = []
        for y in range(0, self.world_y - 1):
            for x in range(0, self.world_x - 1):
                if world[y][x] == self.EMPTY:
                    free_spaces.append([y,x])
        return world, free_spaces
