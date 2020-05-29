# El proyecto de un alumno


from google.appengine.ext import ndb

from asignatura import Asignatura


class Proyecto(ndb.Model):
    hora = ndb.DateTimeProperty(auto_now_add=True)
    titulo = ndb.StringProperty(required=True)
    desc = ndb.StringProperty(default="")
    nombre_alumno = ndb.StringProperty(required=True)
    apellidos_alumno = ndb.StringProperty(required=True)
    clave_asignatura = ndb.KeyProperty(kind=Asignatura)

    @staticmethod
    def recupera_para(req):
        try:
            id_asg = req.GET["asg"]
        except KeyError:
            id_asg = ""

        if id_asg:
            clave_asignatura = ndb.Key(urlsafe=id_asg)
            proyectos = Proyecto.query(Proyecto.clave_asignatura == clave_asignatura)
            return (clave_asignatura.get(), proyectos)
        else:
            print("ERROR: asignatura no encontrada")