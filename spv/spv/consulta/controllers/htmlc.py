from spv.consulta.controllers.jsonc import JSONController
from spv.consulta.request import ConsultaRequest
from spv.consulta.view import View
from spv.generator.generator import Generator


class HTMLController(JSONController):
    def __init__(self, request: ConsultaRequest, mapkeys=[]):
        super().__init__(request, mapkeys)
        self.setContentType("text/html")
        self.actions = {
            "getResumenHTML": self.resolveHTML,
            "getLiquidacionHTML": self.resolveHTML,
        }

    def resolveHTML(self):
        data = self.resolveJsonFromBucket()
        # meta = data['meta']
        code = data['detalle_cuenta'][1]["pago"]["codigo_de_barras_cabecera"]
        data["barcode"] = Generator.genCode39(code)
        view = View(self.request, context=data)
        # view.setVersion(version)
        return view.render()

    def onResolve(self):
        data = self.actions[self.request.getOperation()]()
        self.setBody(data)
