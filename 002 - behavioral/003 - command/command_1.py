"""
Command tem intenção de encapsular uma solicitação como
um objeto, desta forma permitindo parametrizar clientes com diferentes
solicitações, enfileirar ou fazer registro (log) de solicitações e suportar
operações que podem ser desfeitas.

É formado por um cliente (quem orquestra tudo), um invoker (que invoca as
solicitações), um ou vários objetos de comando (que fazem a ligação entre o
receiver e a ação a ser executada) e um receiver (o objeto que vai executar a
ação no final).
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Tuple


class Light:
    ''' Receiver - Luz Inteligente '''

    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'

    def on(self) -> None:
        print(f'Light {self.name} in room {self.room_name} is now ON')

    def off(self) -> None:
        print(f'Light {self.name} in room {self.room_name} is now OFF')

    def change_color(self, color: str) -> None:
        self.color = color
        print(
            f'Light {self.name} in room {self.room_name} is now {self.color}'
        )


class ICommand(ABC):
    ''' Abstract Command - Interface de Comando '''
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class LightOnCommand(ICommand):
    ''' Concrete Command - Comando que Ligará a Luz '''

    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class LightColorChangeCommand(ICommand):
    ''' Concrete Command - Comando que Trocará a cor da Luz '''

    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = color
        self._old_color = self.light.color

    def execute(self) -> None:
        self._old_color = self.light.color
        self.light.change_color(self.color)

    def undo(self) -> None:
        self.light.change_color(self._old_color)


class RemoteController:
    ''' Invoker '''

    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}
        self._undos: List[Tuple[str, str]] = []

    def button_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def button_execute(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()

    def button_undo(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()
            self._undos.append((name, 'undo'))

    def global_undo(self) -> None:
        if not self._undos:
            print('No more undos')
            return None

        button, _ = self._undos.pop()
        self._buttons[button].undo()


if __name__ == "__main__":
    bedroom_light = Light('Luz do Quarto', 'Quarto')
    bathroom_light = Light('Luz do Banheiro', 'Banheiro')

    bedroom_light_switch = LightOnCommand(bedroom_light)
    bathroom_light_switch = LightOnCommand(bathroom_light)
    bedroom_light_blue = LightColorChangeCommand(bedroom_light, 'Blue')
    bathroom_light_green = LightColorChangeCommand(bathroom_light, 'Green')

    remote_controller = RemoteController()

    remote_controller.button_add_command('Luz Quarto', bedroom_light_switch)
    remote_controller.button_add_command('Luz Banheiro', bathroom_light_switch)
    remote_controller.button_add_command('Luz Quarto Azul', bedroom_light_blue)
    remote_controller.button_add_command(
        'Luz Banheiro Verde', bathroom_light_green)

    remote_controller.button_execute('Luz Quarto')
    remote_controller.button_execute('Luz Banheiro')

    remote_controller.button_undo('Luz Quarto')
    remote_controller.button_undo('Luz Banheiro')

    remote_controller.button_execute('Luz Quarto Azul')
    remote_controller.button_execute('Luz Banheiro Verde')

    remote_controller.button_undo('Luz Quarto Azul')
    remote_controller.button_undo('Luz Banheiro Verde')

    remote_controller.button_undo('Luz Quarto Azul')
    remote_controller.button_undo('Luz Banheiro Verde')

    print()
    remote_controller.global_undo()
    remote_controller.global_undo()
    remote_controller.global_undo()
    remote_controller.global_undo()
    remote_controller.global_undo()
    remote_controller.global_undo()
