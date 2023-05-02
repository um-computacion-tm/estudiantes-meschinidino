## CLASE
class Persona:
    # constructor
    def __init__(self, param_nombre, param_email, apellido):
        self.nombre = param_nombre
        self.email = param_email
        self.apellido = apellido
        self.asistencia = 0

    # metodo
    def asistencia_clase(self):
        self.asistencia += 1

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre


class Profesor(Persona):
    def __init__(self, param_nombre, param_email, apellido, legajo_empleado):
        self.legajo_empleado = legajo_empleado
        super().__init__(param_nombre, param_email)


class Alumno:
    def __init__(self, nombre, apellido, email, carrera, materia):
        super().__init__(nombre, apellido, email)
        self.carrera = carrera
        self.materia = materia

    def cambiar_nombre(self, nombre):
        self.nombre = nombre

    def cambiar_email(self, email):
        self.email = email

    def cambiar_apellido(self, apellido):
        self.apellido = apellido

    def cambiar_carrera(self, carrera):
        self.carrera = carrera


class Materia:
    def __init__(self, nombre, facultad, profesor):
        self.nombre = nombre
        self.facultad = facultad
        self.profesor = profesor

    def cambiar_nombre(self, nombre):
        self.nombre = nombre

    def cambiar_facultad(self, facultad):
        self.facultad = facultad

    def cambiar_profesor(self, profesor):
        self.profesor = profesor


## OBJETOS


prof_pepe = Profesor("pepe", "jose@um.edu.ar")

prof_walter = Profesor("walter", "walter@um.edu.ar")

prof_daniel = Profesor("daniel", "daniel@um.edu.ar")

materia_computacion = Materia("Computacion", "Facultad de Ingenieria", prof_pepe)

alumno_dino = Alumno("Dimo", "Meschini", "dino@um.edu.ar", "Ing Informatica", materia_computacion)

print(alumno_dino.nombre, alumno_dino.materia.profesor.nombre)
