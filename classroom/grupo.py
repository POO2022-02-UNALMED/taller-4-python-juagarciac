from classroom.asignatura import Asignatura

class Grupo:

    __grado="Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
    def __str__(self):
        return "Grupo de estudiantes:"+self._grupo

    @ classmethod
    def grado(cls):
        return cls.__grado

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.__grado = nombre

    def listadoAsignaturas(self, **kwargs):
        if (self._asignaturas==None):
            p=[]
            for x in kwargs:
                p.append(kwargs[x])
            self._asignaturas=p
        else:
            for x in kwargs:
                self._asignaturas.append(kwargs[x])

    def agregarAlumno(self, alumno, lista=None):
        if(self.listadoAlumnos==None):
            if (lista!=None):
                lista.append(alumno)
                self.listadoAlumnos =lista
            else:
                self.listadoAlumnos=alumno
        else:
            if (lista!=None):
                lista.append(alumno)
                self.listadoAlumnos =self.listadoAlumnos+lista
            else:
                self.listadoAlumnos=self.listadoAlumnos+alumno