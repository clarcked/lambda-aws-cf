from spv.consulta.controllers.controller import ConsultaController
from spv.consulta.request import ConsultaRequest


class PDFController(ConsultaController):
    def __init__(self, request: ConsultaRequest, mapkeys=[]):
        super().__init__(request, mapkeys)
        self.setContentType("application/pdf")

    def onResolve(self):
        self.isBase64Encoded()
        self.setBody("PDF lorem ipsum dolor sit met")
