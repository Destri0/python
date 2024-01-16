s=0
for i in range(8*8):
  s+=2**i
  print(i+1,2**i,s)
print("En notación científica es %e,\n y el total es: %E granos de trigo." % (2**i,s))