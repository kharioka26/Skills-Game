import random

class Item:
    def __init__(self, name, xp_value):
        self.name = name
        self.xp_value = xp_value

class Mob:
    def __init__(self, name, health, xp_reward):
        self.name = name
        self.health = health
        self.xp_reward = xp_reward

class Player:
    def __init__(self):
        self.level = 1
        self.xp = 0
        self.inventory = []
        self.health = 100
        self.attack_power = 10
    
    def level_up(self):
        self.level += 1
        self.xp = 0
        self.health += 20
        self.attack_power += 5
        print(f"Congratulations! You've leveled up to Level {self.level}!")