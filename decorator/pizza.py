from abc import ABC, abstractmethod

class Pizza(ABC): #interface pizza
    @abstractmethod
    def preco():
        pass

class PizzaDeNona(Pizza):   #implementação Concreta da interface pizza
    def __init__(self, ingredientes) -> None:
        self.ingredientes = ingredientes
    
    def preco(self):
        valor = 0
        for v in self.ingredientes.values():
            valor+=v
        return valor

class PizzaDecorator(Pizza): #implementação do Decorator
    def __init__(self, pizza):
        self.pizzaDecorada = pizza
    
class MassaIntegral(PizzaDecorator):

    def __init__(self, pizza):
        super().__init__(pizza)
    
    def preco(self):
        return self.pizzaDecorada.preco() + 5

    
class ExtraGrande(PizzaDecorator):

    def __init__(self, pizza):
        super().__init__(pizza)
    
    def preco(self):
        return self.pizzaDecorada.preco() *1.3

    
class BordaRecheada(PizzaDecorator):

    def __init__(self, pizza):
        super().__init__(pizza)
    
    def preco(self):
        return self.pizzaDecorada.preco() + 10

    
def main():
    ingredientes= {
        "Massa" : 10,
        "Manjericão" : 5,
        "Muzzarela" : 20,
        "Tomate" : 5
    }

    pizza_basica= PizzaDeNona(ingredientes)
    pizza_mutante = ExtraGrande(BordaRecheada(MassaIntegral(pizza_basica)))
    print(pizza_mutante.preco())

main()