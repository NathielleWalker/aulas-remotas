class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Número de portas: {self.numero_portas}")


# Exemplo de uso
carro1 = Carro("Toyota", "Corolla", 4)
carro1.exibir_informacoes()

carro2 = Carro("Fiat", "Uno", 2)
carro2.exibir_informacoes()
