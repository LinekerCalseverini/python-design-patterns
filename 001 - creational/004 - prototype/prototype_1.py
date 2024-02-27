"""
Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo
"""
from __future__ import annotations
from typing import List
from abc import ABC


class StringReprMixin(ABC):
    def __str__(self) -> str:
        params = ', '.join([
            f'{k}={v}' for k, v in self.__dict__.items()
        ])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return str(self)


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number
    
    def clone(self) -> Address:
        return Address(self.street, self.number)


class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List[Address] = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def clone(self) -> Person:
        new_person = Person(self.firstname, self.lastname)
        for address in self.addresses:
            new_person.add_address(address.clone())

        return new_person


if __name__ == "__main__":
    luiz = Person('Luiz', 'Miranda')
    endereco_luiz = Address('Av. Brasil', '250')
    luiz.add_address(endereco_luiz)

    esposa_luiz = luiz.clone()
    esposa_luiz.firstname = 'Letícia'

    print(luiz)
    print(esposa_luiz)
