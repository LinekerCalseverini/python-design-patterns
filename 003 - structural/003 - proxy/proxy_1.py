"""
O Proxy é um padrão de projeto estrutural que tem a
intenção de fornecer um objeto substituto que atua
como se fosse o objeto real que o código cliente
gostaria de usar.
O proxy receberá as solicitações e terá controle
sobre como e quando repassar tais solicitações ao
objeto real.

Com base no modo como o proxies são usados,
nós os classificamos como:

- Proxy Virtual: controla acesso a recursos que podem
ser caros para criação ou utilização.
- Proxy Remoto: controla acesso a recursos que estão
em servidores remotos.
- Proxy de proteção: controla acesso a recursos que
possam necessitar autenticação ou permissão.
- Proxy inteligente: além de controlar acesso ao
objeto real, também executa tarefas adicionais para
saber quando e como executar determinadas ações.

Proxies podem fazer várias coisas diferentes:
criar logs, autenticar usuários, distribuir serviços,
criar cache, criar e destruir objetos, adiar execuções
e muito mais...
"""
from abc import ABC, abstractmethod
from typing import List, Dict
from time import sleep


class IUser(ABC):
    ''' Abstract Subject '''
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]: pass

    @abstractmethod
    def get_all_user_data(self) -> Dict: pass


class RealUser(IUser):
    ''' Concrete Subject '''

    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2)  # Simulando requisição
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> List[Dict]:
        sleep(2)  # Simulando requisição
        return [
            {'logradouro': 'Av. Brasil', 'numero': '500'}
        ]

    def get_all_user_data(self) -> Dict:
        sleep(2)  # Simulando requisição
        return {
            'cpf': '351.677.400-29',
            'rg': '25.430.949-5'
        }


class UserProxy(IUser):
    ''' Proxy '''

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

        # Esses objetos não existem nesse ponto do código
        self._real_user: RealUser
        self._cached_addresses: List[Dict]
        self._cached_all_user_data: Dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)

    def get_addresses(self) -> List[Dict]:
        self.get_real_user()

        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()

        return self._cached_addresses

    def get_all_user_data(self) -> Dict:
        self.get_real_user()

        if not hasattr(self, '_cached_all_user_data'):
            self._cached_all_user_data = self._real_user.get_all_user_data()

        return self._cached_all_user_data


if __name__ == '__main__':
    user = UserProxy('John', 'Doe')

    # 6 segundos para processar
    print(user.get_addresses())
    print(user.get_all_user_data())

    print()

    # Instantâneo, pegou do cache
    print(user.get_addresses())
    print(user.get_all_user_data())
