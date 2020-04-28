# coding: utf-8
# Nueva asignatura


import webapp2
import time

from model.asignatura import Asignatura


class EliminaAsignaturaHandler(webapp2.RequestHandler):
    def get(self):
        asignatura = Asignatura.recupera(self.request)
        asignatura.key.delete()
        time.sleep(1)
        return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/asignaturas/elimina', EliminaAsignaturaHandler)
], debug=True)
