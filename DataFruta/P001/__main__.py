# Importando todas as classes e funções do módulo __init__
from __init__ import *

# Função para percorrer duas listas simultaneamente usando zip e imprimir os elementos
def percorrer_listas_com_zip(lista_nomes, lista_salarios):
    for nome, salario in zip(lista_nomes, lista_salarios):
        print(f"{nome}: R${salario}")
        
# Função para calcular o novo salário com reajuste de 10% e imprimir
def calcular_folha_com_reajuste(lista_salarios):
    for salario in lista_salarios:
        print(f"Novo salário com reajuste de 10%: R${salario * 1.1:.2f}")

# Função para modificar o dia das datas anteriores a 2019
def modificar_datas_anteriores_a_2019(lista_datas):
    for data in lista_datas:
        if data < Data(1, 1, 2019):
            data.dia = 1
    print("Datas modificadas com sucesso!")
    
# Função para iterar sobre duas listas usando zip
def iterador_zip(lista_nomes, lista_salarios):
    percorrer_listas_com_zip(lista_nomes, lista_salarios)
    
# Função para iterar sobre uma lista e calcular salários com reajuste usando map
def iterador_map(lista_salarios):
    calcular_folha_com_reajuste(lista_salarios)
    
# Função para iterar sobre uma lista e modificar datas usando filter
def iterador_filter(lista_datas):
    modificar_datas_anteriores_a_2019(lista_datas)

# Função principal que define o menu
def menu():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    while True:
        # menu ao usuário
        print("\n Menu Principal \n")
        print("1. Incluir um nome na lista de nomes")
        print("2. Incluir um salário na lista de salários")
        print("3. Incluir uma data na lista de datas")
        print("4. Incluir uma idade na lista de idades")
        print("5. Percorrer as listas de nomes e salários")
        print("6. Calcular o valor da folha com um reajuste de 10%")
        print("7. Modificar o dia das datas anteriores a 2019")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")
        
        # Executando a ação correspondente à opção escolhida
        if opcao == "1":
            nomes.entrada_de_dados()
        elif opcao == "2":
            salarios.entrada_de_dados()
        elif opcao == "3":
            datas.entrada_de_dados()
        elif opcao == "4":
            idades.entrada_de_dados()
        elif opcao == "5":
            iterador_zip(nomes, salarios)
        elif opcao == "6":
            iterador_map(salarios)
        elif opcao == "7":
            iterador_filter(datas)
        elif opcao == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Verifica se o script está sendo executado como o programa principal
if __name__ == "__main__":
    menu()
