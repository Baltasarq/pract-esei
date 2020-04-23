# coding: utf-8
# Nueva asignatura


import webapp2
import time

from webapp2_extras import jinja2

from model.asignatura import Asignatura


class NuevaAsignaturaHandler(webapp2.RequestHandler):
    def get(self):
        valores_plantilla = {
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("nueva_asignatura.html",
            **valores_plantilla))

    def post(self):
        str_curso = self.request.get("edCurso", "")
        nombre = self.request.get("edNombre", "")

        try:
            curso = int(str_curso)
        except ValueError:
            curso = -1

        if (curso < 0
         or not(nombre)):
            return self.redirect("/")
        else:
            asignatura = Asignatura(nombre=nombre, curso=curso)
            asignatura.put()
            time.sleep(1)
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/asignaturas/nueva', NuevaAsignaturaHandler)
], debug=True)
