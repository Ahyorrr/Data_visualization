from random import randint


class Die:
    """class representing the die attributes"""


    def __init__(self, num_sides=6):
        """initializing an 8 sided die"""
        self.num_sides = num_sides


    def roll(self):
        """method to roll die"""
        return randint(1, self.num_sides)
