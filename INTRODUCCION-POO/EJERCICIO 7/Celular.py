class Aplicacion:
    def __init__(self, nombre, tamano_mb):
        self.nombre = nombre
        self.tamano_mb = tamano_mb


class Celular:
    def __init__(self):
        self.espacio_disponible = 1024  
        self.aplicaciones = []  
        self.bateria = 100  

    def instalar_aplicacion(self, nombre, tamano_mb):
        if len(self.aplicaciones) >= 20:
            print("No se pueden instalar más aplicaciones (límite de 20).")
            return
        if tamano_mb > self.espacio_disponible:
            print("No hay suficiente espacio para instalar esta aplicación.")
            return

        nueva_app = Aplicacion(nombre, tamano_mb)
        self.aplicaciones.append(nueva_app)
        self.espacio_disponible -= tamano_mb
        print(f"Aplicación '{nombre}' instalada correctamente.")

    def usar_aplicacion(self, nombre, minutos):
        if self.bateria <= 0:
            print("Celular apagado. No hay batería.")
            return

        app = None
        for a in self.aplicaciones:
            if a.nombre == nombre:
                app = a
                break

        if not app:
            print(f"La aplicación '{nombre}' no está instalada.")
            return

    
        if app.tamano_mb > 250:
            consumo_por_10_min = 5
        elif app.tamano_mb > 100:
            consumo_por_10_min = 2
        else:
            consumo_por_10_min = 1

        bloques_de_10_min = minutos // 10
        consumo_total = bloques_de_10_min * consumo_por_10_min

        if consumo_total >= self.bateria:
            self.bateria = 0
            print("La batería se ha agotado. Celular apagado.")
        else:
            self.bateria -= consumo_total
            print(f"Usaste '{nombre}' por {minutos} minutos. Batería restante: {self.bateria}%")

    def mostrar_bateria(self):
        print(f"Batería restante: {self.bateria}%")


mi_celular = Celular()

mi_celular.instalar_aplicacion("WhatsApp", 80)
mi_celular.instalar_aplicacion("Instagram", 260)
mi_celular.instalar_aplicacion("JuegoPesado", 300)

# Usar aplicaciones
mi_celular.usar_aplicacion("WhatsApp", 30)
mi_celular.usar_aplicacion("Instagram", 40)
mi_celular.usar_aplicacion("JuegoPesado", 60)


mi_celular.mostrar_bateria()


mi_celular.usar_aplicacion("Instagram", 100)
