from ClaseConjunto import Conjunto

def opcion1():
    conjunto3 = conjunto1 + conjunto2
    print(conjunto3)

def opcion2():
    conjunto3 = conjunto1 - conjunto2
    print(conjunto3)

def opcion3():
    bandera = conjunto1 == conjunto2
    print(bandera)

switcher = {
    1: opcion1,
    2: opcion2,
    3: opcion3
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':
    conjunto1 = Conjunto(5,8,7,2,1)
    conjunto2 = Conjunto(5,2,9,1,5)
    bandera = False
    while not bandera:
        print("0 Salir")
        print("1 Unión de conjuntos")
        print("2 Diferencia de conjuntos")
        print("3 Igualdad de conjuntos")

        opcion= int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion)==0