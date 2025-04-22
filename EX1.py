A= int(input("Digite o primeiro valor: "))
B= int(input("Digite o segundo valor: "))
C= int(input("Digite o terceiro valor: "))

somaAB= A+B

print(f"A soma de A ({A}) e B ({B}) é igual a {somaAB}")
if somaAB<C:
    print(f"A soma de A e B ({somaAB}) é menor que C ({C})")