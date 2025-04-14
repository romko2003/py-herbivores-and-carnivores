class Animal:
    alive = []

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def die(self):
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    @classmethod
    def __str__(cls):
        return str(cls.alive)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other):
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if other.health <= 0:
                other.die()


# Тестування
if __name__ == "__main__":
    lion = Carnivore("Simba")
    print(len(Animal.alive))  # 1
    print(isinstance(Animal.alive[0], Carnivore))  # True

    rabbit = Herbivore("Susan")
    rabbit.hide()
    print(rabbit.hidden)  # True

    lion = Carnivore("Lion King")
    rabbit = Herbivore("Susan")

    print(rabbit.health)  # 100
    lion.bite(rabbit)
    print(rabbit.health)  # 50

    rabbit.hide()
    lion.bite(rabbit)
    print(rabbit.health)  # 50

    rabbit.hide()
    lion.bite(rabbit)
    print(rabbit.health)  # 0
    print(rabbit in Animal.alive)  # False

    pantera = Carnivore("Bagira")
    snake = Carnivore("Kaa")
    print(Animal.alive)
    # [{Name: Bagira, Health: 100, Hidden: False}, {Name: Kaa, Health: 100, Hidden: False}]
# ealth: 100, Hidden: False}, {Name: Lion King, Health: 100, Hidden: False}, {Name: Bagira, Health: 100, Hidden: False}, {Name: Kaa, Health: 100, Hidden: False}]lse}, {Name: Lion King, Health: 100, Hidden: False}, {Name: Bagira, Health: 100, Hidden: False}, {Name: Kaa, Health: 100, Hidden: False}]