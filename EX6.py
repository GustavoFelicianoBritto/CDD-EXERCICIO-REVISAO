peso =  float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em cm: ").replace(',','.'))

imc = peso / (altura * altura)

#print(f"Seu imc é {imc:.1f}")

if imc <= 18.6:
    print(f"Seu imc é {imc:.2f} e você está abaixo do peso")
elif imc > 18.6 and imc <24.9:
    print(f"Seu imc é {imc:.2f} e está no peso ideal")
elif imc > 24.9 and imc <29.9:
    print(f"Seu imc é {imc:.2f} e está levemente acima do peso")
elif imc >29.9 and imc <34.9:
    print(f"Seu imc é {imc:.2f} e está com obesidade grau I")
elif imc > 34.9 and imc <39.9:
    print(f"Seu imc é {imc:.2f} e está com obesidade grau II")
elif imc > 40.0:
    print(f"Seu imc é {imc:.2f} e está com obesidade grau III")
else:
    print(f"Seu imc é {imc:.2f} e está fora da tabela de IMC")