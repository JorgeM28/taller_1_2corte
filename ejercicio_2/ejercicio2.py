print("--------------------------")
print("------NUMERO-INVERSO------")
print("--------------------------")

N=int(input("¿De que numero quieres saber su inverso?: "))
inverso = 0
n1=N

if N >= 0:
    while N > 0:
        r=N % 10
        inverso = inverso * 10 + r
        N = N // 10
    print("\nEl numero",n1,"escrito de forma inversa seria: " +str(inverso),"\n")
else:
    print("El numero ingresado es negativo, por favor digita un numero entero positivo")