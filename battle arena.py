import random

class Character:
    def __init__(self, name, health, attack_power, defense, speed):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed
    
    def attack(self, target):
        damage = max(1, self.attack_power - target.defense)
        print(f"{self.name} attacks {target.name}! Deals {damage} damage.")
        target.take_damage(damage)
    
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Remaining health: {self.health}")
    
    def is_alive(self):
        return self.health > 0
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20, defense=10, speed=5)
        self.rage = 0
    
    def attack(self, target):
        if self.health < 36:  
            print(f"{self.name} enters Berserk Mode! Attack power doubled!")
            damage = max(1, (self.attack_power * 2) - target.defense)
        else:
            damage = max(1, self.attack_power - target.defense)
        
        print(f" {self.name} swings a sword! Deals {damage} damage.")
        target.take_damage(damage)

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=30, defense=5, speed=7)
        self.mana = 50
    
    def fireball(self, target):
        if self.mana >= 10:
            self.mana -= 10
            damage = max(1, (self.attack_power + 10) - target.defense)
            print(f" {self.name} casts Fireball! Deals {damage} damage but loses 5 health.")
            target.take_damage(damage)
            self.take_damage(5)
        else:
            print(f"{self.name} has no mana left! Regular attack instead.")
            self.attack(target)

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=22, defense=8, speed=10)
        self.critical_chance = 30
    def attack(self, target):
        if random.randint(1, 100) <= self.critical_chance:
            damage = max(1, (self.attack_power * 2) - target.defense)
            print(f" {self.name} lands a Critical Hit! Deals {damage} damage.")
        else:
            damage = max(1, self.attack_power - target.defense)
            print(f" {self.name} shoots an arrow! Deals {damage} damage.")
        target.take_damage(damage)

def battle(character1, character2):
    print("\nBattle Begins!\n")
    while character1.is_alive() and character2.is_alive():
        if character1.speed >= character2.speed:
            character1.attack(character2)
            if character2.is_alive():
                character2.attack(character1)
        else:
            character2.attack(character1)
            if character1.is_alive():
                character1.attack(character2)
               
        print("\n--- Next Turn ---\n")
    
    if character1.is_alive():
        print(f" {character1.name} wins the battle!")
    else:
        print(f" {character2.name} wins the battle!")

# Example Battle
warrior = Warrior("Thor")
mage = Mage("Gandalf")
archer = Archer("Alex")
battle(archer, warrior)
