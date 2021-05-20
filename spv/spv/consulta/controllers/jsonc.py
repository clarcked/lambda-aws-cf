import json

from spv.consulta.controllers.controller import ConsultaController
from spv.consulta.request import ConsultaRequest
from spv.utils.utils import hashmap
from spv.dynamo.dynamo import Dynamo
from spv.s3.jsonb import JSONBucket
from spv.s3.pdfb import PDFBucket


class JSONController(ConsultaController):
    def __init__(self, request: ConsultaRequest, mapkeys=[]):
        super().__init__(request, mapkeys)
        self.actions = {
            "getResumenPorFecha": self.getResumenPorFecha,
            "getResumenPorCuenta": self.getResumenPorCuenta,
            "getLiquidacionPorFecha": self.getResumenPorFecha,
            "getLiquidacionesPorCuenta": self.getResumenPorCuenta
        }
        self.setContentType("application/json")
        self.dynamo = Dynamo()
        self.jsonbucket = JSONBucket()
        self.pdfbucket = PDFBucket()

    def getResumenPorCuenta(self):
        items = self.dynamo.query_id(int(self.request.getParam("id")))
        keys = ["fecha_cierre_actual",
                "fecha_vencimiento_actual", "fecha", "Link_resumen"]
        resumenes = []
        for item in items:
            resumen = dict(item["resumen"])
            resumen = hashmap(keys, resumen)
            resumen.update({"Link_resumen": self.pdfbucket.sign(
                "descarga.pdf"), "fecha": item["aaaamm"]})
                # "cuenta_credito": item["cuenta_credito"]
            resumenes.append(resumen)
        return resumenes

    def getResumenPorFecha(self):
        items = self.dynamo.query_fecha(
            int(self.request.getParam("id")), int(self.request.getParam("fecha")))
        for item in items:
            resumen = dict(item["resumen"])
            # resumen.update({"fecha": item["aaaamm"], "cuenta_credito": item["cuenta_credito"]})
        return resumen

    def resolveJsonFromBucket(self):
        data = self.jsonbucket.get(self.request.jsonKey())
        return hashmap(self.mapkeys, data)

    def onResolve(self):
        data = self.actions[self.request.getOperation()]()
        self.setBody(data)
