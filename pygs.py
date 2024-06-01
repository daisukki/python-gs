'''Matheus Henriques do Amaral - RM 556957. Turma 1ESPI.'''

#Função e Lista (armazenando alturas futuras).
def calcular_altura_mar(altura_inicial, aumento_anual, anos):
    alturas = []
    ano_atual = 2024
    for _ in range(anos):
        altura_inicial += aumento_anual
        alturas.append((ano_atual, altura_inicial))
        ano_atual += 1
    return alturas


# Exibir os valores
def exibir_alturas(alturas):
    for ano, altura in alturas:
        print(f"Ano {ano}: {altura:.2f} mm")


#Entrada do usuário
def entrada_anos():
    while True:
        try:
            anos = int(input("Por quantos anos deseja projetar o nível do mar? (1 a 20): "))
            if 1 <= anos <= 20:
                return anos
            else:
                print("Por favor, insira um número válido de anos (1 a 20).")
        except ValueError:
            print("Por favor, insira um número válido.")

# Variáveis iniciais
altura_inicial = 101
aumento_anual = 3.4
anos = entrada_anos()

# Cálculo das alturas futuras
alturas_futuras = calcular_altura_mar(altura_inicial, aumento_anual, anos)

# Exibição das alturas futuras
exibir_alturas(alturas_futuras)
