"""
Mediator é um padrão de projeto comportamental
que tem a intenção de definir um objeto que
encapsula a forma como um conjunto de objetos
interage. O Mediator promove o baixo acoplamento
ao evitar que os objetos se refiram uns aos
outros explicitamente e permite variar suas
interações independentemente.
"""
from abc import ABC, abstractmethod
from typing import List


class Colleague(ABC):
    def __init__(self, name: str, mediator: 'Mediator') -> None:
        self.name = name
        self.mediator = mediator
        self.mediator.add(self)

    @abstractmethod
    def broadcast(self, message: str) -> None: pass
    @abstractmethod
    def send_direct(self, receiver: str, message: str) -> None: pass
    @abstractmethod
    def direct(self, message: str) -> None: pass


class Mediator(ABC):
    @abstractmethod
    def add(self, person: Colleague) -> None: pass
    @abstractmethod
    def remove(self, person: Colleague) -> None: pass
    @abstractmethod
    def broadcast(self, person: Colleague, message: str) -> None: pass

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str,
               message: str) -> None: pass


class Person(Colleague):
    def broadcast(self, message: str) -> None:
        self.mediator.broadcast(self, message)

    def send_direct(self, receiver: str, message: str) -> None:
        self.mediator.direct(self, receiver, message)

    def direct(self, message: str) -> None:
        print(message)


class ChatRoom(Mediator):
    def __init__(self) -> None:
        self.colleagues: List[Colleague] = []

    def is_colleague(self, person: Colleague) -> bool:
        return person in self.colleagues

    def find_colleague(self, name: str) -> Colleague | None:
        for colleague in self.colleagues:
            if colleague.name == name:
                return colleague

        return None

    def add(self, person: Colleague) -> None:
        if not self.is_colleague(person):
            self.colleagues.append(person)

    def remove(self, person: Colleague) -> None:
        if self.is_colleague(person):
            self.colleagues.remove(person)

    def broadcast(self, person: Colleague, message: str) -> None:
        if not self.is_colleague(person):
            return

        print(f'{person.name} disse: {message}')

    def direct(self, sender: Colleague, receiver: str, message: str) -> None:
        if not self.is_colleague(sender):
            return

        colleague = self.find_colleague(receiver)
        if not colleague:
            return

        colleague.direct(
            f'{sender.name} disse para {colleague.name}: {message}'
        )


if __name__ == '__main__':
    chat_room = ChatRoom()
    john = Person('John', chat_room)
    jane = Person('Jane', chat_room)
    jane.broadcast('Hey, John!')
    john.broadcast('Hey, Jane!')

    john.send_direct('Jane', 'Hey, Jane!')
    jane.send_direct('John', 'Hey, John!')
