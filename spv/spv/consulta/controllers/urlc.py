from spv.consulta.controllers.controller import ConsultaController
from spv.consulta.request import ConsultaRequest
from spv.s3.pdfb import PDFBucket


class URLController(ConsultaController):
    def __init__(self, request: ConsultaRequest, mapkeys=[]):
        super().__init__(request, mapkeys)
        self.setContentType("text/html")
        self.pdfbucket = PDFBucket()

    def onResolve(self):
        presigned = self.pdfbucket.sign("descarga.pdf");
        print(presigned)
        self.setBody(presigned)

