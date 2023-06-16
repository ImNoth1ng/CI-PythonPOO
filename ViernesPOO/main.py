from cosas import *


def main():
    per1 = Persona("Luis", 20)
    print(per1)
    print(Persona.descripcion)

    print("------HERENCIA ALUMNO------")
    a1 = Alumno("Mondongo", 20, "123456789", "Ing. en Sistemas")
    print(a1)
    print(Alumno.descripcion)

    a2 = Alumno.constructor_defecto()
    print(a2)
    a2.nombre = "Elizabeth"
    a2.edad = 19
    a2.numero_cuenta = "987654321"
    a2.carrera = "Ing. en Computacion"
    print(a2)
    print("------DORMIR------")
    a2.dormir()

    print("------HERENCIA PROFESOR------")
    p1 = Profesor("Haisenberg", 40, "999999998", "Ing en Quimica")
    print(p1)
    print(Profesor.descripcion)
    p1.dormir()

    print("------HERENCIA AYUDANTE PROFESOR------")

    ay1 = AyudanteProfesor("Jesse", 30, "999892","Ing Quimica", 55985,"Quimicia", 23)
    print(ay1)

    ay1.dormir()
    ay1.dar_clase("Ingles")

main()