"""
Chain of responsibility (COR) é um padrão comportamental
que tem a intenção de evitar o acoplamento do remetente de
uma solicitação ao seu receptor, ao dar a mais de um objeto
a oportunidade de tratar a solicitação.
Encadear os objetos receptores passando a solicitação
ao longo da cadeia até que um objeto a trate.
"""

# Implementando com funções


def handler_ABC(letter: str) -> str:
    letters = 'ABC'

    if letter.upper() in letters:
        return f'{letter} was handled by {handler_ABC.__name__}'

    return handler_DEF(letter)


def handler_DEF(letter: str) -> str:
    letters = 'DEF'

    if letter.upper() in letters:
        return f'{letter} was handled by {handler_DEF.__name__}'

    return handler_unsolved(letter)


def handler_unsolved(letter: str) -> str:
    return f'{letter} could not be handled. {handler_unsolved.__name__}'


if __name__ == '__main__':
    for letter in 'ABCDEFG':
        print(handler_ABC(letter))
