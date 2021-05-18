from spv.consulta.controllers.jsonc import JSONController
from spv.consulta.request import ConsultaRequest
from spv.consulta.view import View


class HTMLController(JSONController):
    def __init__(self, request: ConsultaRequest, mapkeys=[]):
        super().__init__(request, mapkeys)

    def onResolve(self):
        print("resolving content html view")
        data = self.resolveFullJson()
        view = View(self.request, context=data)
        self.setBody(view.render())
