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
        data = self.pdfbucket.data64("descarga.pdf")
        print(data)
        return data

    def onResolve(self):
        data = self.actions[self.request.getOperation()]()
        self.setBody(data)
