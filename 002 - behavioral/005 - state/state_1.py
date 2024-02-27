"""
O Padrão de projeto State é um padrão comportamental
que tem a intenção de permitir a um objeto mudar
seu comportamento quando o seu estado interno
muda.
O objeto parecerá ter mudado sua classe.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class OrderState(ABC):
    def __init__(self, order: 'Order') -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None: pass
    @abstractmethod
    def approve(self) -> None: pass
    @abstractmethod
    def reject(self) -> None: pass


class PaymentPending(OrderState):
    def pending(self) -> None:
        print('Pagamento já está pendente, nenhuma alteração feita.')

    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print('Pagamento aprovado.')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Pagamento recusado.')


class PaymentApproved(OrderState):
    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print('Pagamento pendente.')

    def approve(self) -> None:
        print('Pagamento já foi aprovado, nenhuma alteração feita.')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Pagamento recusado.')


class PaymentRejected(OrderState):
    def pending(self) -> None:
        print('Pagamento recusado, nenhuma ação pode ser feita.')

    def approve(self) -> None:
        print('Pagamento recusado, nenhuma ação pode ser feita.')

    def reject(self) -> None:
        print('Pagamento recusado, nenhuma ação pode ser feita.')


class Order:
    ''' Context '''

    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        print(f'Tentando executar {self.__class__.__name__}().pending().')
        self.state.pending()
        print(f'Estado atual: {self.state.__class__.__name__}.')
        print()

    def approve(self) -> None:
        print(f'Tentando executar {self.__class__.__name__}().approve().')
        self.state.approve()
        print(f'Estado atual: {self.state.__class__.__name__}.')
        print()

    def reject(self) -> None:
        print(f'Tentando executar {self.__class__.__name__}().reject().')
        self.state.reject()
        print(f'Estado atual: {self.state.__class__.__name__}.')
        print()


if __name__ == '__main__':
    order = Order()
    order.pending()
    order.approve()
    order.pending()
    order.reject()
    order.pending()
    order.approve()
