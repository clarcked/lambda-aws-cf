from spv.consulta.controllers.jsonc import JSONController
from spv.consulta.request import ConsultaRequest
from spv.consulta.view import View
from spv.generator.generator import Generator


class HTMLController(JSONController):
    def __init__(self, request: ConsultaRequest, mapkeys=[]):
        super().__init__(request, mapkeys)
        self.setContentType("text/html")
        self.generator = Generator()


    def resolveHTML(self):
        data = self.resolveJsonFromBucket()
        data["barcode"] = self.generator.genCode39("00000000")
        view = View(self.request, context=data)
        return view.render()

    def onResolve(self):
        self.setBody(self.resolveHTML())
