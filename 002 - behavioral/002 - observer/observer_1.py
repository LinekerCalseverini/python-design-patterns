"""
O padrão Observer tem a intenção de
definir uma dependência de um-para-muitos entre
objetos, de maneira que quando um objeto muda de
estado, todo os seus dependentes são notificados
e atualizados automaticamente.

Um observer é um objeto que gostaria de ser
informado, um observable (subject) é a entidade
que gera as informações.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: pass


class Smartphone(IObserver):
    def __init__(self, name, observable: IOBservable) -> None:
        self._name = name
        self._observable = observable

    def update(self) -> None:
        observable_name = self._observable.__class__.__name__
        print(f'{self._name} - {observable_name} atualizado:'
              '\n\t', self._observable.state)


class Notebook(IObserver):
    def __init__(self, observable: IOBservable) -> None:
        self._observable = observable

    def show(self) -> None:
        state = self._observable.state
        print('Sou o notebook e vou mostrar esses dados:', state)

    def update(self) -> None:
        self.show()


class IOBservable(ABC):
    ''' Observable '''

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def notify_observers(self) -> None: pass

    @property
    @abstractmethod
    def state(self) -> Dict: pass


class WeatherStation(IOBservable):
    ''' Observable '''

    def __init__(self) -> None:
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self) -> Dict:
        return self._state

    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self) -> None:
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()


if __name__ == "__main__":
    weather_station = WeatherStation()

    smartphone_1 = Smartphone('Smartphone 1', weather_station)
    smartphone_2 = Smartphone('Smartphone 2', weather_station)
    notebook = Notebook(weather_station)

    weather_station.add_observer(smartphone_1)
    weather_station.add_observer(smartphone_2)
    weather_station.add_observer(notebook)

    weather_station.state = {'temperature': 30}
    weather_station.state = {'temperature': 40}
    weather_station.state = {'humidity': 90}

    weather_station.remove_observer(smartphone_2)
    weather_station.state = {'temperature': 50}
    weather_station.reset_state()
