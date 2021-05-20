from spv.consulta.request import ConsultaRequest


class ConsultaController:
    def __init__(self, request: ConsultaRequest, mapkeys=[]):
        self.request = request
        self.mapkeys = mapkeys
        self.actions = {}
        self.response = {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": {
                "codigo": 0,
                "detalle": "",
                "errores": [
                    {
                        "codigo": "",
                        "detalle": "",
                        "origen": "",
                        "spvtrack_id": "",
                        "titulo": ""
                    }
                ],
                "estado": "",
                "tipo": ""
            },
            "isBase64Encoded": False,
        }

    def setStatus(self, status=200):
        self.response["statusCode"] = status

    def setHeader(self, key, value):
        self.response["headers"][key] = value

    def setContentType(self, value):
        self.setHeader("Content-Type", value)

    def isBase64Encoded(self):
        self.response["isBase64Encoded"] = True

    def setBody(self, body):
        self.response["body"] = body

    def onResolve(self):
        pass

    def getResponse(self):
        self.onResolve()
        self.setStatus(200)
        return self.response
