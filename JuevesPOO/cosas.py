class Autor:
    def __init__(self, nom, pseudo):
        self.__nombre = nom
        self.__pseudonimo = pseudo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom

    @property
    def pseudonimo(self):
        return self.__pseudonimo

    @pseudonimo.setter
    def pseudonimo(self, pseudo):
        self.__pseudonimo = pseudo

    def __str__(self):
        return f"Nombre: {self.__nombre}\nPseudonimo: {self.__pseudonimo}"

    def escribir(self):
        print(f"El autor {self.__pseudonimo} esta escribiendo su siguiente obra")


class Libro:

    def __init__(self, titulo, aut, year, edit):
        self.__titulo = titulo
        self.__autor = aut
        self.__year = year
        self.__editorial = edit

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def edit(self):
        return self.__editorial

    @edit.setter
    def edit(self, editorial):
        self.__editorial = editorial

    def __str__(self):
        return f"Titulo: {self.__titulo}\nAutor: {self.__autor}\nAño: {self.__year}\nEditorial: {self.__editorial}"

    @classmethod
    def libro_planeta(cls, titulo, aut, year):
        return cls(titulo, aut, year, "Planeta")

    def leer(self, minutos):
        print(f"Leyendo por {minutos} minutos...")


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, ed):
        self.__edad = ed

    def __str__(self):
        return f"Nombre: {self.__nombre}\nEdad: {self.__edad}"

class Estudiante(Persona):
    def __init__(self, nombre, edad, Num_Cuenta, carrera, promedio):
        super().__init__(nombre, edad)
        self.__carrera = carrera
        self.__Numero_Cuenta = Num_Cuenta
        self.__promedio = promedio

    @property
    def carrera(self):
        return self.__carrera

    @carrera.setter
    def carrera(self, carrera):
        self.__carrera = carrera

    @property
    def Num_Cuenta(self):
        return self.__Numero_Cuenta

    @Num_Cuenta.setter
    def Num_Cuenta(self, Num_Cuenta):
        self.__Numero_Cuenta = Num_Cuenta

    @property
    def promedio(self):
        return self.__promedio

    @promedio.setter
    def promedio(self, promedio):
        self.__promedio = promedio

    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nNumero de cuenta: {self.__Numero_Cuenta}\nCarrera: {self.__carrera}\nPromedio: {self.__promedio}"