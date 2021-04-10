import random


class Creature:
    def __init__(self, world):
        self.vision = 1
        self.speed = 1
        self.food_consumed = 0
        self.location = world.spawn_creature()

    # def __pick_move_location(self, world):
    #     move_options = self.__movement_options(world)
    #     visible_food = bool(len(move_options['food']))
    #     visible_free_spaces = bool(len(move_options['free_space']))
    #
    #     if self.vision == 1:
    #         if visible_food:
    #             return random.choice(move_options['food'])
    #         elif visible_free_spaces:
    #             return random.choice(move_options['free_space'])
    #         else:
    #             return self.location
    #
    #     if visible_food:
    #         nearest = self.__nearest_food(move_options['food'])
    #         return self.__determine_move(nearest)
    #     if visible_free_spaces:
    #         return random.choice(move_options['free_space']
    #
    #     return self.location

    def __nearest_food(self, food_options):
        if len(food_options) == 1:
            return food_options[0]
        options = {}
        location_y = self.location[0]
        location_x = self.location[1]
        for choice in food_options:
            option_y = choice[0]
            option_x = choice[1]
            y_distance = abs(location_y - option_y)
            x_distance = abs(location_x - option_x)
            if y_distance < x_distance:
                if x_distance in options:
                    options[x_distance].append(choice)
                else:
                    options[x_distance] = [choice]
            else:
                if y_distance in options:
                    options[y_distance].append(choice)
                else:
                    options[y_distance] = [choice]
        return random.choice(options[min(options.keys())])

    # def __determine_move(self, food_location):


    def __movement_options(self, world):
        my_y = self.location[0]
        my_x = self.location[1]
        movement_options = {
            'food': [],
            'free_space': []
        }
        for y in range(-self.vision, self.vision + 1):
            for x in range(-self.vision, self.vision + 1):
                potential_location = world.world_map[my_y + y][my_x + x]
                if potential_location == world.FOOD:
                    movement_options['food'].append((my_y + y, my_x + x))
                if potential_location == world.EMPTY:
                    movement_options['free_space'].append((my_y + y, my_x + x))
        return movement_options
