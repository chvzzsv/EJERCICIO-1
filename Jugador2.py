class Jugador2():
    def __init__(self, nombre,salud,habilidad):
        self.nombre=nombre
        self.salud=salud
        self.habilidad=habilidad
     
    def BolaDeEnergia(self):
        return'El jugador {} con su vida al {} tiene la habilidad de {} que hace 30  de daño'.format(self.nombre, self.salud, self.habilidad)
    
avatar=Jugador2('samus', 100, 'lanzar una bola de energia recargada')
print(avatar.BolaDeEnergia())