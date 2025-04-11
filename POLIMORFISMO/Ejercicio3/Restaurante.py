
class Empleado:
    def __init__(self, nombre, sueldo_mes):
        self.nombre = nombre
        self.sueldo_mes = sueldo_mes
    
    def sueldo_total(self):
        return self.sueldo_mes 


class Cocinero(Empleado):
    def __init__(self, nombre, sueldo_mes, horas_extra, sueldo_hora):
        super().__init__(nombre, sueldo_mes)
        self.horas_extra = horas_extra
        self.sueldo_hora = sueldo_hora
    
    def sueldo_total(self):
        return self.sueldo_mes + (self.horas_extra * self.sueldo_hora)

class Mesero(Empleado):
    def __init__(self, nombre, sueldo_mes, horas_extra, sueldo_hora, propina):
        super().__init__(nombre, sueldo_mes)
        self.horas_extra = horas_extra
        self.sueldo_hora = sueldo_hora
        self.propina = propina
    
    def sueldo_total(self):
        return self.sueldo_mes + (self.horas_extra * self.sueldo_hora) + self.propina

class Administrativo(Empleado):
    def __init__(self, nombre, sueldo_mes, cargo):
        super().__init__(nombre, sueldo_mes)
        self.cargo = cargo


def mostrar_empleados_con_sueldo(empleados, sueldo_buscado):
    encontrados = False
    for empleado in empleados:
        if empleado.sueldo_mes == sueldo_buscado:
            print(f"{empleado.nombre} (Cargo: {getattr(empleado, 'cargo', 'N/A')}) - Sueldo base: ${empleado.sueldo_mes}")
            encontrados = True
    if not encontrados:
        print(f"No hay empleados con sueldo base igual a ${sueldo_buscado}")


# a) Instanciar empleados
cocinero = Cocinero("Chef Carlos", 2000, 10, 15.5)
mesero1 = Mesero("Juan", 1500, 5, 10.0, 200)
mesero2 = Mesero("Ana", 1600, 8, 10.0, 300)
admin1 = Administrativo("Luisa", 2500.50, "Gerente")
admin2 = Administrativo("Pedro", 1600, "Asistente")

# b) Calcular sueldos totales
print("\n--- Sueldos Totales ---")
print(f"{cocinero.nombre}: ${cocinero.sueldo_total():.2f}")
print(f"{mesero1.nombre}: ${mesero1.sueldo_total():.2f}")
print(f"{mesero2.nombre}: ${mesero2.sueldo_total():.2f}")
print(f"{admin1.nombre}: ${admin1.sueldo_total():.2f}") 

# c) Filtrar empleados con sueldo_mes == 1600
print("\n--- Empleados con Sueldo Base $1600 ---")
lista_empleados = [cocinero, mesero1, mesero2, admin1, admin2]
mostrar_empleados_con_sueldo(lista_empleados, 1600)