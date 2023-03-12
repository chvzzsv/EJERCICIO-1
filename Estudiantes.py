class Estudiante:
    def __init__(self, nombre, codigo, carrera):
        self.nombre = nombre
        self.codigo= codigo
        self.carrera= carrera

    def registro(self):
        return 'EL NOMBRE DEL ESTUDIANTE ES: {}. CON EL CÓDIGO {}, ESTUDIA LA CARRERA DE {}'.format(self.nombre, self.codigo, self.carrera)
    
registroAlumno =Estudiante('JAVIER CHÁVEZ', 20210861, 'LIC. EN COMPUTACIÓN.')
print(registroAlumno.registro())
