def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class AppSettings:
    def __init__(self) -> None:
        """ O init será chamado todas as vezes """
        self.tema = 'O tema escuro'
        self.font = '18px'


@singleton
class Teste:
    def __init__(self) -> None:
        print('OI')


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'O tema claro'
    print(as1.tema)

    as2 = AppSettings()
    print(as1.tema)

    t1 = Teste()
    t2 = Teste()
    print(t1 == t2)
