class Animal:
    alive: list["Animal"] = []

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.health: int = 100
        self.hidden: bool = False
        Animal.alive.append(self)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, Hidden: {self.hidden}}}"
        )

    @classmethod
    def __str__(cls) -> str:
        return str(cls.alive)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if other.health <= 0:
                other.die()
# Health: 100, Hidden: False}, {Name: Kaa, Health: 100,
# Hidden: False}]lse},
# {Name: Lion King, Health: 100, Hidden: False}, {Name: Bagira,
# Health: 100, Hidden: False},
# {Name: Kaa, Health: 100, Hidden: False}]
