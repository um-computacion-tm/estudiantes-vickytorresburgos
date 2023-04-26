"""#clase

class profesor:
    pass

#objetos

profesor_pepe = profesor()
profesor_walter = profesor()
profesor_gabriel = profesor()

print(id(profesor_gabriel))
print(id(profesor_walter))
print(id(profesor_pepe))"""


"""#clase

class profesor:
    def __init__(self,param_nombre):
        self.nombre = param_nombre

profesor_pepe = profesor("pepe")
print(id(profesor_pepe))
print(id(profesor_pepe.nombre))

profesor_walter = profesor("walter")
print(id(profesor_walter))
print(id(profesor_walter.nombre))

profesor_gabriel = profesor("gabriel")
print(id(profesor_gabriel))
print(id(profesor_gabriel.nombre))"""

"""#clase

class profesor:
    def __init__(self,param_nombre):
        self.nombre = param_nombre

    def cambiar_nombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre

#objetos
profesor_pepe = profesor("pepe")
print(id(profesor_pepe))
print(id(profesor_pepe.nombre))

profesor_pepe.cambiar_nombre("jose")
print(profesor_pepe.nombre)"""


"""profesor_walter = profesor("walter")
print(id(profesor_walter))
print(id(profesor_walter.nombre))

profesor_gabriel = profesor("gabriel")
print(id(profesor_gabriel))
print(id(profesor_gabriel.nombre))"""

"""#clase

class profesor:
    def __init__(self,param_nombre,param_email):
        self.nombre = param_nombre
        self.email = param_email

    def cambiar_nombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre

#objetos
profesor_pepe = profesor("pepe")
print(id(profesor_pepe))
print("el nombre es: ")
print(id(profesor_pepe.nombre))
print("el email es: ")
print(id(profesor_pepe.email))


profesor_pepe.cambiar_nombre("jose")
print(profesor_pepe.nombre)"""


"""profesor_walter = profesor("walter")
print(id(profesor_walter))
print(id(profesor_walter.nombre))

profesor_gabriel = profesor("gabriel")
print(id(profesor_gabriel))
print(id(profesor_gabriel.nombre))"""

"""#clase

class profesor:
    def __init__(self,param_nombre,param_email):
        self.nombre = param_nombre
        self.email = param_email
        self.asistencia = 0

    def cambiar_nombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre

    def asistencia_clase(self):
        self.asistencia += 1

#objetos
profesor_pepe = profesor("pepe","jose@um.com")
print(id(profesor_pepe))

print("el nombre es: ")
print(profesor_pepe.nombre)

print("el email es: ")
print(id(profesor_pepe.email))

print("su asistencia es: ")
print(profesor_pepe.asistencia)

print("EL PROFESOR FUE A CLASE...")
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()"""


#clase

class Persona:
    def __init__(self,param_nombre,param_email):
        self.nombre = param_nombre
        self.email = param_email
        self.asistencia = 0
    
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def asistencia_clase(self):
        self.asistencia += 1

class profesor(Persona):
    
    def __init__(self,param_nombre,param_email,legajo_empleado):
        self.legajo_empleado = legajo_empleado
        super().__init__(param_nombre,param_email)

class Alumnos(Persona):
    def __init__(self,param_nombre,param_email,legajo_alumno):
        self.legajo_alumno = legajo_alumno
        self.materias_cursando = []
        super().__init__(param_nombre,param_email)

    def cursando(self,materia):
        self.materias_cursando.append(materia)

class Materias:
    def __init__(self,param_nombre,param_creditos):
        self.nombre = param_nombre
        self.creditos = param_creditos

#objetos
profesor_pepe = profesor("pepe","jose@um.com")
print(id(profesor_pepe))

print("el nombre es: ")
print(profesor_pepe.nombre)

print("el email es: ")
print(id(profesor_pepe.email))
print("su asistencia es: ")
print(profesor_pepe.asistencia)

print("EL PROFESOR FUE A CLASE...")
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()

print("su asistencia es: ")
print(profesor_pepe.asistencia)


valentina_artola = Alumnos("valentina artola","1234")
print(id(valentina_artola))

print("el nombre es: ")
print(valentina_artola.nombre)

print("el legajo es: ")
print(valentina_artola.legajo)

calculo = Materias("calculo","3")
print("el nombre de la materia es: ")
print(calculo.nombre)

print("la cantidad de creditos es: ")
print(calculo.creditos)



