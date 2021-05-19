import json

from spv.consulta.controllers.controller import ConsultaController
from spv.consulta.request import ConsultaRequest
from spv.utils.utils import hashmap


class JSONController(ConsultaController):
    def __init__(self, request: ConsultaRequest, mapkeys=[]):
        super().__init__(request, mapkeys)
        self.actions = {
            "getResumenPorFecha": self.getResumenPorFecha,
            "getResumenPorCuenta": self.getResumenPorCuenta
        }
        self.setContentType("application/json")

    def getResumenPorCuenta(self):
        return {
            "fecha_cierre_actual": "value fecha_cierre_actual",
            "fecha_cierre_anterior": "value fecha_cierre_actual",
            "saldos_anterior": "value saldos_anterior",
            "saldos_actual": "value saldos_actual",
            "fecha_cierre_actual": "value fecha_cierre_actual",
            "fecha_cierre_anterior": "value fecha_cierre_actual",
            "saldos_anterior": "value saldos_anterior",
            "saldos_actual": "value saldos_actual"
        }

    def getResumenPorFecha(self):
        return {
            "fecha_cierre_actual": "value fecha_cierre_actual",
            "fecha_cierre_anterior": "value fecha_cierre_actual",
            "saldos_anterior": "value saldos_anterior",
            "saldos_actual": "value saldos_actual"
        }

    def resolveJsonFromBucket(self):
        data = {
            "detalle_cuenta": "value detalle_cuenta",
            "movimientos_generales": "value movimientos_generales",
            "movimientos_totales": "value movimientos_totales",
            "fecha_cierre_actual": "value fecha_cierre_actual",
            "fecha_cierre_anterior": "value fecha_cierre_actual",
            "saldos_anterior": "value saldos_anterior",
            "saldos_actual": "value saldos_actual",
            "fecha_cierre_actual": "value fecha_cierre_actual",
            "fecha_cierre_anterior": "value fecha_cierre_actual",
            "saldos_anterior": "value saldos_anterior",
            "descripcion_debito_automatico": "value descripcion_debito_automatico",
            "aviso": "value aviso",
            "saldos_actual": "value saldos_actual"
        }

        return hashmap(self.mapkeys, data)

    def onResolve(self):
        data = self.actions[self.request.getOperation()]()
        self.setBody(json.dumps(data))
