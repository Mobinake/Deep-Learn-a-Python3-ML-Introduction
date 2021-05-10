import matplotlib.pyplot as plt
#grafico 1
x=[1,9,3,6]
y=[1,9,9,9]
#grafico 2
x2=[3,3,0,6]
y2=[1,9,7,7]
#grafico 3
x3=[1,3,8,6]
y3=[1,5,3,3]
#grafico 4
x4=[1]
y4=[1]

color=['orange','brown','grey']

plt.subplot(2,2,1) #dividir el grafico
plt.plot(x,y,'o--')
plt.subplot(2,2,2) #dividir el grafico
plt.plot(x2,y2,'go')
plt.subplot(2,2,3) #dividir el grafico
plt.plot(x3,y3,'--')
plt.subplot(2,2,4) #dividir el grafico

for p,c in zip(x,color):
    plt.axvline(p, label='lineas'.format(p),c=c)

plt.show()


























"""
x=[0.2,0,6,0.8]
color=['blue','yellow','purple']
color2=['orange','brown','grey']
for p,c in zip(x,color):
    plt.axvline(p, label='lineas'.format(p),c=c)
for p, c in zip(x, color2):
    plt.axhline(p, label='lineas'.format(p), c=c)

plt.legend()
plt.show()

x=[1,3,1,4,5,6,7,6,5,4,3,2,3,4,5,4,3,2,4,5,7,5,4,3,1,4,1]
y=[4,1,2,4,2,3,4,3,2,3,1,2,6,3,2,5,3,2,3,4,5,2,3,4,6,7,7]
plt.plot(x, y, 'o--')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.legend()
plt.show()
fig,ax=plt.subplots()
ax.fill_between(x,y)
plt.show()
"""