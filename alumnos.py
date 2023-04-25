class Alumnos:
    def __init__(self,param_nombre,param_legajo):
        self.nombre = param_nombre
        self.legajo = param_legajo

class Materias:
    def __init__(self,param_nombre,param_creditos):
        self.nombre = param_nombre
        self.creditos = param_creditos


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