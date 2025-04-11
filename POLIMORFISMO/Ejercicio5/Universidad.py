# Clases para los ambientes
class Oficina:
    def __init__(self, nroSillas, nroEscritorios, nroEstanterias):
        self.nroSillas = nroSillas
        self.nroEscritorios = nroEscritorios
        self.nroEstanterias = nroEstanterias
    
    def mostrar(self):
        print("--- Oficina ---")
        print(f"Sillas: {self.nroSillas}")
        print(f"Escritorios: {self.nroEscritorios}")
        print(f"Estanterías: {self.nroEstanterias}")
    
    def cantidadMuebles(self):
        return self.nroSillas + self.nroEscritorios + self.nroEstanterias

class Aula:
    def __init__(self, nombre, capacidad, proyector):
        self.nombre = nombre
        self.capacidad = capacidad
        self.proyector = proyector  # 1 = Sí, 0 = No
    
    def mostrar(self):
        print(f"--- Aula '{self.nombre}' ---")
        print(f"Capacidad: {self.capacidad} personas")
        print(f"Proyector: {'Sí' if self.proyector == 1 else 'No'}")
    
    def cantidadMuebles(self):
        
        return self.capacidad 

class Laboratorio:
    def __init__(self, nombre, capacidad, nroMesas, nroSillas):
        self.nombre = nombre
        self.capacidad = capacidad
        self.nroMesas = nroMesas
        self.nroSillas = nroSillas
    
    def mostrar(self):
        print(f"--- Laboratorio '{self.nombre}' ---")
        print(f"Capacidad: {self.capacidad} personas")
        print(f"Mesas: {self.nroMesas}")
        print(f"Sillas: {self.nroSillas}")
    
    def cantidadMuebles(self):
        return self.nroMesas + self.nroSillas


# a) 2 Oficinas, 2 Aulas, 1 Laboratorio
oficina1 = Oficina(10, 5, 3)
oficina2 = Oficina(8, 4, 2)
aula1 = Aula("A101", 30, 1)
aula2 = Aula("B202", 25, 0)
lab1 = Laboratorio("Lab Química", 20, 10, 20)

# b) Mostrar datos
oficina1.mostrar()
aula1.mostrar()
lab1.mostrar()

# c) Calcular muebles (sobrecarga implícita)
print("\n--- Total de Muebles ---")
print(f"Oficina 1: {oficina1.cantidadMuebles()} muebles")
print(f"Aula 'A101': {aula1.cantidadMuebles()} muebles (asumiendo sillas)")
print(f"Laboratorio 'Lab Química': {lab1.cantidadMuebles()} muebles")