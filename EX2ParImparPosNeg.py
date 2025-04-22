num=int(input("Digite o valor: "))
numPosNeg = ""
numPI=""

if num %2==0:
    numPI="par"
else:
    numPI="impar"
if num >0:
    numPN = "positivo"
elif num <0:
    numPN = "negativo"
else:
    numPN="igual a zero"

print(f"O número {num} é {numPN} e {numPI}")
