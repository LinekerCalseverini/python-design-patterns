from abc import ABC, abstractmethod


class PlayMode(ABC):
    def __init__(self, player: 'Player') -> None:
        self.player = player

    @abstractmethod
    def press_next(self) -> None: pass

    @abstractmethod
    def press_prev(self) -> None: pass


class RadioMode(PlayMode):
    def press_next(self) -> None:
        self.player.playing += 1000

    def press_prev(self) -> None:
        self.player.playing -= 1000 if self.player.playing > 0 else 0


class MusicMode(PlayMode):
    def press_next(self) -> None:
        self.player.playing += 1

    def press_prev(self) -> None:
        self.player.playing -= 1 if self.player.playing > 0 else 0


class Player:
    def __init__(self) -> None:
        self.mode: PlayMode = RadioMode(self)
        self.playing = 0

    def change_mode(self, mode: PlayMode) -> None:
        print(f'Mudando para mode: {mode.__class__.__name__}.')
        self.playing = 0
        self.mode = mode

    def press_next(self) -> None:
        self.mode.press_next()
        print(f'Now Playing: {self}')

    def press_prev(self) -> None:
        self.mode.press_prev()
        print(f'Now Playing: {self}')

    def __str__(self) -> str:
        return str(self.playing)


if __name__ == '__main__':
    player = Player()
    player.press_next()
    player.press_next()
    player.press_next()
    player.press_next()
    player.press_prev()
    player.press_prev()

    print()
    player.change_mode(MusicMode(player))
    player.press_next()
    player.press_next()
    player.press_next()
    player.press_next()
    player.press_prev()
    player.press_prev()
