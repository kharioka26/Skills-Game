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

   def gain_xp(self, amount):
        self.xp += amount
        print(f"You gained {amount} XP!")
        if self.xp >= 100 * self.level:
            self.level_up()

    def pick_up_item(self, item):
        self.inventory.append(item)
        self.gain_xp(item.xp_value)
        print(f"You picked up a {item.name}!")

    def attack_mob(self, mob):
        print(f"Attacking {mob.name}!")
        mob.health -= self.attack_power
        if mob.health <= 0:
            print(f"You defeated the {mob.name}!")
            self.gain_xp(mob.xp_reward)
            return True
        else:
            return False

def get_random_mob():
    mobs = [
        Mob("Goblin", 30, 50),
        Mob("Orc", 50, 100),
        Mob("Dragon", 80, 200)
    ]
    return random.choice(mobs)

def get_random_item():
    items = [
        Item("Health Potion", 30),
        Item("Magic Scroll", 50),
        Item("Ancient Relic", 100)
    ]
    return random.choice(items)

def print_status(player):
    print(f"\nPlayer Level: {player.level}")
    print(f"XP: {player.xp}/{100 * player.level}")
    print(f"Health: {player.health}")
    print(f"Attack Power: {player.attack_power}")
    print(f"Inventory: {[item.name for item in player.inventory]}")

def main():
    player = Player()
    print("Welcome to the Adventure Game!")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Explore")
        print("2. View Status")
        print("3. Quit")

        choice = input("> ")

        if choice == "1":
            action = random.choice(["find_item", "fight_mob"])
            if action == "find_item":
                item = get_random_item()
                player.pick_up_item(item)
            elif action == "fight_mob":
                mob = get_random_mob()
                print(f"A wild {mob.name} appeared!")
                while mob.health > 0:
                    print(f"\nThe {mob.name} has {mob.health} health left.")
                    print("1. Attack")
                    print("2. Run")
                    action = input("> ")
                    if action == "1":
                        if player.attack_mob(mob):
                            break
                    elif action == "2":
                        print("You ran away safely.")
                        break
                    else:
                        print("Invalid choice.")
            else:
                print("Unexpected action.")
        
        elif choice == "2":
            print_status(player)
        
        elif choice == "3":
            print("Thanks for playing! Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
