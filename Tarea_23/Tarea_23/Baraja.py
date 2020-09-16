#Definicion de la clase baraja

class Carta :
    def __init__(self,palo,valor):
        self.palo=palo
        self.valor=valor
    def __str__(self):#Funcion para que cuando se printen estos objetos, no se muestre "Baraja.Carta object at 0x0000...(direccion de memoria)
        return "[{}--{}]".format(self.palo,self.valor)


class Baraja :
    def __init__(self):
        palos=["Treboles", "Diamantes","Corazones","Picas"]
        valores=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.mazo=[]
        for t in valores:
            for p in palos:
                carta= Carta(t,p)
                self.mazo.append(carta)
    def MostrarBaraja(self):
        for carta in self.mazo:
            print(carta)
