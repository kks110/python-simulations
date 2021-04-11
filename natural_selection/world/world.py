import numpy as np
import random


class World:
    def __init__(self, y, x):
        self.EMPTY = 0.0
        self.WORLD_EDGE = 1.0
        self.FOOD = 2.0
        self.CREATURE = 3.0

        self.world_x = x
        self.world_y = y
        self.world_map, self.empty_spaces = self.__generate_map()
        self.food_per_day = 10

    def spawn_food(self):
        for _ in range(0, self.food_per_day):
            food_space_y, food_space_x = self.__find_free_space()
            self.world_map[food_space_y][food_space_x] = self.FOOD

    def spawn_creature(self):
        creature_space_y, creature_space_x = self.__find_free_space()
        self.world_map[creature_space_y][creature_space_x] = self.CREATURE
        return creature_space_y, creature_space_x

    def remove_creature(self, location):
        creature_space_y, creature_space_x = location
        self.empty_spaces.append(location)
        self.world_map[creature_space_y][creature_space_x] = self.EMPTY

    def move_creature_and_eat(self, old_location, new_location):
        ate_food = False
        y_old_location, x_old_location = old_location
        y_new_location, x_new_location = new_location
        self.empty_spaces.append(old_location)
        self.world_map[y_old_location][x_old_location] = self.EMPTY
        if self.world_map[y_new_location][x_new_location] == self.FOOD:
            ate_food = True
        else:
            self.empty_spaces.remove(new_location)
        self.world_map[y_new_location][x_new_location] = self.CREATURE
        return ate_food

    def end_day(self):
        for y in range(0, self.world_y):
            for x in range(0, self.world_x):
                if self.world_map[y][x] == self.FOOD:
                    self.world_map[y][x] = self.EMPTY
                    self.empty_spaces.append((y, x))

    def __find_free_space(self):
        space = self.empty_spaces[random.randint(0, len(self.empty_spaces) - 1)]
        self.empty_spaces.remove(space)
        return tuple(space)

    def __generate_map(self):
        world = np.ones((self.world_y, self.world_x))
        world[1:-1, 1:-1] = self.EMPTY
        free_spaces = []
        for y in range(0, self.world_y - 1):
            for x in range(0, self.world_x - 1):
                if world[y][x] == self.EMPTY:
                    free_spaces.append((y,x))
        return world, free_spaces
