"""
Crea una clase llamada Aves, tomando en cuenta las características común de
todas las aves
ejemplo:
Tienen plumas, picos, alas… etc
Diferenciarlas en
Tipos: voladores, no voladores
Imprime:
Nombre de la ave, sus características y el tipo
"""

class Aves:
    def __init__(self, nombre, plumas, alas, vuela):
        self.nombre=nombre
        self.plumas=plumas
        self.alas=alas
        self.vuela=vuela

    def __repr__(self):
        return "Esta ave se llama: {} tiene plumas:{} tiene:{} alas y puede volar:{}".format(self.nombre, self.plumas, self.alas, self.vuela)

tucan=Aves("Tuki", "si", 2, "si")
pinguino=Aves("Polo", "si", 2, "no")
avestruz=Aves("Forest", "si", 2, "no")
paloma=Aves("Ataca Autos", "si", 2, "si")

print(tucan)
print(pinguino)
print(avestruz)
print(paloma)

