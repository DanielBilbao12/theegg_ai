#Tarea 33
#Autor: Daniel Bilbao

#region
class Pokemon ():
    def __init__(self, nombre, vida, ataque):
        self.nombre=nombre
        self.vida=vida
        self.ataque=ataque
    def MostrarEstadisticas(self):
        print("La vida de "+str(self.nombre)+" es de "+str(self.vida))

def main():
    Pikachu=Pokemon("Pikachu",100,55)
    Jigglypuff=Pokemon("Jigglypuff",100,45)
    turno=0 #Variable para decidir el turno, en este caso Pikachu es el 1 y Jigglypuff es el 2 --> Podriamos ponerlo de manera aleatoria
    print("¡COMIENZA EL COMBATE!\n")
    while Pikachu.vida>0 and Jigglypuff.vida>0:
        if turno==1: #Turno de pikachu
            Jigglypuff.vida-=Pikachu.ataque
            turno=0
            Jigglypuff.MostrarEstadisticas()
            Pikachu.MostrarEstadisticas()
            print("\n")
        else: #Turno de Jigglypuff
            Pikachu.vida-=Jigglypuff.ataque
            turno=1
            Jigglypuff.MostrarEstadisticas()
            Pikachu.MostrarEstadisticas()
            print("\n")
    if Pikachu.vida<=0:
        print("El ganador del combate es: "+str(Jigglypuff.nombre))
    else:
        print("El ganador del combate es: "+str(Pikachu.nombre))
#endregion

main()