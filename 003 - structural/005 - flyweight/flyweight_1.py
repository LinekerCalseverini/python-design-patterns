"""
Flyweight é um padrão de projeto estrutural
que tem a intenção de usar compartilhamento
para suportar eficientemente grandes quantidades
de objetos de forma granular.

Só use o Flyweight quanto TODAS as condições
a seguir forem verdadeiras:

- uma aplicação utiliza uma grande quantidade de
objetos;
- os custos de armazenamento são altos por causa
da grande quantidade de objetos;
- a maioria dos estados de objetos podem se tornar
extrínsecos;
- muitos objetos podem ser substituídos por poucos
objetos compartilhados;
- a aplicação não depende da identidade dos objetos.

Importante:
- Estado intrínseco é o estado do objeto que não muda,
esse estado deve estar dentro do objeto flyweight;
- Estado extrínseco é o estado do objeto que muda,
esse estado pode ser movido para fora do objeto
flyweight;

Dicionário:
Intrínseco - que faz parte de ou que constitui a
essência, a natureza de algo; que é próprio de
algo; inerente.
Extrínseco - que não pertence à essência de algo;
que é exterior.
"""
from typing import List, Dict


class Address:
    def __init__(self, street: str, neighborhood: str, zip_code: str) -> None:
        self._street = street
        self._neighborhood = neighborhood
        self._zip_code = zip_code

    def show_address(self, address_number: str, address_details: str) -> None:
        print((f'{address_number} - {self._street}, {address_details}, '
               f'{self._neighborhood} - {self._zip_code}'))


class Client:
    ''' Context '''

    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List[Address] = []

        # Extrinsic address data
        self._address_number: str
        self._address_details: str

    def add_address(self, address: Address) -> None:
        self._addresses.append(address)

    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(
                self._address_number, self._address_details
            )

    @property
    def address_number(self):
        return self._address_number

    @address_number.setter
    def address_number(self, address_number: str):
        self._address_number = address_number

    @property
    def address_details(self):
        return self._address_details

    @address_details.setter
    def address_details(self, address_details: str):
        self._address_details = address_details


class AddressFactory:
    _addresses: Dict = {}
    _address_Number: int = 0

    def _get_key(self, **kwargs):
        return ''.join(kwargs.values())

    def get_address(self, **kwargs):
        key = self._get_key(**kwargs)
        if key not in self._addresses:
            self._addresses[key] = Address(**kwargs)
        return self._addresses[key]


if __name__ == '__main__':
    address_factory = AddressFactory()
    address_1 = address_factory.get_address(
        street='Av. Paulista',
        neighborhood='Bela Vista',
        zip_code='01310-000'
    )
    address_2 = address_factory.get_address(
        street='Av. Paulista',
        neighborhood='Bela Vista',
        zip_code='01310-000'
    )

    luiz = Client('Luiz')
    luiz.address_number = '50'
    luiz.address_details = 'Casa'
    luiz.add_address(address_1)
    luiz.add_address(address_2)
    luiz.list_addresses()

    joana = Client('Joana')
    joana.address_number = '250A'
    joana.address_details = 'AP 01'
    joana.add_address(address_1)
    joana.add_address(address_2)
    joana.list_addresses()
