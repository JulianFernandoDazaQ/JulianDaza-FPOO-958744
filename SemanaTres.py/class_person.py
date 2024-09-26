#---------------
#Person

#dni: int
#name: str
#lasname: int
#role: int
 # self se utiliza en clases      
 # clve valor son propiedades de tipo opjeto es una instancia de la clase definimos la estructura "un contrato"
 # self modifica def__init__ constructor de la clase metodo especial y se pueden campbiar y son una variable siempre se diven inicializar para hacer una variable que tipo de ato es unicializar el 
#---------------

class Person:
    def __init__ (self, dni: int, name: str, lastname: str, role: int):
        self.dni = dni
        self.name = name
        self.lastname = lastname
        self.role = role

    def __repr__(self):
        return F"dni={self.name},{self.lastname}" 

    def __repr__(self):
        return f"dni=".format(self.name,lastname)       

Person1 = Person(dni=123, name="luisito", lastname="velez,", role=1)
Person2 = Person(dni=123, role="estudiante" )
Person3 = 

print(Person1)
 