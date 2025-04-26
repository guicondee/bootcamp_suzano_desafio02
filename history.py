from datetime import datetime
from abc import ABC, abstractclassmethod, abstractproperty
import textwrap

class IteratorAccounts:
    def __init__(self, accounts):
        self.accounts = accounts
        self._index = 0
        

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            account = self.accounts[self._index]
            return f"""\
            Agency:\t{account.agency}
            Number:\t\t{account.number}
            Holder:\t{account.name}
            Balance:\t\tR$ {account.balance:.2f}
        """

        except IndexError:
            raise StopIteration
        finally:
            self._index += 1

class Client:
    def __init__(self, address):
        self.address = address
        self.accounts = []
        self.index_account = 0

    def start_transaction(self, account, transaction):
        # TODO: Validar o número de transações e invalidar a operação se for necessário.
        # print("\n@@@ Você excedeu o número de transações permitidadas para hoje! @@@")
        transaction.register(account)

    def add_account(self, account):
        self.accounts.append(account)
    
class History:
    def __init__(self):
        self._trasactions = []
    
    @property
    def transactions(self):
        return self._trasactions
    
    def add_trasaction(self, transaction):
        self._trasactions.append(
            {
                "type": transaction._class_._name_,
                "value": transaction.value,
                "date": datetime.now().strftime("%d-%m%Y %H:%M:%S" ),
            }
        )

    def generate_report(self, type_transaction=None):
        for transaction in self._trasactions:
            if type_transaction is None or transaction["type"].lower() == type_transaction.lower():
                yield transaction
    
    # TODO: filtrar todas as transações realizadas no dia
    def current_transaction_of_the_day(self):
        pass