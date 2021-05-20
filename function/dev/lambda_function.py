from spv.consulta.request import ConsultaRequest
from spv.consulta.router import ConsultaRouter


def lambda_handler(event, context):
    # Patch para hacer test fuera de la APIGW-------------------
    if "operationName" not in event["requestContext"]:
        event["requestContext"]["operationName"] = event["queryStringParameters"]["operationName"]
    # Patch---------------------------------------------------

    mapkeys = ["detalle_cuenta", "movimientos_generales", "movimientos_totales",
               "descripcion_debito_automatico", "descripcion_leyenda", "cuotas_a_vencer", "aviso"]
    req = ConsultaRequest(event)
    router = ConsultaRouter(req)
    controller = router.getController(mapkeys)
    return controller.getResponse()
