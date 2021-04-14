import random


class Creature:
    def __init__(self, world, vision, speed):
        self.vision = vision
        self.speed = speed
        self.food_consumed = 0
        self.location = world.spawn_creature()
        self.dead = False
        self.move_history = {
            'locations': [self.location],
            'food_consumed': [self.food_consumed]
        }

    def move(self, world):
        for _ in range(self.speed):
            move_location = self.__pick_move_location(world)
            i_ate = world.move_creature_and_eat(self.location, move_location)
            self.location = move_location
            self.move_history['locations'].append(self.location)
            if i_ate:
                self.food_consumed += 1
                self.move_history['food_consumed'].append(self.food_consumed)

    def spawn_new_creature(self, world):
        vision_low_point = self.vision - 1 if self.vision > 0 else 1
        vision_mutation = random.choice([vision_low_point, self.vision, self.vision + 1])

        speed_low_point = self.speed - 1 if self.speed > 1 else 1
        speed_mutation = random.choice([speed_low_point, self.speed, self.speed + 1])

        if self.food_consumed >= 2:
            return Creature(world=world, vision=vision_mutation, speed=speed_mutation)
        return False

    def end_day(self, world):
        if self.food_consumed == 0:
            self.__kill(world)
        self.food_consumed = 0

    def __kill(self, world):
        self.dead = True
        world.remove_creature(self.location)

    def __pick_move_location(self, world):
        move_options = self.__movement_options(world)
        visible_food = bool(len(move_options['food']))
        visible_free_spaces = bool(len(move_options['free_space']))

        if self.vision == 1:
            if visible_food:
                return random.choice(move_options['food'])
            elif visible_free_spaces:
                return random.choice(move_options['free_space'])
            else:
                return self.location

        if visible_food:
            nearest = self.__nearest_food(move_options['food'])
            return self.__determine_move_to_food(nearest)
        if visible_free_spaces:
            return self.__determine_move(move_options['free_space'])

        return self.location

    def __nearest_food(self, food_options):
        if len(food_options) == 1:
            return food_options[0]
        options = {}
        location_y, location_x = self.location
        for choice in food_options:
            option_y, option_x = choice
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
        choice = random.choice(options[min(options.keys())])
        return choice

    def __determine_move(self, move_options):
        allowed_options = []
        my_y, my_x = self.location
        for option in move_options:
            options_y, options_x = option
            if abs(options_y - my_y) <= self.speed and abs(options_x - my_x) <= self.speed:
                allowed_options.append(option)
        if allowed_options:
            return random.choice(allowed_options)
        else:
            return self.location

    def __determine_move_to_food(self, food_location):
        new_location = []
        y_food, x_food = food_location
        y_creature, x_creature = self.location
        y_distance = y_food - y_creature
        x_distance = x_food - x_creature
        if y_distance < 0:
            new_location.append(y_creature - 1)
        elif y_distance > 0:
            new_location.append(y_creature + 1)
        else:
            new_location.append(y_creature)

        if x_distance < 0:
            new_location.append(x_creature - 1)
        elif x_distance > 0:
            new_location.append(x_creature + 1)
        else:
            new_location.append(x_creature)
        return tuple(new_location)

    def __movement_options(self, world):
        my_y, my_x = self.location
        movement_options = {
            'food': [],
            'free_space': []
        }
        for y in range(-self.vision, self.vision + 1):
            for x in range(-self.vision, self.vision + 1):
                if abs(my_y + y) < world.world_y and abs(my_x + x) < world.world_x:
                    if my_y + y >= 0 and my_x + x >= 0:
                        potential_location = world.world_map[my_y + y][my_x + x]
                        if potential_location == world.FOOD:
                            movement_options['food'].append((my_y + y, my_x + x))
                        if potential_location == world.EMPTY:
                            movement_options['free_space'].append((my_y + y, my_x + x))
        return movement_options
