import numpy as np
import matplotlib.pyplot as plt

fig, ax=plt.subplots()
x=np.linspace(-3.0,3.0,100)
y=np.linspace(-3.0,3.0,100)
x,y=np.meshgrid(x,y)
z=np.sqrt(x**2+2*y**2)
ax.contourf(x,y,z)
plt.show()












"""

fig, ax=plt.subplots()
#plt.subplot(1,2,1)
ax.barh([0.1,0.5,0.9],[0.1,0.3,0.9])
#plt.subplot(1,2,2)
#ax.bar([0.4,0.2,0.1,0.3],[0.1,0.2,0.2,0.3])
plt.show()

#grafico de sen y cos con puntos
x=np.arange(0,10,0.1)
y=np.cos(x)
y1=np.sin(x)
plt.plot(x,y,'--',linewidth=1)
plt.axis('equal')
plt.plot(x,y1,'--',linewidth=1)
plt.axis('equal')
plt.show()

#grafico de barras con ciudad
Ciudad=['','Villa','Asu', 'Oviedo']
hab=['0', '10.000', '2.000.000', '30.000']
fig, ax=plt.subplots()
ax.set_title("Cantidad de habitantes")
ax.barh(Ciudad,hab)
plt.show()

#figura de "violin"
fig, ax=plt.subplots()
ax.violinplot([1,2,1,2,3,4,5,6])
plt.show()

#mapa de calor
fig, ax=plt.subplots()
x=np.random.random((14,14))
ax.imshow(x)
plt.show()

#grafico en 3d
axes=plt.axes(projection="3d")
axes.set_title("Mi grafiquito 3D", fontsize=14, fontweight='bold')
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_zlabel('Z')
x=np.linspace(-10,10,1000)
y=np.sin(x)
z=np.tan(x)
axes.plot3D(x,y,z)
plt.show()
"""