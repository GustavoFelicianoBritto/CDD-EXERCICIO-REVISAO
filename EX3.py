repetir = "s"
while repetir=="s":
    num=int(input("Digite o valor: "))

    if num % 2==0 and num >0:
        print("par e positivo")
    elif num % 2==0 and num <0:
        print("par e negativo")
    elif num % 2==1 and num >0:
        print("impar e positivo")
    elif num % 2==1 and num <0:
        print("impar e negativo")
    else:
        print("Número foi zero")
    repetir=input("\nS = Sim, N= Não\nDeseja repetir? ").lower()
