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
            "getResumenURL": self.resolveURL,
            "getLiquidacionURL": self.resolveURL,
        }

    def prepare(self):
        if not self.pdfbucket.has_file(self.request.pdfKey()):
            html = self.resolveHTML()
            data = Generator.genPDF(html, wkhtml=os.environ["WKHTML2PDF_PATH"])
            self.pdfbucket.put(self.request.pdfKey(), data)

    def resolvePDF(self):
        self.isBase64Encoded()
        data = self.pdfbucket.data64("descarga.pdf")
        return data

    def resolveURL(self):
        data = self.request.params
        data["expiration"] = self.pdfbucket.expiration
        data["url"] = self.pdfbucket.sign("descarga.pdf")
        # data = self.pdfbucket.sign("descarga.pdf")
        return data

    def onResolve(self):
        data = self.actions[self.request.getOperation()]()
        self.setBody(data)
