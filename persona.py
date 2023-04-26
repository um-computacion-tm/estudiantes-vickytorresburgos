cliente1 = {"nombre":"pepe","apellido":"honguito",}

cliente2 = {"nombre":"pepa","apellido":"fernandez",}

class Persona:
    def __init__(self, persona) -> dict:
        self.nombre = persona.get("nombre")
        self.apellido = persona.get("apellido")
    
    def __init__(self,nombre = "",apellido = ""):
        self.nombre = nombre
        self.apellido = apellido

    def __repr__(self):
        return f"->Persona:[nombre] = {self.nombre} [apellido] = {self.apellido}"


if __name__ == "__main__":
    
    p1 = Persona(cliente1) #p1 = referencia y Persona(cliente1) = objeto
    p2 = Persona(cliente2) #p1 y p2 son referenciadores
    p3 = p1
    p3.nombre = "pablo"
    p4 = Persona("juan","molina")
    print(p1)
    print(p2)
    print(p3)
    print(p4)