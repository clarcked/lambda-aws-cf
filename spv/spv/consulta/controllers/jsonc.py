import json

from spv.consulta.controllers.controller import ConsultaController
from spv.consulta.request import ConsultaRequest
from spv.utils.utils import hashmap
from spv.dynamo.dynamo import Dynamo
from spv.s3.jsonb import JSONBucket

class JSONController(ConsultaController):
    def __init__(self, request: ConsultaRequest, mapkeys=[]):
        super().__init__(request, mapkeys)
        self.actions = {
            "getResumenPorFecha": self.getResumenPorFecha,
            "getResumenPorCuenta": self.getResumenPorCuenta
        }
        self.setContentType("application/json")
        self.dynamo = Dynamo()
        self.jsonbucket = JSONBucket()

    def getResumenPorCuenta(self):
        return self.dynamo.query_id(int(self.request.getParam("id")))

    def getResumenPorFecha(self):
        return self.dynamo.query_fecha(int(self.request.getParam("id")),int(self.request.getParam("fecha")))

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
        data = self.jsonbucket.get(self.request.jsonKey())
        return hashmap(self.mapkeys, data)

    def onResolve(self):
        data = self.actions[self.request.getOperation()]()
        self.setBody(data)
