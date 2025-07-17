print("DIgite o primeiro número: ")
numero1 = float(input())
print("Digite o segundo número: ")
numero2 = float(input())

print("Escolha a operação ")
print("1 - Adiação , 2 - Subtração, 3 - Multiplicação, 4 - Divisão")
operacao = int(input())

match operacao:
    case 1:
        resultado  = numero1 + numero2
        print("O resultado da soma é: ", resultado)
    case 2:
        resultado  = numero1 - numero2
        print("O resultado da subtração é: ", resultado)
    case 3:
        resultado  = numero1 * numero2
        print("O resultado da multiplicação é: ", resultado)
    case 4:  
        resultado = numero1 / numero2
        print("O resultado da divisão é: ", resultado)
    case _:
        print("Operação inválida")
