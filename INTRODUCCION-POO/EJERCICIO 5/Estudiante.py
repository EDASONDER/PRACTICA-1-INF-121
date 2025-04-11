class Estudiante:
    def __init__(self, nombre, nota_1, nota_2):
        self.nombre = nombre
        self.nota_1 = nota_1
        self.nota_2 = nota_2

#a)Calcular promedio
    def calcular_promedio(self):
        return (self.nota_1 + self.nota_2) / 2


#b)Mostrar si aprobo
    def aprobo(self):
        promedio = self.calcular_promedio()
        return promedio >= 6

    def mostrar_info(self):
        promedio = self.calcular_promedio()
        estado = "aprobó" if self.aprobo() else "no aprobó"
        print(f"{self.nombre} tiene un promedio de {promedio:.2f} y {estado}.")


#c)Crear tres estudiantes
est1 = Estudiante("Ana", 7.5, 8)
est2 = Estudiante("Pedro", 5, 4)
est3 = Estudiante("Lucía", 6, 6)


est1.mostrar_info()
est2.mostrar_info()
est3.mostrar_info()
