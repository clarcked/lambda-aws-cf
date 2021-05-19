from spv.consulta.controllers.controller import ConsultaController
from spv.consulta.request import ConsultaRequest
from spv.s3.pdfb import PDFBucket


class URLController(ConsultaController):
    def __init__(self, request: ConsultaRequest, mapkeys=[]):
        super().__init__(request, mapkeys)
        self.setContentType("text/html")
        self.pdfbucket = PDFBucket()
        self.actions = {
            "getResumenURL": self.resolveURL
        }

    def resolveURL(self):
        data = self.request.params
        data["expiration"] = self.pdfbucket.expiration
        data["url"] = self.pdfbucket.sign("descarga.pdf")
        return data

    def onResolve(self):
        data = self.actions[self.request.getOperation()]()
        self.setBody(data)
