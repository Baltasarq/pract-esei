# Asignatura perteneciente a un curso


from google.appengine.ext import ndb


class Asignatura(ndb.Model):
    curso = ndb.IntegerProperty(indexed=True)
    nombre = ndb.StringProperty(required=True)

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()
