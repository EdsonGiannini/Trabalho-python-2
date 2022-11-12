def hora_nova(hora,min):
        if(hora<12):
                A= (f"{hora}:{min}A.M.")
                print(A)
        else:
                hora=hora-12
                P=(f"{hora}:{min}P.M.")
                print(P)
        return
while True:
        hora = int(input("Informe a hora de 0 a 24 ou digite um número negativo para sair: "))
        if hora < 0:
                break
        min = int(input("Informe os minutos: "))

        hora_nova(hora,min)
