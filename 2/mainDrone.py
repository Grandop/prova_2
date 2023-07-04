from Drone import Drone
from PilhaDrones import PilhaDrones

pilha = PilhaDrones()

def exibir_menu():
    print("\nMENU")
    print("1. Adicionar drone na pilha")
    print("2. Remover drone da pilha")
    print("3. Imprimir pilha de drones")
    print("4. Sair")

while True:
    exibir_menu()
    opcao = input("Digite um numero: ")

    if opcao == "1":
        marca = input("Digite a marca do drone: ")
        modelo = input("Digite o modelo do drone: ")
        drone = Drone(marca, modelo, quantidadeHelices='8')
        pilha.add(drone)
        print("Drone adicionado à pilha")

    elif opcao == "2":
        veiculo = pilha.remover()
        if veiculo:
            print("Drone removido da pilha")
        else:
            print("Pilha de drones vazia")

    elif opcao == "3":
        pilha.imprimir()

    elif opcao == "4":
        print('Programa encerrado')
        break

    else: print("Numero invalido")
    
    