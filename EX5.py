salarioMinimo = float(input("Digite o valor atual do salário mínimo: ").replace(',','.'))
salarioAtual = float(input("Digite o valor atual do salário mínim: ").replace(',','.'))

div = salarioAtual/salarioMinimo

print(f"O usuário recebe {div:.1f} vezes o salário mínimo.")