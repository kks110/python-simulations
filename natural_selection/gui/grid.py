import tkinter as tk


class Grid():
    def __init__(self, world):
        self.labels = {}
        for y in range(world.world_y):
            for x in range(world.world_x):
                if world.world_map[y][x] == world.WORLD_EDGE:
                    self.labels[(y, x)] = tk.Label(text="", bg="black", fg="white")
                    self.labels[(y, x)].grid(row=y, column=x)
                if world.world_map[y][x] == world.FOOD:
                    self.labels[(y, x)] = tk.Label(text="F", bg="green", fg="white")
                    self.labels[(y, x)].grid(row=y, column=x)
                if world.world_map[y][x] == world.CREATURE:
                    self.labels[(y, x)] = tk.Label(text="C", bg="blue", fg="white")
                    self.labels[(y, x)].grid(row=y, column=x)
                else:
                    self.labels[(y, x)] = tk.Label(text="", bg="white", fg="white")
                    self.labels[(y, x)].grid(row=y, column=x)

    def update_grid(self, world):
        for y in range(world.world_y):
            for x in range(world.world_x):
                label = self.labels[(y, x)]
                if world.world_map[y][x] == world.EMPTY:
                    label.configure(text="", bg="white")
                if world.world_map[y][x] == world.WORLD_EDGE:
                    label.configure(text="", bg="black")
                if world.world_map[y][x] == world.FOOD:
                    label.configure(text="F", bg="green")
                if world.world_map[y][x] == world.CREATURE:
                    label.configure(text="C", bg="blue")
                self.labels[(y, x)] = label
