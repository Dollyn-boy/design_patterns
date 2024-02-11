from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def preco(self):
        pass

class PizzaDeNona(Pizza):
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes
    
    def preco(self):
        valor = 0
        for v in self.ingredientes.values():
            valor += v
        return valor

class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self.pizzaDecorada = pizza

    def preco(self):
        return self.pizzaDecorada.preco()

class MassaIntegral(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
    
    def preco(self):
        return self.pizzaDecorada.preco() + 5

class ExtraGrande(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
    
    def preco(self):
        return self.pizzaDecorada.preco() * 1.3

class BordaRecheada(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
    
    def preco(self):
        return self.pizzaDecorada.preco() + 10

def main():
    ingredientes = {
        "Massa": 10,
        "Manjericão": 5,
        "Muzzarela": 20,
        "Tomate": 5
    }

    pizza_basica = PizzaDeNona(ingredientes)
    pizza_mutante = ExtraGrande(BordaRecheada(MassaIntegral(pizza_basica)))
    print(str(pizza_mutante.preco()))

main()