import json
import boto3
import pdfkit
import base64
import re

from jinja2 import Template
from io import BytesIO, StringIO
from barcode import Code39
from barcode.writer import ImageWriter

s3 = boto3.client('s3')


def generar_pdf(template, bucket):
    pdf = ""
    try:
        pdfkit_options = {
            'page-size': 'A4',
            'margin-top': '0',
            'margin-right': '0',
            'margin-bottom': '0',
            'margin-left': '0',
        }
        config = pdfkit.configuration(wkhtmltopdf="bin/wkhtmltopdf")
        pdf = pdfkit.from_string(
            template,
            "",
            configuration=config,
            options=pdfkit_options
        )
        print("pdf created")
        b64 = base64.b64encode(pdf)
        pdf = b64.decode("utf-8")
    except FileNotFoundError as e:
        print(e)
    return pdf


def genBarCode39(arg):
    io = BytesIO()
    code = arg.rstrip()
    Code39(code, add_checksum=False, writer=ImageWriter(format="png")).write(io, {
        "module_width": 0.08,
        "module_height": 4,
        "font_size": 6,
        "text_distance": 1,
        "quiet_zone": 1
    })
    b64 = base64.b64encode(io.getvalue())
    return b64.decode("utf-8")


def lambda_handler(event, context):
    responseObj = {}
    responseObj['statusCode'] = 404
    responseObj['headers'] = {}
    responseObj['body'] = ""
    bucket = 'edn-s3-predev-bucket-resumenes-json'
    if "queryStringParameters" not in event:
        return responseObj
    if not event["queryStringParameters"].keys() & {"cuenta", "fecha"}:
        return responseObj
    cuenta = event['queryStringParameters']['cuenta']
    fecha_cierre_actual = event['queryStringParameters']['fecha']
    key = cuenta + '-' + fecha_cierre_actual + '.json'
    doc_type = "html"
    if "doc" in event["queryStringParameters"]:
        doc_type = event['queryStringParameters']['doc']
    try:
        template = open("template.html")
        t = Template(template.read())
        print("bucket key: {}".format(key))
        data = s3.get_object(Bucket=bucket, Key=key)
        dataJson = data['Body'].read().decode("utf-8")
        loadData = json.loads(dataJson)

        num_codigo_barra = loadData['detalle_cuenta'][1]["pago"]["codigo_de_barras_cabecera"]
        barcode = genBarCode39(num_codigo_barra)

        rendered = t.render(
            barcode=barcode,
            detalle_cuenta=loadData['detalle_cuenta'],
            movimientos_generales=loadData['movimientos_generales'],
            movimientos_totales=loadData['movimientos_totales'],
            descripcion_debito_automatico=loadData["descripcion_debito_automatico"],
            descripcion_leyenda=loadData['descripcion_leyenda'],
            cuotas_a_vencer=loadData['cuotas_a_vencer'],
            aviso=loadData['aviso']
        )

        responseObj['statusCode'] = 200
        responseObj['headers']['Content-Type'] = 'text/html'
        responseObj['body'] = rendered

        if doc_type == 'pdf':
            content = generar_pdf(rendered, bucket)
            responseObj['headers']['Content-Type'] = 'application/pdf'
            responseObj['body'] = content
            responseObj['isBase64Encoded'] = True

        if doc_type == 'json':
            responseObj['headers']['Content-Type'] = 'application/json'
            responseObj['body'] = dataJson
    except Exception as e:
        print(e)
        raise e
    return responseObj
