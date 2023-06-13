from cosas import Alumno

def main():
    """"
    al1 = Alumno()
    print(al1)

    al2 = Alumno()
    print(al2.facultad)
    print(al1.facultad)
    print(Alumno.facultad)
    #OJO
    print("------------------")
    al1.facultad = "Fes Aragon EDOMEX"
    print(al2.facultad)
    print(al1.facultad)
    print(Alumno.facultad)
    print("------------------")
    print(vars(al1))
    print(vars(al2))
    print("------------------")
    al1.edad = 999
    print(vars(al1))

    Al1 = Alumno("Luis", 20, "ICO")
    Al2 = Alumno("Elizabeth", 19, "Mecatronica")
    print(Al1.nombre)
    print(Al1.carrera)
    print(Al2.nombre)
    print(Al2.carrera)
    print("------------------")
    print(vars(Al2))
    """
    Al1 = Alumno("Luis", 20, "ICO")
    print(vars(Al1))
    Al1.__edad= 999
    print(vars(Al1))
main()