class ConsultaController:
    def __init__(self, request):
        self.request = request
        self.response = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/html"
            },
            "body": "",
            "isBase64Encoded": False
        }

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
        return self.response
