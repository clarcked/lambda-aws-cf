import os

from spv.consulta.controllers.htmlc import HTMLController
from spv.consulta.request import ConsultaRequest
from spv.generator.generator import Generator


class PDFController(HTMLController):
    def __init__(self, request: ConsultaRequest, mapkeys=[]):
        super().__init__(request, mapkeys)
        self.setContentType("application/pdf")
        self.actions = {
            "getResumenPDF": self.resolvePDF,
            "getLiquidacionPDF": self.resolvePDF,
        }

    def resolvePDF(self):
        self.isBase64Encoded()
        html = self.resolveHTML()
        return Generator.genPDF(html, os.environ("WKHTML2PDF_PATH"))

    def onResolve(self):
        data = self.actions[self.request.getOperation()]()
        self.setBody(data)
