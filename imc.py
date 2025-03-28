print('Vamos calcular seu IMC')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)
print('Seu IMC é de %.2f' % imc)

def criarTabelaIMC(nome, imc):
    print("\nTabela de Referência de IMC")
    print("---------------------------------")
    print("Nome da Pessoa\t\tClassificação")
    print("---------------------------------")
    
    if imc < 18.5:
        classificacao = "Abaixo do Peso"
    elif 18.5 <= imc < 25:
        classificacao = "Peso Normal"
    elif 25 <= imc < 30:
        classificacao = "Sobrepeso"
    elif 30 <= imc < 35:
        classificacao = "Obesidade Grau I"
    elif 35 <= imc < 40:
        classificacao = "Obesidade Grau II"
    else:
        classificacao = "Obesidade Grau III"
    
    print(f"{nome}\t\t{classificacao}")

criarTabelaIMC(nome, imc)