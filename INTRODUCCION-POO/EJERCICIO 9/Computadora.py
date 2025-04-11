class Computadora:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.estado = "Apagada"

    def mostrar_componentes(self):
        print(f"\nComponentes de la computadora {self.marca} {self.modelo}:")
        print("- Procesador")
        print("- Memoria RAM")
        print("- Disco duro / SSD")
        print("- Tarjeta gráfica")
        print("- Placa base")
        print("- Fuente de poder")

    def mostrar_estado(self):
        print(f"\nEstado actual: {self.estado}")

    def encender(self):
        if self.estado == "Encendida":
            print("\nLa computadora ya está encendida.")
        else:
            self.estado = "Encendida"
            print("\nEncendiendo la computadora...")

    def apagar(self):
        if self.estado == "Apagada":
            print("\nLa computadora ya está apagada.")
        else:
            self.estado = "Apagada"
            print("\nApagando la computadora...")

# Crear instancia de la clase
mi_pc = Computadora("ASUS", "ROG Strix")

# Mostrar componentes
mi_pc.mostrar_componentes()

# Mostrar estado actual
mi_pc.mostrar_estado()

# Encender la computadora
mi_pc.encender()
mi_pc.mostrar_estado()

# Apagar la computadora
mi_pc.apagar()
mi_pc.mostrar_estado()
