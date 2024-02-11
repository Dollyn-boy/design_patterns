import random
import string
from abc import ABC, abstractmethod

class Authorizer(ABC):
    @abstractmethod
    def authorize(self):
        pass
    
    @abstractmethod
    def is_authorized(self) -> bool:
        pass

class Order:

    def __init__(self) -> None:
        self.id = "".join(random.choices(string.ascii_lowercase, k=6))
        self.status= "open"

    def set_status(self, status):
        self.status = status

class Authorizer_SMS(Authorizer):

    def __init__ (self):
        self.authorized = False
        self.code = None

    def generate_sms_code(self):
        self.code = "".join(random.choices(string.ascii_lowercase, k=6))
    
    def authorize(self):
        code = input("Enter SMS Code: ")
        self.authorize = code == self.code
    
    def is_authorized(self) -> bool:
        return self.authorize
    

class PaymentProcessor:
    def __init__(self, authorizer: Authorizer):
        self.authorizer = authorizer #Injecção de dependência por Construção
        
    def pay(self, order):
        #authorizer = Authorizer_SMS(), instanciação de um objeto dentro de uma função como essa n é uma boa ideia
        self.authorizer.authorize()
        if not self.authorizer.is_authorized():
            raise Exception("Not Authorized")
        print(f"Processing payment for order {order.id}")
        order.set_status("paid")
