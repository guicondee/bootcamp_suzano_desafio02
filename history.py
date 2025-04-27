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
    
class Person(Client):
    def __init__(self, name, date_of_birth, cpf, address):
        super().__init__(address)
        self.name = name
        self.date_of_birth = date_of_birth
        self.cpf = cpf

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
class Account:
    def __init__(self, number, client):
        self._balance = 0
        self._number = number
        self._agency = "0001"
        self._client = client
        self._history = History()

       
    @classmethod
    def new_account(cls, number, client):
        return cls(number, client)
    
    @property
    def balance(self):
        return self._balance
    
    @property
    def number(self):
        return self._number
    
    
    @property
    def agency(self):
        return self._agency
    
    
    @property
    def client(self):
        return self._client
    
    @property
    def history(self):
        return self._history
    
    def withdraw(self, value):
        balance = self._balance
        exceeded_balance = value > balance

        if exceeded_balance:
            print("\n@@@ Operação falhou! Você não tem s aldo suficiente, @@@")

        elif value > 0:
            self._balance -= value
            print("\n=== Saque realizado com sucesso! ===")
            return True
        
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False
        
    
    def deposit(self, value):
        if value > 0:
            self._balance += value
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False
        
        return True