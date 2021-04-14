import toml


class Config:
    def __init__(self):
        config = toml.load("natural_selection/config/config.toml")
        self.world_y_axis = config['world']['y_axis']
        self.world_x_axis = config['world']['x_axis']
        self.world_food_per_day = config['world']['food_per_day']
        self.world_days = config['world']['days']
        self.world_ticks_per_day = config['world']['ticks_per_day']
        self.creatures_initial_creature_count = config['creatures']['initial_creature_count']
        self.creatures_default_starting_vision = config['creatures']['default_starting_vision']
        self.creatures_default_starting_speed = config['creatures']['default_starting_speed']
