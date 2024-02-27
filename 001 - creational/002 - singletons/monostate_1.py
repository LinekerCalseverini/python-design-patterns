"""
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.
"""
from abc import ABC


class StringReprMixin(ABC):
    def __str__(self) -> str:
        params = ', '.join([
            f'{k}={v}' for k, v in self.__dict__.items()
        ])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return str(self)


class MonoStateSimple(StringReprMixin):
    _state = {}

    def __init__(self, nome=None, sobrenome=None) -> None:
        self.__dict__ = self._state

        if nome is not None:
            self.nome = nome
        if sobrenome is not None:
            self.sobrenome = sobrenome


if __name__ == "__main__":
    ms1 = MonoStateSimple('Robert', 'Cruz')
    ms2 = MonoStateSimple(sobrenome='Inacio')
    print(ms1)
    print(ms2)
