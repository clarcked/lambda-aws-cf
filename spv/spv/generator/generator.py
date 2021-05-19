import pdfkit
import base64
import re

from io import BytesIO
from barcode import Code39
from barcode.writer import ImageWriter


class Generator:
    def __init__(self):
        pass

    @staticmethod
    def genCode39(code):
        barcode = ""
        try:
            io = BytesIO()
            code = re.sub(' +', ' ', code)
            Code39(code, writer=ImageWriter(format="png")).write(io, {
                "module_width": 0.05,
                "module_height": 4,
                "font_size": 6,
                "text_distance": 1,
                "quiet_zone": 3
            })
            b64 = base64.b64encode(io.getvalue())
            barcode = b64.decode("utf-8")
        except IOError as e:
            print(e)
        return barcode

    @staticmethod
    def genPDF(template, wkhtml):
        pdf = ""
        try:
            pdfkit_options = {
                'page-size': 'A4',
                'margin-top': '0',
                'margin-right': '0',
                'margin-bottom': '0',
                'margin-left': '0',
            }
            config = pdfkit.configuration(wkhtmltopdf=wkhtml)
            pdf = pdfkit.from_string(
                template,
                "",
                configuration=config,
                options=pdfkit_options
            )
            b64 = base64.b64encode(pdf)
            pdf = b64.decode("utf-8")
        except FileNotFoundError as e:
            print(e)
        return pdf
