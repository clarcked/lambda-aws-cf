if "__main__" == __name__:
    data = {
        "detalle_cuenta": "value detalle_cuenta",
        "movimientos_generales": "value movimientos_generales",
        "movimientos_totales": "value movimientos_totales",
        "descripcion_debito_automatico": "value descripcion_debito_automatico",
        "aviso": "value aviso",
    }
    mapkeys = ["detalle_cuenta", "avisox", "other", "movimientos_totales"]

    def sanitize(keys, args):
        sanitized = {}
        for index in args:
            if index in keys:
                sanitized[index] = args[index]
        return sanitized

    result = sanitize(mapkeys, data)
    print(result)
