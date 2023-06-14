from cosas import Alumno, Perro

def main():
    a1 = Alumno("Juan", 20, "Contaduría")
    print(vars(a1))

    a1.__nombre = "Mondongo"
    print(vars(a1))

    a1.set_nombre("Maria")
    print(vars(a1))

    print(f"---------To string------")
    print(a1.__str__())

    print("---edad---")
    a1.set_edad(25)
    a1.set_edad(125)

    print("---------Estudiar------")

    a1.estudiar(5)


    print("---------Perro------")
    p1 = Perro("Pug", 2, 0.5)
    print(vars(p1))
    p1.raza = "Chihuahua"
    print(vars(p1))
    p1.__raza = "Pastor Aleman"
    print(vars(p1))

    print("---------To string------")
    p1.edad = 5
    p1.estatura = 0.6
    print(p1)

    cachorro = Perro.es_cachorro(p1.edad)
    print(cachorro)

    print("---------Dormir------")
    p1.dormir(5)

    print("---------Ladrar------")
    p1.ladrar(5)
    p1.ladrar(6)

    danes = Perro.perro_grande(0.8)
    print(danes)
main()