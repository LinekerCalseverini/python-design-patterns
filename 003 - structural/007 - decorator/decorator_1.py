"""
Decorator é um padrão de projeto estrutural que permite que você
adicione novos comportamentos em objetos ao colocá-los dentro de
um "wrapper" (decorador) de objetos.
Decoradores fornecem uma alternativa flexível ao uso de subclasses
para a extensão de funcionalidades.

Decorator (padrão de projeto) != Decorator em Python

Python decorator -> Um decorator é um callable que aceita outra
função como argumento (a função decorada). O decorator pode
realizar algum processamento com a função decorada e devolvê-la
ou substituí-la por outra função ou objeto invocável.
Do livro "Python Fluente", por Luciano Ramalho (pág. 223)
"""
# from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
from typing import List
from copy import deepcopy


# INGREDIENTS
@dataclass
class Ingredient:
    price: float


@dataclass
class Bread(Ingredient):
    price: float = 1.50


@dataclass
class Sausage(Ingredient):
    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    price: float = 7.99


@dataclass
class Egg(Ingredient):
    price: float = 1.50


@dataclass
class Cheese(Ingredient):
    price: float = 6.35


@dataclass
class MashedPotatoes(Ingredient):
    price: float = 2.25


@dataclass
class PotatoSticks(Ingredient):
    price: float = 0.99


# Hotdogs
class Hotdog:
    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        string = f'{self.name}:\n'
        string += '\n'.join([
            f'\t{ingredient.__class__.__name__} -> {ingredient.price}'
            for ingredient in self.ingredients
        ])
        string += f'\n\tTotal: {self.price}'
        return string


class SimpleHotdog(Hotdog):
    def __init__(self) -> None:
        self._name = 'SimpleHotdog'
        self._ingredients = [
            Bread(),
            Sausage(),
            PotatoSticks()
        ]


class SpecialHotdog(Hotdog):
    def __init__(self) -> None:
        self._name = 'SpecialHotdog'
        self._ingredients = [
            Bread(),
            Sausage(),
            Bacon(),
            Egg(),
            Cheese(),
            MashedPotatoes(),
            PotatoSticks()
        ]


class HotdogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog) -> None:
        self._hotdog = hotdog

    @property
    def price(self) -> float:
        return self._hotdog.price

    @property
    def name(self) -> str:
        return self._hotdog.name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._hotdog.ingredients


class BaconDecorator(HotdogDecorator):
    def __init__(self, hotdog: Hotdog) -> None:
        super().__init__(hotdog)
        self._ingredient = Bacon()
        self._ingredients = deepcopy(self._hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return f'{self._hotdog.name} + {self._ingredient.__class__.__name__}'

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        string = f'{self.name}:\n'
        string += '\n'.join([
            f'\t{ingredient.__class__.__name__} -> {ingredient.price}'
            for ingredient in self.ingredients
        ])
        string += f'\n\tTotal: {self.price}'
        return string


if __name__ == '__main__':
    simple = SimpleHotdog()
    print(simple)

    bacon_simple = BaconDecorator(simple)
    print(bacon_simple)

    special = SpecialHotdog()
    print(special)
