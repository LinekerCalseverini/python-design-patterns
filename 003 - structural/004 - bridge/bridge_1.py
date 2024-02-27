"""
Bridge é um padrão de projeto estrutural que
tem a intenção de desacoplar uma abstração
da sua implementação, de modo que as duas
possam variar e evoluir independentemente.

Abstração é uma camada de alto nível para algo.
Geralmente, a abstração não faz nenhum trabalho
por conta própria, ela delega parte ou todo o
trabalho para a camada de implementação.

RELEMBRANDO: Adapter é um padrão de projeto
estrutural que tem a intenção de permitir
que duas classes que seriam incompatíveis
trabalhem em conjunto através de um "adaptador".

Diferença (GOF pag. 208) - A diferença chave
entre esses padrões está nas suas intenções...
...O padrão Adapter faz as coisas funcionarem
APÓS elas terem sido projetadas; o Bridge as
faz funcionar ANTES QUE existam...
"""
from abc import ABC, abstractmethod


class IRemoteControl(ABC):
    @abstractmethod
    def increase_volume(self) -> None: pass
    @abstractmethod
    def decrease_volume(self) -> None: pass
    @abstractmethod
    def power(self) -> None: pass


class IDevice:
    def __init__(self) -> None:
        self._name = self.__class__.__name__

    def __str__(self) -> str:
        attributes = ','.join([
            f'{k}={v}' for k, v in self.__dict__.items()
        ])

        return f'{self.__class__.__name__}({attributes})'

    @property
    @abstractmethod
    def volume(self) -> int: pass

    @volume.setter
    def volume(self, value: int) -> None: pass

    @property
    @abstractmethod
    def power(self) -> bool: pass
    @power.setter
    def power(self, value: bool) -> None: pass


class RemoteControl(IRemoteControl):
    def __init__(self, device: IDevice) -> None:
        self._device = device

    def increase_volume(self) -> None:
        self._device.volume += 10

    def decrease_volume(self) -> None:
        self._device.volume -= 10

    def power(self) -> None:
        self._device.power = not self._device.power


class RemoteControlWithMute(RemoteControl):
    def mute(self) -> None:
        self._device.volume = 0


class TV(IDevice):
    def __init__(self) -> None:
        super().__init__()
        self._power = False
        self._volume = 10

    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, value: int) -> None:
        if not self.power:
            print(f'Please turn on the {self._name} first.')
            return

        if value > 100 or value < 0:
            return

        self._volume = value
        print('Volume set to', self._volume)

    @property
    def power(self) -> bool:
        return self._power

    @power.setter
    def power(self, value: bool) -> None:
        self._power = value
        status = 'ON' if self._power else 'OFF'
        print(f'{self._name} turned {status}')


class Radio(TV):
    ...


if __name__ == '__main__':
    tv = TV()

    remote = RemoteControl(tv)
    remote.power()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.power()
    remote.increase_volume()
    remote.power()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()

    print()
    radio = Radio()

    remote = RemoteControlWithMute(radio)
    remote.power()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.power()
    remote.increase_volume()
    remote.power()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()

    print('MUTE')
    remote.mute()
