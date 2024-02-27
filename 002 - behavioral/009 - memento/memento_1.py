"""
GoF - Memento é um padrão de projeto comportamental
que tem a intenção de permitir que você salve e restaure
um estado anterior de um objeto originator sem revelar os
detalhes da sua implementação e sem violar o encapsulamento.

Originator é o objeto que deseja salvar seu estado.
Memento é usado para salvar o estado do Originator.
Caretaker é usado para armazenar mementos.
Caretaker também é usado com o Padrão Command.
"""
from typing import Any, Dict, List
from copy import deepcopy


class Memento:
    def __init__(self, state: Dict) -> None:
        self._state: Dict
        super().__setattr__('_state', state)

    @property
    def state(self) -> Dict:
        return self._state

    def __setattr__(self, __name: str, __value: Any) -> None:
        raise AttributeError('Memento objects are immutable')


class ImageEditor:
    def __init__(self, name: str, width: int, height: int) -> None:
        self._name = name
        self._width = width
        self._height = height

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        self._width = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        self._height = value

    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.state

    def __str__(self) -> str:
        attributes = ', '.join([
            f'{k}={v}' for k, v in self.__dict__.items()
        ])
        return f'{self.__class__.__name__}({attributes})'


class Caretaker:
    def __init__(self, originator: ImageEditor):
        self._originator = originator
        self._mementos: List[Memento] = []

    def backup(self):
        self._mementos.append(self._originator.save_state())

    def restore(self) -> None:
        if not self._mementos:
            return

        self._originator.restore(self._mementos.pop())


if __name__ == '__main__':
    img = ImageEditor('FOTO_1.png', 111, 111)
    caretaker = Caretaker(img)

    caretaker.backup()

    img.name = 'FOTO_2.jpg'
    img.width = 222
    img.height = 222
    caretaker.backup()

    img.name = 'FOTO_3.jpg'
    img.width = 333
    img.height = 333
    caretaker.backup()

    img.name = 'FOTO_4.jpg'
    img.width = 444
    img.height = 444
    caretaker.restore()
    caretaker.restore()

    print(img)
