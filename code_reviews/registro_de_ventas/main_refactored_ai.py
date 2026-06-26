def promedio(arreglo):
    if not arreglo:
        return 0.0
    return sum(arreglo) / len(arreglo)


def eliminar_mayores_al_promedio(facturas, importes):
    prom = promedio(importes)
    facturas_filtradas = []
    importes_filtrados = []
    for f, imp in zip(facturas, importes):
        if imp <= prom:
            facturas_filtradas.append(f)
            importes_filtrados.append(imp)
    return facturas_filtradas, importes_filtrados


def reemplazo_facturas_9999(facturas, importes):
    prom = promedio(importes)
    for idx, (f, imp) in enumerate(zip(facturas, importes)):
        if f % 2 == 0 and imp < prom:
            facturas[idx] = 9999
        if imp % 2 == 0 and imp < prom:
            importes[idx] = 9999


def minimo(arreglo):
    if not arreglo:
        return None
    return min(arreglo)


def reemplazo_valor_min(facturas, importes):
    imp_min = minimo(importes)
    if imp_min is None:
        return
    for idx, imp in enumerate(importes):
        if imp == imp_min:
            importes[idx] = -2


def calcula_minimo_facturado(facturas, importes):
    imp_min = minimo(importes)
    if imp_min is None:
        print("No hay importes para calcular el mínimo.")
        return
    idx = importes.index(imp_min)
    print(f"El importe mínimo facturado es: {imp_min}")
    print(f"Pertenece a la factura N° {facturas[idx]}")


def mostrar_facturas_e_importes(facturas, importes):
    print("\nListado de facturas e importes:")
    for f, imp in zip(facturas, importes):
        print(f"  Factura N°{f} → Importe: {imp}")


def cargar_factura_importe():
    facturas = []
    importes = []
    while True:
        try:
            num = int(input("Ingrese el número de factura (0 para terminar): "))
        except ValueError:
            print("Debe ingresar un número entero.")
            continue
        if num == 0:
            break
        if num < 0:
            print("El número de factura no puede ser negativo.")
            continue
        while True:
            try:
                imp = float(input("Ingrese el importe (>= 0): "))
            except ValueError:
                print("Debe ingresar un número válido.")
                continue
            if imp < 0:
                print("El importe no puede ser negativo.")
                continue
            break
        facturas.append(num)
        importes.append(imp)
    return facturas, importes


def main():
    print("EMPRESA TONER PARA IMPRESORAS\nREGISTRO DE VENTAS")
    facturas, importes = cargar_factura_importe()
    if not facturas:
        print("NO HAY NINGÚN REGISTRO REALIZADO")
        return

    calcula_minimo_facturado(facturas, importes)
    mostrar_facturas_e_importes(facturas, importes)

    reemplazo_facturas_9999(facturas, importes)
    reemplazo_valor_min(facturas, importes)
    facturas, importes = eliminar_mayores_al_promedio(facturas, importes)

    print("\nResultados finales:")
    mostrar_facturas_e_importes(facturas, importes)


if __name__ == "__main__":
    main()
