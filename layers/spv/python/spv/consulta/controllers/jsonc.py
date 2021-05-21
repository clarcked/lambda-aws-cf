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
        resumenes = []
        for item in items:
            resumen = dict(items[0]["resumen"])
            resumen.update({"Link_resumen": self.pdfbucket.sign("descarga.pdf"), "fecha": str(item["aaaamm"])})
            resumenes.append(resumen)
        return json.dumps(resumenes)

    def getResumenPorFecha(self):
        data = self.resolveJsonFromBucket()
        return json.dumps(data)

    def resolveJsonFromBucket(self):
        print(self.request.jsonKey())
        data = self.jsonbucket.get(self.request.jsonKey())
        return hashmap(self.mapkeys, data)

    def onResolve(self):
        data = self.actions[self.request.getOperation()]()
        self.setBody(data)
