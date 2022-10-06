import random

print("----------------------------------------------------------")
print("-------------------ADIVINAR-EL-NUMERO---------------------")
print("----------------------------------------------------------")

#INPUT
A=random.randint(1,1000)
i=0
X=int(input("Adivina el número: "))
#PROCCESS
while  A!=X:
    i=i+1
    X=int(input("Vuelve a intentarlo: "))
    if X<A:
        print("El numero a adivinar es mas grande")
    elif X>A:
        print("El numero a adivinar es mas pequeño")
    elif X==A:
        print("Felicitaciones has adivinado el numero el numero era:" ,A,"en" ,i,"intentos")

#OUTPUT