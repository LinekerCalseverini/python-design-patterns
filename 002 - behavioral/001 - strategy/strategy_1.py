"""
Strategy é um padrão de projeto comportamental que tem
a intenção de definir uma família de algoritmos,
encapsular cada uma delas e torná-las intercambiáveis.
Strategy permite que o algorítmo varie independentemente
dos clientes que o utilizam.

Princípio do aberto/fechado (Open/closed principle)
Entidades devem ser abertas para extensão, mas fechadas para modificação
"""
from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, total: float) -> float: pass


class TwentyPercent(DiscountStrategy):
    def calculate(self, total: float) -> float:
        return total * 0.8


class FiftyPercent(DiscountStrategy):
    def calculate(self, total: float) -> float:
        return total * 0.5


class NoDiscount(DiscountStrategy):
    def calculate(self, total: float) -> float:
        return total


class CustomDiscount(DiscountStrategy):
    def __init__(self, discount: float) -> None:
        self._discount = discount / 100

    def calculate(self, total: float) -> float:
        return total * (1 - self._discount)


class Order:
    def __init__(self, total: float, discount: DiscountStrategy) -> None:
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self._total)


if __name__ == "__main__":
    twenty_percent = TwentyPercent()
    fifty_percent = FiftyPercent()
    no_discount = NoDiscount()
    five_percent = CustomDiscount(5)

    order = Order(1000, twenty_percent)
    order2 = Order(1000, fifty_percent)
    order3 = Order(1000, no_discount)
    order4 = Order(1000, five_percent)

    print(order.total)
    print(order.total_with_discount)

    print(order2.total)
    print(order2.total_with_discount)

    print(order3.total)
    print(order3.total_with_discount)

    print(order4.total)
    print(order4.total_with_discount)
