# Função que mostra o menu
def menu():
    print("\n==============================")
    print("   CONVERSOR DE MOEDAS")
    print("==============================")
    print("1 - Real para Dólar")
    print("2 - Dólar para Real")
    print("3 - Real para Euro")
    print("4 - Euro para Real")
    print("5 - Real para Libra")
    print("6 - Libra para Real")
    print("7 - Sair")
    print("==============================")

# Função que faz a conversão 
def converter_moeda(opcao, valor):
    if opcao == 1:
        return valor / 5.0  # Real para Dólar
    elif opcao == 2:
        return valor * 5.0  # Dólar paraReal
    elif opcao == 3:
        return valor / 6.0  # Real para Euro
    elif opcao == 4:
        return valor * 6.0  # Euro para Real
    elif opcao == 5:
        return valor / 6.5  # Real para Libra
    elif opcao == 6:
        return valor * 6.5  # Libra para Real
    else:
        return 0

# Função da moeda de destino
def nome_moeda(opcao):
    if opcao == 1:
        return "Dólares"
    elif opcao == 2:
        return "Reais"
    elif opcao == 3:
        return "Euros"
    elif opcao == 4:
        return "Reais"
    elif opcao == 5:
        return "Libras"
    elif opcao == 6:
        return "Reais"
    else:
        return ""