from spv.consulta.controllers.controller import ConsultaController
from spv.consulta.request import ConsultaRequest


class HTMLController(ConsultaController):
    def __init__(self, request: ConsultaRequest):
        super().__init__(request)
