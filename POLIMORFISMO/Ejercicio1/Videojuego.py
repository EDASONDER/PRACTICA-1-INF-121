class Videojuego:
    
    def __init__(self, nombre, plataforma, cantidad_jugadores=1):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidad_jugadores = cantidad_jugadores
    
    
    def mostrar(self):
        print(f"Videojuego: {self.nombre}")
        print(f"Plataforma: {self.plataforma}")
        print(f"Jugadores: {self.cantidad_jugadores}")
        print("-" * 20)
    
    
    def agregar_jugadores(self, cantidad=1):
        if cantidad > 0:
            self.cantidad_jugadores += cantidad
            print(f"Se agregó {cantidad} jugador(es). Total: {self.cantidad_jugadores}")
        else:
            print("La cantidad debe ser mayor a 0.")


v1 = Videojuego("The Legend of Zelda", "Nintendo Switch")  
v2 = Videojuego("Cyberpunk 2077", "PC", 0) 

v1.mostrar()
v2.mostrar()


v1.agregar_jugadores()           
v2.agregar_jugadores(3)          