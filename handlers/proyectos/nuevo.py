# coding: utf-8
# Nuevo proyecto


import webapp2
import time

from webapp2_extras import jinja2
from google.appengine.ext import ndb

from model.proyecto import Proyecto


class NuevoProyectoHandler(webapp2.RequestHandler):
    def get(self):
        valores_plantilla = {
            "clave_asignatura": self.request.GET["asg"]
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("nuevo_proyecto.html",
            **valores_plantilla))

    def post(self):
        apellidos = self.request.get("edApellidos", "")
        nombre = self.request.get("edNombre", "")
        titulo = self.request.get("edTitulo", "")
        desc = self.request.get("edDesc", "")
        clave_asignatura = self.request.GET["asg"]

        if (not apellidos
         or not nombre
         or not titulo):
            return self.redirect("/")
        else:
            proyecto = Proyecto(nombre_alumno=nombre,
                                apellidos_alumno=apellidos,
                                titulo=titulo,
                                desc=desc,
                                clave_asignatura=ndb.Key(urlsafe=clave_asignatura))
            proyecto.put()
            time.sleep(1)
            return self.redirect("/proyectos/lista?asg=" + clave_asignatura)


app = webapp2.WSGIApplication([
    ('/proyectos/nuevo', NuevoProyectoHandler)
], debug=True)
