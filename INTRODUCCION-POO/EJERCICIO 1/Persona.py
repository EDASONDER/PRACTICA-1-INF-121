class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def saludar(self):
        print(f"Hola, soy {self.nombre} de {self.ciudad}")

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False


# a)Crear tres personas
persona1 = Persona("Carlos", 25, "Lima")
persona2 = Persona("María", 17, "Cusco")
persona3 = Persona("Luis", 30, "Arequipa")

# b)Mostrar saludos
persona1.saludar()
persona2.saludar()
persona3.saludar()

# c)Verificar si son mayores de edad
print(f"{persona1.nombre} es mayor de edad: {persona1.es_mayor_de_edad()}")
print(f"{persona2.nombre} es mayor de edad: {persona2.es_mayor_de_edad()}")
print(f"{persona3.nombre} es mayor de edad: {persona3.es_mayor_de_edad()}")
