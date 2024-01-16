x=0
numeros=[]
while(x < 1):
    x = int(input('¿Cuántos números quieres?'))
for i in range(x):
    z = float(input('Dame un número:'))
    numeros.append(z)
print('Media = ', sum(numeros)/x)