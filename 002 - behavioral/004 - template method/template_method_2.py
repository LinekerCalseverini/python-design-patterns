from abc import ABC, abstractmethod


class Pizza(ABC):
    ''' Classe Abstrata '''

    def prepare(self) -> None:
        ''' Template Method '''
        self.hook_before_ingredients()
        self.add_ingredients()  # Abstract
        self.hook_after_ingredients()
        self.cook()  # Abstract
        self.cut()  # Concrete
        self.serve()  # Concrete

    def hook_before_ingredients(self) -> None: pass

    def hook_after_ingredients(self) -> None: pass

    def cut(self) -> None:
        print(f'{self.__class__.__name__}: cortando em 8 pedaços.')

    def serve(self) -> None:
        print(f'{self.__class__.__name__}: servindo a pizza.')

    @abstractmethod
    def add_ingredients(self) -> None: pass

    @abstractmethod
    def cook(self) -> None: pass


class HouseSpecial(Pizza):
    ''' Subclasse Concreta '''

    def add_ingredients(self) -> None:
        print(f'{self.__class__.__name__}: colocando ingredientes da casa.')

    def cook(self) -> None:
        print(f'{self.__class__.__name__}: cozinhando a pizza na grelha.')

    def serve(self) -> None:
        print(f'{self.__class__.__name__}: servindo a pizza na grelha.')


class Veggie(Pizza):
    ''' Subclasse Concreta '''
    def hook_before_ingredients(self) -> None:
        print(f'{self.__class__.__name__}: lavando ingredientes.')

    def add_ingredients(self) -> None:
        print(f'{self.__class__.__name__}: colocando ingredientes veganos.')

    def cook(self) -> None:
        print(f'{self.__class__.__name__}: cozinhando a pizza no forno.')


if __name__ == '__main__':
    pizza = HouseSpecial()
    pizza.prepare()

    veggie_pizza = Veggie()
    veggie_pizza.prepare()
