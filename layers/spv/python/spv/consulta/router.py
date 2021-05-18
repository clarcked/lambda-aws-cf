from spv.consulta.controllers.controller import ConsultaController
from spv.consulta.controllers.htmlc import HTMLController
from spv.consulta.controllers.jsonc import JSONController
from spv.consulta.controllers.pdfc import PDFController
from spv.consulta.controllers.urlc import URLController
from spv.consulta.request import ConsultaRequest


class ConsultaRouter:
    def __init__(self, request: ConsultaRequest) -> None:
        self.request: ConsultaRequest = request
        self.operations = {
            "getResumenPorFecha": JSONController,
            "getResumenHTML": HTMLController,
            "getResumenPDF": PDFController,
            "getResumenURL": URLController
        }

    def getRequest(self) -> ConsultaRequest:
        self.self_request = self.request
        return self.self_request

    def getController(self, mapkey=[]) -> ConsultaController:
        return self.operations[self.request.getOperation()](self.request, mapkey)
