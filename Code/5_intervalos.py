import random
random.seed()
x = random.randrange(120)
print('Número elegido:',x)
if x<10:
    print('El número es menor de 10')
elif x<50:
    print('El número se encuentra entre el 10 y el 50.')
elif x<100:
    print('El número se encuentra entre el 50 y el 100.')
else:
    print('El número es mayor de 100')