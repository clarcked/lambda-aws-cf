from spv.consulta.controllers.jsonc import JSONController
from spv.consulta.request import ConsultaRequest
from spv.consulta.view import View

class HTMLController(JSONController):
    def __init__(self, request: ConsultaRequest, mapkeys=[]):
        super().__init__(request, mapkeys)
        self.setContentType("text/html")

    def onResolve(self):
        data = self.resolveJsonFromBucket()
        view = View(self.request, context=data)
        self.setBody(view.render())
