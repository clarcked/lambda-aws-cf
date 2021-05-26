from spv.consulta.request import ConsultaRequest
from spv.dynamo.dynamo import Dynamo
from spv.s3.jsonb import JSONBucket
from spv.s3.pdfb import PDFBucket
from botocore.exceptions import UnknownKeyError


class ConsultaController:
    def __init__(self, request: ConsultaRequest, mapkeys=[]):
        self.request = request
        self.mapkeys = mapkeys
        self.dynamo = Dynamo()
        self.jsonbucket = JSONBucket()
        self.pdfbucket = PDFBucket()
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

    def setStatus(self, status: int = 200):
        self.response["statusCode"] = status

    def setHeader(self, key, value):
        self.response["headers"][key] = value

    def setContentType(self, value):
        self.setHeader("Content-Type", value)

    def isBase64Encoded(self):
        self.response["isBase64Encoded"] = True

    def setBody(self, body):
        self.response["body"] = body

    def prepare(self):
        pass

    def onResolve(self):
        pass

    def getResponse(self):
        try:
            self.prepare()
            self.onResolve()
            self.setStatus(200)
        except FileNotFoundError | UnknownKeyError as e:
            print(e)
            self.setStatus(404)
        except IOError as e:
            print(e)
            self.setStatus(400)
        except TypeError as e:
            print(e)
            self.setStatus(500)
        finally:
            return self.response
