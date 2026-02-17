from abc import ABC, abstractmethod

class Character(ABC):
    
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Remaining health: {self.health}")
    
    @abstractmethod
    def attack(self, opponent):
        pass
class Warrior(Character):
    
    def attack(self, opponent):
        damage = self.power * 2
        print(f"{self.name} performs a heavy sword attack!")
        opponent.take_damage(damage)
class Mage(Character):
    
    def attack(self, opponent):
        damage = self.power + 10
        print(f"{self.name} casts a fireball!")
        opponent.take_damage(damage)
class Archer(Character):
    
    def attack(self, opponent):
        damage = self.power
        print(f"{self.name} shoots an arrow!")
        opponent.take_damage(damage)
warrior = Warrior("Thor", 100, 20)
mage = Mage("Merlin", 80, 15)
archer = Archer("Robin", 90, 18)
warrior.attack(mage)
mage.attack(warrior)
archer.attack(warrior)
