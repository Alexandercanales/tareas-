from Estudiantes import Estudiantes
from Materias import Materias
from ParcialLaboratorio import ParcialLaboratorio

class Notas(Estudiantes,Materias):
    pass
        
    def nota():
        return"el estudiante {} en la clase {} tinene las notas de {}".format(Estudiantes.nombre,Materias.materia1,ParcialLaboratorio.califi)
notita = Notas 
print(notita.nota)
    
