class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura


class Quadrado:
    def __init__(self, lado):
        self.retangulo = Retangulo(lado, lado)

    def definir_lado(self, lado):
        self.retangulo.largura = lado
        self.retangulo.altura = lado

    def calcular_area(self):
        return self.retangulo.calcular_area()


# Exemplo de uso
retangulo = Retangulo(4, 5)
print(f"Área do retângulo: {retangulo.calcular_area()}")

quadrado = Quadrado(4)
print(f"Área do quadrado: {quadrado.calcular_area()}")