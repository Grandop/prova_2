from Drone import Drone
class PilhaDrones(Drone):
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def add(self, drone):
        if self.topo == None:
            self.topo = drone
        else:
            drone.proximo = self.topo
            self.topo = drone
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