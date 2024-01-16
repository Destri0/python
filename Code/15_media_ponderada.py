x=[5,10,6,8,3]
y=[.2,.6,.1,.6,.9]
arit=round(sum(i for i in x)/len(x),5)
print('Media aritmética:', arit)
pondera=round(sum(i*j for i,j in zip(x,y)),5)
print('Media ponderada:', pondera)