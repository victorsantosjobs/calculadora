import funcoes
import os

operacao = input("\n\n\n\nDigite o tipo de calculo que deseja realizar.Sendo eles: soma, multiplicacao, adicao, divisao.\n\n\n")

os.system('cls')
match operacao:

    case "soma":
        funcoes.somar()

    case "multiplicacao":
        funcoes.multiplicacao()

    case "divisao":
        funcoes.divisao()

    case "modulo":
        funcoes.produto()

    case "produto":
        funcoes.potencia() 
            
