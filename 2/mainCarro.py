from Carro import Carro
from PilhaCarros import PilhaCarros

pilha = PilhaCarros()

def exibir_menu():
    print("\nMENU")
    print("1. Adicionar carro na pilha")
    print("2. Remover carro da pilha")
    print("3. Imprimir pilha de carros")
    print("4. Sair")

while True:
    exibir_menu()
    opcao = input("Digite um numero: ")

    if opcao == "1":
        marca = input("Digite a marca do carro: ")
        modelo = input("Digite o modelo do carro: ")
        drone = Carro(marca, modelo, portas='5')
        pilha.add(drone)
        print("Carro adicionado à pilha")

    elif opcao == "2":
        veiculo = pilha.remover()
        if veiculo:
            print("Carro removido da pilha")
        else:
            print("Pilha de drones vazia")

    elif opcao == "3":
        pilha.imprimir()

    elif opcao == "4":
        print('Programa encerrado')
        break

    else: print("Numero invalido")
    
    