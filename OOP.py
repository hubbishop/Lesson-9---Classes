__author__ = 'cook'


class Weapon:

    def __init__(self, name, capacity, energy_to_use, ammo):
        self.name = name
        self.cap = capacity
        self.energy_to_use = energy_to_use
        self.ammo = ammo

    def __str__(self):
        return self.name + " which has " + str(self.ammo) + " ammo out of " + str(self.cap)

    def use_weapon(self):
        if self.ammo > 0:
            self.ammo -= 1
            return self.ammo
        else:
            return None

    def replenish_ammo(self, rounds):
        self.ammo = max(self.cap, self.ammo + rounds)


class Hero:

    def __init__(self, name, warrior_class, weapon, energy, shield_strength):
        self. name = name
        self.warrior_class = warrior_class
        self.weapon = weapon
        self.energy = energy
        self.shield = shield_strength

    def __str__(self):
        return "I am the mighty " + self.name + " hero class " + self.warrior_class + \
               ", I wield the " + str(self.weapon) + " and have " + str(self.energy)\
               + " energy " +\
               " and " + str(self.shield) + " shields."

    def use_weapon(self):
        if self.weapon.use_weapon() is not None:
            self.energy -= self.weapon.energy_to_use
        else:
            return None


kimber = Weapon("Kimber 1911", 7, 1, 7)
JimBob = Hero("Jim Bob", "redneck", kimber, 10, 10)

print(JimBob)
JimBob.use_weapon()
print(JimBob)
