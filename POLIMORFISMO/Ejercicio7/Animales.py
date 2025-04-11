
class Animal:
    def hacerSonido(self):
        print("Este animal hace un sonido.")  
    
    def moverse(self):
        print("Este animal se mueve.")      


class Perro(Animal):
    def hacerSonido(self):
        print("¡Guau guau! 🐶")  
    
    def moverse(self):
        print("El perro corre en 4 patas. 🏃♂️")  


class Gato(Animal):
    def hacerSonido(self):
        print("¡Miau miau! 🐱")  
    
    def moverse(self):
        print("El gato salta silenciosamente. 🦘")  


class Pajaro(Animal):
    def hacerSonido(self):
        print("¡Pío pío! 🐦")  
    
    def moverse(self):
        print("El pájaro vuela por el cielo. 🌤️")  


# a) Instanciar 1 Perro, 1 Gato y 1 Pájaro
animal1 = Perro()
animal2 = Gato()
animal3 = Pajaro()


# b) Usar hacerSonido() 
print("=== Sonidos de los animales ===")
animal1.hacerSonido()  # Perro
animal2.hacerSonido()  # Gato
animal3.hacerSonido()  # Pájaro

# c) Usar moverse()
print("\n=== Movimiento de los animales ===")
animal1.moverse()  # Perro
animal2.moverse()  # Gato
animal3.moverse()  # Pájaro