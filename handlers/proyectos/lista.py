import webapp2
from webapp2_extras import jinja2

from model.proyecto import Proyecto


class ListaProyectosHandler(webapp2.RequestHandler):
    def get(self):
        proyectos = Proyecto.recupera_para(self.request)

        valores_plantilla = {
            "proyectos": proyectos
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("lista_proyectos.html",
            **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/proyectos/lista', ListaProyectosHandler)
], debug=True)
