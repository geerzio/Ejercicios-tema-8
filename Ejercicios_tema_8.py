#Crear clase Persona.
#Crear variables las privadas edad, nombre y telefono de la clase Persona.
#Crear gets y sets de cada propiedad. --- Crear un objeto persona en el main.
#Utiliza los gets y sets para darle valores a las propiedades edad, nombre y telefono,
#por último muéstralas por consola


class persona():
    
    def set_edad(self,edad):
        self.__age = edad

    def set_name(self,nombre):
        self.__name = nombre

    def set_num(self,telefono):
        self.__num= telefono   

    def get_edad(self):
        print(f"La edad es {self.__age}")

    def get_name(self):
        print(f"El nombre es {self.__name}")
    
    def get_num(self):
        print(f"El numero de telefono es {self.__num}")

juan = persona()
juan.set_edad(15)
juan.get_edad()

juan.set_name("Juan")
juan.get_name()

juan.set_num(46415353)
juan.get_num()