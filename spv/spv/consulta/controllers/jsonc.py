import json

from spv.consulta.controllers.controller import ConsultaController
from spv.consulta.request import ConsultaRequest


class JSONController(ConsultaController):
    def __init__(self, request: ConsultaRequest, mapkeys=[]):
        super().__init__(request, mapkeys)
        self.setContentType("application/json")

    def resolveJson(self):
        return {
            "fecha_cierre_actual": "value fecha_cierre_actual",
            "fecha_cierre_anterior": "value fecha_cierre_actual",
            "saldos_anterior": "value saldos_anterior",
            "saldos_actual": "value saldos_actual"
        }

    def resolveFullJson(self):
        data = {
            "detalle_cuenta": "value detalle_cuenta",
            "movimientos_generales": "value movimientos_generales",
            "movimientos_totales": "value movimientos_totales",
            "descripcion_debito_automatico": "value descripcion_debito_automatico",
            "aviso": "value aviso",
        }
        return map(lambda x: print(x), self.mapkeys)

    def onResolve(self):
        data = self.resolveJson()
        self.setBody(json.dumps(data))
