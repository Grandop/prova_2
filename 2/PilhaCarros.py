from Carro import Carro
class PilhaCarros(Carro):
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def add(self, carro):
        if self.topo == None:
            self.topo = carro
        else:
            carro.proximo = self.topo
            self.topo = carro
        self.tamanho += 1
        self.imprimir()
    
    def imprimir(self):
        print("-----------")
        if self.topo == None:
            print("Pilha Vazia")
        else:
            aux = self.topo
            while( aux ):
                print( aux )
                aux = aux.proximo 
                print("-----------") 
            print("Total de elementos: ", str(self.tamanho) )
    


    def remover(self):
        if self.topo == None:
            print("Pilha Vazia")
        else:
            self.topo = self.topo.proximo
            self.tamanho -= 1
            self.imprimir()