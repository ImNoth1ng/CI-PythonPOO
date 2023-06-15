from cosas import Libro, Autor, Persona, Estudiante

def main():
    l1 = Libro.libro_planeta("El perfume", Autor("Patrick Suskind", "PS"), 1985)
    print(l1)

    #cambiando el seudonimo del autor a minusculas
    l1.autor.pseudonimo = l1.autor.pseudonimo.lower()
    print(l1)

    print("--Herencia--")

    est1= Estudiante("Juan", 20, 318858798,"ICO", 10)
    print(est1)

    #cambiando el nombre del estudiante con herencia de Persona
    print("-----Cambiando nombre-----")
    est1.nombre = "Elizabet"
    print(est1)

    #cambiando la edad del estudiante con herencia de Persona
    print("-----Cambiando edad-----")
    est1.edad = 19
    print(est1)


main()