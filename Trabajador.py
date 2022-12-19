class Persona:
    def __init__(self, id, nombre, apellidos, email, sexo):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.sexo = sexo

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getApellidos(self):
        return self.apellidos

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getSexo(self):
        return self.sexo

    def setSexo(self, sexo):
        self.sexo = sexo
