from Estudiantes import Estudiante
from Materia import Materias
from Estudiantes import registroAlumno
from Materia import MateriaPOO

class Notas(Estudiante, Materias):
    pass
    def __init__(self, parcial, lab):
        self.parcial= parcial
        self.lab= lab
        

    def calificar(self):
        nombre = registroAlumno.nombre
        materia = MateriaPOO.materia
        return '{} EN LA NOTA DE PARCIAL OBTUVO {} Y EN EL LABORATORIO OBTUVO LA NOTA DE {}, APROBANDO LA CÁTEDRA DE {}'.format(nombre, self.parcial, self.lab, materia)
    
notaMateria = Notas(7.0, 9.6)
print(notaMateria.calificar())
