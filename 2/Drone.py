from Veiculo import Veiculo

class Drone(Veiculo):
    def __init__(self, marca, modelo, quantidadeHelices):
        super().__init__(marca, modelo)
        self._quantidadeHelices = quantidadeHelices
        self.proximo = None

    def __str__(self):
        texto  = "\n --------------"
        texto += "\nMarca: " + self.marca
        texto += "\nModelo: " + self.modelo
        texto += "\nQuantidade de Helices: " + self._quantidadeHelices
        return texto