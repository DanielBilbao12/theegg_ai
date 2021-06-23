#Clase vaca

class Vaca:
    def __init__(self,peso,produccion,id):
        self.peso=peso
        self.produccion=produccion
        self.id=id
    def Info(self):
        print("La vaca numero "+str(self.id)+" pesa "+str(self.peso)+" kilos y produce "+str(self.produccion)+" litros por dia")




