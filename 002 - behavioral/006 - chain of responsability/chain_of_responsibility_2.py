from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def handle(self, letter: str) -> str: pass


class HandlerABC(Handler):
    def __init__(self, successor: Handler) -> None:
        self.successor = successor
        self.letters = 'ABC'

    def handle(self, letter) -> str:
        if letter.upper() in self.letters:
            return f'{letter} was handled by {self.__class__.__name__}'

        return self.successor.handle(letter)


class HandlerDEF(Handler):
    def __init__(self, successor: Handler) -> None:
        self.successor = successor
        self.letters = 'DEF'

    def handle(self, letter) -> str:
        if letter.upper() in self.letters:
            return f'{letter} was handled by {self.__class__.__name__}'

        return self.successor.handle(letter)


class HandlerUnsolved(Handler):
    def handle(self, letter) -> str:
        return f'{letter} could not be handled. {self.__class__.__name__}'


if __name__ == '__main__':
    handler_unsolved = HandlerUnsolved()
    handler_def = HandlerDEF(handler_unsolved)
    handler_abc = HandlerABC(handler_def)
    for letter in 'ABCDEFG':
        print(handler_abc.handle(letter))
