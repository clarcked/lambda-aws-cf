class ConsultaRequest:
    def __init__(self, event) -> None:
        self.query = event["queryStringParameters"]
        self.params = event["pathParameters"]
        self.operation = event["requestContext"]["operationName"]

    def getOperation(self):
        return self.operation

    def getQuery(self, key):
        return self.query[key]

    def getParam(self, key):
        return self.params[key]

    def getParams(self):
        return self.params

    def jsonKey(self):
        return "{}-{}.json".format(self.getParam("id"), self.getParam("fecha"))

    def pdfKey(self):
        return "{}-{}.pdf".format(self.getParam("id"), self.getParam("fecha"))
