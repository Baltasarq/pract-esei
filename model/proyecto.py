# El proyecto de un alumno


from google.appengine.ext import ndb

from asignatura import Asignatura


class Proyecto(ndb.Model):
    hora = ndb.DateTimeProperty(auto_now_add=True)
    titulo = ndb.StringProperty(required=True)
    nombre_alumno = ndb.StringProperty(required=True)
    apellidos_alumno = ndb.StringProperty(required=True)
    asignatura = ndb.KeyProperty(kind=Asignatura)
