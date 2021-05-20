from spv.utils.utils import hashmap

items = [
    {
        "resumen": {
            "pago_minimo_pesos": "0,00",
            "saldo_actual_pesos": "6.694,45",
            "franquicia_proximo_periodo": "3.358,45",
            "fecha_vencimiento_actual": "30/09/20",
            "saldo_anterior_dolares": "0,00",
            "fecha_vencimiento_anterior": "27/08/20",
            "saldo_actual_dolares": "0,00",
            "fecha_cierre_anterior": "13/08/20",
            "fecha_cierre_proximo": "15/10/20",
            "fecha_cierre_actual": "17/09/20",
            "saldo_anterior_pesos": "15.129,43",
            "fecha_proximo_vencimiento": "28/10/20",
            "pago_minimo_dolares": "0,00"
        },
        "aaaamm": 202008,
        "cuenta_credito": 845540196
    },
    {
        "resumen": {
            "pago_minimo_pesos": "0,00",
            "saldo_actual_pesos": "6.694,45",
            "franquicia_proximo_periodo": "3.358,45",
            "fecha_vencimiento_actual": "30/09/20",
            "saldo_anterior_dolares": "0,00",
            "fecha_vencimiento_anterior": "27/08/20",
            "saldo_actual_dolares": "0,00",
            "fecha_cierre_anterior": "13/08/20",
            "fecha_cierre_proximo": "15/10/20",
            "fecha_cierre_actual": "17/09/20",
            "saldo_anterior_pesos": "15.129,43",
            "fecha_proximo_vencimiento": "28/10/20",
            "pago_minimo_dolares": "0,00"
        },
        "aaaamm": 202009,
        "cuenta_credito": 845540196
    }
]

if "__main__" == __name__:
    # keys = ["fecha_cierre_actual",
    #         "fecha_vencimiento_actual", "fecha", "Link_resumen"]

    keys = ["fecha_cierre_actual",
            "fecha_vencimiento_actual", "fecha", "Link_resumen"]
    resumenes = []
    for item in items:
        resumen = dict(item["resumen"])
        resumen = hashmap(keys, resumen)
        resumen.update({"fecha": item["aaaamm"], "cuenta_credito": item["cuenta_credito"]})
        resumenes.append(resumen)

    print(resumenes)
