# from typing import Any


# class Meta(type):
#     def __call__(self, *args: Any, **kwds: Any) -> Any:
#         print('META CALL é executado')
#         return super().__call__(*args, **kwds)


# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print('NEW é executado')
#         return super().__new__(cls)

#     def __init__(self, nome) -> None:
#         print('INIT é executado')
#         self.nome = nome

#     def __call__(self, x, y, *args: Any, **kwds: Any) -> Any:
#         print('Call chamado', self.nome, x + y)


# p1 = Pessoa('Lineker')
# p1(2, 2)
"""
O Singleton tem a intenção de garantir que uma classe tenha somente
uma instância e fornece um ponto global de acesso para a mesma.

When discussing which patterns to drop, we found
that we still love them all.
(Not really—I'm in favor of dropping Singleton.
Its use is almost always a design smell.)
- Erich Gamma, em entrevista para informIT
http://www.informit.com/articles/article.aspx?p=1404056
"""
from typing import Dict


class Singleton(type):
    _instances: Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self) -> None:
        """ O init será chamado todas as vezes """
        self.tema = 'O tema escuro'
        self.font = '18px'


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'Qualquer outra coisa'

    as2 = AppSettings()
    as3 = AppSettings()
    print(as3.tema)
    print(as1 == as2)
    print(as1 == as3)
    print(as2 == as3)
