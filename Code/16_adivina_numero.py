import random
random.seed()
n=random.randrange(1,100)
print('Adivina el número desde el 1 al 100.')
nu=int(input('Introduce un número para adivinarlo: '))
while nu!=n:
    if nu>n:
        nu=int(input('El número es mas pequeño'))
    elif nu<n:
        nu=int(input('El número es mas grande'))
print('Felicidades has adivinado que el número es:',n)