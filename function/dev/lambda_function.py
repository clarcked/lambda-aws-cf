from spv.consulta.request import ConsultaRequest
from spv.consulta.router import ConsultaRouter


def lambda_handler(event, context):
    req = ConsultaRequest(event)
    router = ConsultaRouter(req)
    controller = router.getController()
    return controller.getResponse()

