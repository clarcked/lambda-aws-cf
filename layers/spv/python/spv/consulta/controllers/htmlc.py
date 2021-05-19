from spv.consulta.controllers.jsonc import JSONController
from spv.consulta.request import ConsultaRequest
from spv.consulta.view import View
from spv.generator.generator import Generator


class HTMLController(JSONController):
    def __init__(self, request: ConsultaRequest, mapkeys=[]):
        super().__init__(request, mapkeys)
        self.setContentType("text/html")
        self.actions = {
            "getResumenHTML": self.resolveHTML
        }

    def resolveHTML(self):
        data = self.resolveJsonFromBucket()
        # code = data['detalle_cuenta'][1]["pago"]["codigo_de_barras_cabecera"]
        data["barcode"] = Generator.genCode39("00000000")
        return View(self.request, context=data).render()

    def onResolve(self):
        data = self.actions[self.request.getOperation()]()
        self.setBody(data)
