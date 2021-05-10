class Coche:
    def __init__(self, marca, color, ruedas,v_max):
        self.marca=marca
        self.color=color
        self.ruedas=ruedas
        self.v_max=v_max

    def acelerar(self):
        return "Estoy acelerando"

    def __repr__(self):
        return "Mi coche es {} y su color es {} y tiene {} ruedas. Y tiene una velocidad maxima de {}".format(self.color,self.marca, self.ruedas,self.v_max)

#reto
evelynCoche=Coche("tesla","negro", 4, 250)
print(evelynCoche)
print(evelynCoche.marca.upper())
print(evelynCoche.color.capitalize())
print(evelynCoche.ruedas)
print(evelynCoche.v_max)
print(evelynCoche.acelerar())
