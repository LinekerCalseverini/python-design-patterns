"""
Adapter é um padrão de projeto estrutural que
tem a intenção de permitir que duas classes
que seriam incompatíveis trabalhem em conjunto
através de um "adaptador".
"""
from abc import ABC, abstractmethod


class ControllerMixIn(ABC):
    @abstractmethod
    def up(self) -> None: pass
    @abstractmethod
    def down(self) -> None: pass
    @abstractmethod
    def left(self) -> None: pass
    @abstractmethod
    def right(self) -> None: pass


class Controller(ControllerMixIn):
    def up(self) -> None:
        print(f'{self.__class__.__name__}: up')

    def down(self) -> None:
        print(f'{self.__class__.__name__}: down')

    def left(self) -> None:
        print(f'{self.__class__.__name__}: left')

    def right(self) -> None:
        print(f'{self.__class__.__name__}: right')


class XController:
    def move_up(self) -> None:
        print(f'{self.__class__.__name__}: move up')

    def move_down(self) -> None:
        print(f'{self.__class__.__name__}: move down')

    def move_left(self) -> None:
        print(f'{self.__class__.__name__}: move left')

    def move_right(self) -> None:
        print(f'{self.__class__.__name__}: move right')


class ControlAdapter(ControllerMixIn):
    ''' Wrapper Adapter '''

    def __init__(self, x_controller: XController) -> None:
        self._x_controller = x_controller

    def up(self) -> None:
        self._x_controller.move_up()

    def down(self) -> None:
        self._x_controller.move_down()

    def left(self) -> None:
        self._x_controller.move_left()

    def right(self) -> None:
        self._x_controller.move_right()


class ControlAdapter2(XController, ControllerMixIn):
    ''' Inheritance Adapter '''

    def up(self) -> None:
        self.move_up()

    def down(self) -> None:
        self.move_down()

    def left(self) -> None:
        self.move_left()

    def right(self) -> None:
        self.move_right()


if __name__ == '__main__':
    # Original Controller
    c1 = Controller()
    c1.up()
    c1.down()
    c1.left()
    c1.right()

    # Wrapper Adapter
    print()
    c2 = ControlAdapter(XController())
    c2.up()
    c2.down()
    c2.left()
    c2.right()

    # Inheritance Adapter
    print()
    c3 = ControlAdapter2()
    c3.up()
    c3.down()
    c3.left()
    c3.right()
