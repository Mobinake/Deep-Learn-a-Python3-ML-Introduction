class Perro:
    def __init__(self,raza, edad, estatura, energetico):
        self.raza=raza
        self.edad=edad
        self.estatatura=estatura
        self.energetico=energetico

    def __repr__(self):
        return "El perro tiene {} edad, su raza es {} y su estatura es de {} cm".format(self.edad, self.raza, self.estatatura)

    def Comer(self):
        return "El perro esta comiendo mucho"

    def Dormir(self):
        return "El perro esta durmiendo en tu cama"

    def Jugar(self):
        return "Muy jugueton"

tuPerro=Perro("Rotweiler", 2, 100, "si")
print(tuPerro)
print(tuPerro.Comer())
print(tuPerro.Dormir())
print(tuPerro.Jugar())