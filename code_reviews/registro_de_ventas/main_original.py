print("EMPRESA TONER PARA IMPRESORAS")
print("REGISTRO DE VENTAS")
arrayFactura = [ ]
arrayImporte = [ ]

def promedio(arreglo):
    suma = 0
    for i in range(0, len(arreglo)):
        suma += arreglo[i]
    if(len(arreglo) != 0):
        promedio = suma/len(arreglo)
    return promedio


def eliminarMayoresAlPromed(arrayFactura, arrayImporte):
    promed = promedio(arrayImporte)
    for i in range(0, len(arrayFactura)):
        if arrayFactura[i] > promed:
            del arrayFactura[i]
            del arrayImporte[i]
    print("Lista final arrayImporte")
    print(arrayImporte)
    print("Lista final arrayFactura")
    print(arrayFactura)


def reemplazoFacturas9999(arrayFactura, arrayImporte):
    promed = promedio(arrayImporte)
    print("El promedio es:", promed)
    for i in range(0, len(arrayFactura)):
        if arrayFactura[i] % 2 == 0 and arrayFactura[i] < promed:
            arrayFactura[i] = 9999
        if arrayImporte[i] % 2 == 0 and arrayImporte[i] < promed:
            arrayImporte[i] = 9999

def minimo(arreglo):
    mini = arreglo [0]
    for i in range(0, len(arreglo)):
        if(arreglo[i] < mini):
            mini = arreglo[i]
    return mini

def reemplazoValorMin(arrayFactura, arrayImporte):
    menor = minimo(arrayImporte)
    for i in range(0, len(arrayFactura)):
        if arrayImporte[i] == menor:
            arrayImporte[i] = -2

def calculaMinimoFacturado(arrayFactura, arrayImporte):
    importMinimo = minimo(arrayImporte)
    print("El importe minimo facturado es:", importMinimo)
    indice = arrayImporte.index(importMinimo)
    print("Pertenece a la factura N"+str(arrayFactura[indice]))


def mostrarFacturasEImportes(arrayFactura, arrayImporte):
    for i in range(0, len(arrayFactura)):
        print("Factura N", arrayFactura[i], "Importe: ",    arrayImporte[i])

def cargarFacturaImporte(arrayFactura, arrayImporte):
    numeroFactura = int(input("Ingrese el numero de factura: "))
    if numeroFactura != 0:
        if numeroFactura > 0:
            arrayFactura.append(numeroFactura)
            elImporte = float(input("Ingrese el importe: "))
            if elImporte < 0:
                print("Ingrese un importe mayor o igual a 0")
            while elImporte < 0:
                elImporte = float(input("Ingrese el importe: "))
                if elImporte < 0:
                    print("Ingrese un importe mayor o igual a 0")
            arrayImporte.append(elImporte)
        else:
            print("No puede ser negativo, ingrese nuevamente!!")
    else:
        return

    while numeroFactura != 0:
        numeroFactura = int(input("Ingrese el numero de factura: "))
        if numeroFactura > 0:
            arrayFactura.append(numeroFactura)
            elImporte = float(input("Ingrese el importe: "))
            if elImporte < 0:
                print("Ingrese un importe mayor o igual a 0")
            while elImporte < 0:
                elImporte = float(input("Ingrese el importe: "))
                if elImporte < 0:
                    print("Ingrese un importe mayor o igual a 0")
            arrayImporte.append(elImporte)
        elif numeroFactura < 0:
            print("No puede ser negativo, ingrese nuevamente!!")


cargarFacturaImporte(arrayFactura, arrayImporte)
if len(arrayFactura) > 0:
    calculaMinimoFacturado(arrayFactura, arrayImporte)
    mostrarFacturasEImportes(arrayFactura, arrayImporte)
    reemplazoFacturas9999(arrayFactura, arrayImporte)
    reemplazoValorMin(arrayFactura, arrayImporte)
    eliminarMayoresAlPromed(arrayFactura, arrayImporte)
else:
    print("NO HAY NINGUN REGISTRO REALIZADO ")

# print(arrayFactura,arryaImporte)

