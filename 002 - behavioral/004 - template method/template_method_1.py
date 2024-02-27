"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""
from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation1()
        self.base_operation()
        self.operation2()

    def hook(self): pass

    def base_operation(self):
        print("Operação base concluída.")

    @abstractmethod
    def operation1(self): pass

    @abstractmethod
    def operation2(self): pass


class ConcreteClass1(Abstract):
    def hook(self):
        print('Apenas a Classe 1 implementa o Hook.')

    def operation1(self):
        print("Operação 1 concluída.")

    def operation2(self):
        print("Operação 2 concluída.")


class ConcreteClass2(Abstract):
    def operation1(self):
        print("Operação 1 finalizada.")

    def operation2(self):
        print("Operação 2 finalizada.")


if __name__ == "__main__":
    c1 = ConcreteClass1()
    c1.template_method()

    c2 = ConcreteClass2()
    c2.template_method()
