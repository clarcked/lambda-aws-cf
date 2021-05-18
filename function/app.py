if "__main__" == __name__:
    data = {
        "detalle_cuenta": "value detalle_cuenta",
        "movimientos_generales": "value movimientos_generales",
        "movimientos_totales": "value movimientos_totales",
        "descripcion_debito_automatico": "value descripcion_debito_automatico",
        "aviso": "value aviso",
    }
    mapkeys = ["detalle_cuenta", "aviso"]
    result = list(map(lambda x: data[x], mapkeys))
    print(result)
