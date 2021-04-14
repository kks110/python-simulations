import numpy as np
import random


class World:
    def __init__(self, y, x, food_per_day):
        self.EMPTY = 0.0
        self.WORLD_EDGE = 1.0
        self.FOOD = 2.0
        self.CREATURE = 3.0

        self.world_x = x
        self.world_y = y
        self.world_map = self.__generate_map()
        self.empty_spaces = []
        self.food_per_day = food_per_day
        self.__update_empty_spaces()

    def spawn_food(self):
        for _ in range(self.food_per_day):
            food_space_y, food_space_x = self.__find_free_space()
            self.world_map[food_space_y][food_space_x] = self.FOOD
            self.__update_empty_spaces()

    def spawn_creature(self):
        creature_space_y, creature_space_x = self.__find_free_space()
        self.world_map[creature_space_y][creature_space_x] = self.CREATURE
        self.__update_empty_spaces()
        return creature_space_y, creature_space_x

    def remove_creature(self, location):
        creature_space_y, creature_space_x = location
        self.world_map[creature_space_y][creature_space_x] = self.EMPTY
        self.__update_empty_spaces()

    def move_creature_and_eat(self, old_location, new_location):
        ate_food = False
        y_old_location, x_old_location = old_location
        y_new_location, x_new_location = new_location
        self.world_map[y_old_location][x_old_location] = self.EMPTY
        if self.world_map[y_new_location][x_new_location] == self.FOOD:
            ate_food = True
        self.world_map[y_new_location][x_new_location] = self.CREATURE
        self.__update_empty_spaces()
        return ate_food

    def end_day(self):
        for y in range(self.world_y):
            for x in range(self.world_x):
                if self.world_map[y][x] == self.FOOD:
                    self.world_map[y][x] = self.EMPTY
        self.__update_empty_spaces()

    def __find_free_space(self):
        space = self.empty_spaces[random.randint(0, len(self.empty_spaces) - 1)]
        return tuple(space)

    def __generate_map(self):
        world = np.ones((self.world_y, self.world_x))
        world[1:-1, 1:-1] = self.EMPTY
        return world

    def __update_empty_spaces(self):
        empty_spaces = []
        for y in range(self.world_y - 1):
            for x in range(self.world_x - 1):
                if self.world_map[y][x] == self.EMPTY:
                    empty_spaces.append((y,x))
        self.empty_spaces = empty_spaces
