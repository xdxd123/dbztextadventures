import random
import pickle

# ---------- Player and Enemy Classes ----------

class Character:
    def __init__(self, power_level):
        self.power_level = power_level
        self.update_stats()

    def update_stats(self):
        self.strength = self.power_level * 0.1
        self.health = self.power_level * 0.05
        self.agility = self.power_level * 0.15
        self.durability = self.power_level * 0.075

class Enemy:
    def __init__(self, name, strength, durability, health, agility):
        self.name = name
        self.strength = strength
        self.durability = durability
        self.health = health
        self.agility = agility
        self.defeated = False

# ---------- Save/Load Functions ----------

def save_game(filename, player, enemies):
    with open(filename, 'wb') as file:
        pickle.dump((player.power_level, [e.defeated for e in enemies]), file)

def load_game(filename, player, enemies):
    with open(filename, 'rb') as file:
        pl, defeated_flags = pickle.load(file)
        player.power_level = pl
        player.update_stats()
        for i, defeated in enumerate(defeated_flags):
            enemies[i].defeated = defeated

# ---------- Game Setup ----------

player = Character(5)

enemies = [
    Enemy("Goku Raditz Saga", strength=25, durability=10, health=15, agility=10),
    Enemy("Raditz", strength=120, durability=90, health=60, agility=180),
    Enemy("Nappa", strength=185, durability=200, health=225, agility=150),
    Enemy("Vegeta", strength=1800, durability=1350, health=900, agility=2700),
]

# ---------- Main Game Loop ----------

race = input("Choose your race: human, saiyan, majin, frieza, namekian, demon: ").lower()

while race == "human" and player.power_level <= 500:
    print("\nA. Train with martial artists\nB. Lift weights\nC-Z. Fight enemies")
    print("Type 'save' or 'load' to manage your game.")
    choice = input("Your choice: ").upper()

    if choice == 'A':
        player.power_level += random.randint(1, 25)
    elif choice == 'B':
        player.power_level += random.randint(1, 15)
    elif choice == 'SAVE':
        save_game('savegame.txt', player, enemies)
        print("Game saved.")
        continue
    elif choice == 'LOAD':
        load_game('savegame.txt', player, enemies)
        print("Game loaded.")
        continue
    elif choice in ['C', 'D', 'E', 'F']:
        enemy_index = ord(choice) - ord('C')
        if enemy_index < len(enemies):
            enemy = enemies[enemy_index]
            if enemy.defeated:
                print(f"You have already defeated {enemy.name}.")
            elif (player.strength >= enemy.durability and
                  player.agility >= enemy.agility and
                  player.health >= enemy.strength):
                print(f"You are fighting {enemy.name}... You win!")
                enemy.defeated = True
                player.power_level += (enemy_index + 1) * 200
            else:
                print(f"You are fighting {enemy.name}... You have died.")
                break
    else:
        print("Invalid option.")

    player.update_stats()
    print(f"Power Level: {player.power_level:.2f}, Str: {player.strength:.2f}, HP: {player.health:.2f}, Agi: {player.agility:.2f}, Dur: {player.durability:.2f}")
