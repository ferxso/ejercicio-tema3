#ejercicio tema 3

def suma(a,b,c):

    print(a+b+c)

suma(1, 2, 3)



class Coche:   
    puertas = 0
    def agregar_puerta(puertas):
        puertas += 1
        print('cantidad de puertas:' , puertas)

    agregar_puerta(3)
