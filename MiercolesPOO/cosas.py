class Alumno:
    facultad = "FES Aragón"

    def __init__(self, nom, ed, carr ):
        self.__nombre = nom
        self.__edad = ed
        self.__carrera = carr

    def set_nombre(self, nom):
        self.__nombre = nom

    def get_nombre(self):
        return self.__nombre

    def set_edad(self, ed):
        if ed >= 8 and ed >= 120:
            self.__edad = ed
        else:
            print("Edad incorrecta")
            self.__edad = 0

    def get_edad(self):
        return self.__edad

    def set_carrera(self, carr):
        self.__carrera = carr

    def get_carrera(self):
        return self.__carrera

    def __str__(self):
        cadena = "nombre: " + self.__nombre + "\n"
        cadena = cadena + "edad: " + str(self.__edad) + "\n"
        cadena = cadena + "carrera: " + self.__carrera + "\n"
        return cadena

    def estudiar(self, horas=1):
        print(f"El alumna/o {self.__nombre} esta estudiando por {horas} horas")

class Perro:
    reino = "Canino"
    def __init__(self, raza, edad, estatura):
        self.__raza = raza
        self.__edad = edad
        self.__estatura = estatura

    #Método de acceso (getter)
    @property
    def raza(self):
        return self.__raza

    #Método de modificación (setter)
    @raza.setter
    def raza(self, raza):
        self.__raza = raza

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if edad > 0 and edad < 20:
            self.__edad = edad
        else:
            print("Edad incorrecta")
            self.__edad = 0

    @property
    def estatura(self):
        return self.__estatura

    @estatura.setter
    def estatura(self, estatura):
        if estatura > 0.1 and estatura < 2:
            self.__estatura = estatura
        else:
            print("Estatura incorrecta")
            self.__estatura = 0

    def __str__(self):
            return f"""
            -----------------------------
            Raza: {self.__raza}
            Edad: {self.__edad}
            Estatura: {self.__estatura}
            -----------------------------
            """

    @staticmethod
    def es_cachorro(edad):
        return edad < 3

    @staticmethod
    def dormir(vueltas = 5):
        for i in range(vueltas):
            print(f"dando vuelta {i + 1}")
        print("Zzzzzz!")

    def ladrar(self, ladridos=1):
        if ladridos >5:
            print("Demasiados ladridos")
        else:
            for i in range(ladridos):
                print("Guau")

    @classmethod
    def perro_grande(cls, est):
        if est > 0.79:
            return cls("",0,est)


    @classmethod
    def contructor_dos(cls, raza, edad):
        if edad > 0 and edad < 20:
            return cls(raza, edad, 0.0)
        else:
            return cls(raza, 0, 0.0)

