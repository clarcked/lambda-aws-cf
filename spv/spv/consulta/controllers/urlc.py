from spv.consulta.controllers.controller import ConsultaController
from spv.consulta.request import ConsultaRequest


class URLController(ConsultaController):
    def __init__(self, request: ConsultaRequest, mapkeys=[]):
        super().__init__(request, mapkeys)
        self.setContentType("application/json")
