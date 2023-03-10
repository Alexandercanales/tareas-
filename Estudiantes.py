class Estudiantes:
    def __init__(self, nombre, edad ):
        self.nombre = nombre 
        self.edad = edad   
          
    def informacion(self):
        return"el estudinate {} tiene {} ".format(self.nombre,self.edad) 

InfoEstudiante = Estudiantes ("alexander", 20) 
print (InfoEstudiante.informacion())