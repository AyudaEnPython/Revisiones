"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from datetime import datetime
# Clase Base
class Producto:
    def __init__(self, sku, nombre, precio_base):
        self.sku = sku
        self.nombre = nombre
        self.precio_base = precio_base
        self.impuesto_general = 0.18 # Ejemplo de impuesto

    def mostrar_info_base(self):
        return f"SKU: {self.sku} - {self.nombre} | Precio Base: ${self.precio_base:.2f}"

    def calcular_precio_final(self):
        return self.precio_base * (1 + self.impuesto_general)

# Subclase 1: ProductoFisico
class ProductoFisico(Producto):
    def __init__(self, sku, nombre, precio_base, peso_kg, dimensiones):
        super().__init__(sku, nombre, precio_base)
        self.peso_kg = peso_kg
        self.dimensiones = dimensiones # Ej: "30x20x10 cm"
        self.costo_envio_por_kg = 2.5 # Ejemplo

    def calcular_costo_envio(self):
        return self.peso_kg * self.costo_envio_por_kg

    # Sobrescritura de método
    def calcular_precio_final(self):
        precio_con_impuesto = super().calcular_precio_final()
        costo_envio = self.calcular_costo_envio()
        print(f"(Costo envío para {self.nombre}: ${costo_envio:.2f})")
        return precio_con_impuesto + costo_envio

    # Sobrescritura y extensión
    def mostrar_info_base(self):
        info_base = super().mostrar_info_base()
        return f"{info_base} | Peso: {self.peso_kg}kg, Envío: ${self.calcular_costo_envio():.2f}"

# Subclase 2: ProductoDigital
class ProductoDigital(Producto):
    def __init__(self, sku, nombre, precio_base, url_descarga, formato="MP4"):
        super().__init__(sku, nombre, precio_base)
        self.url_descarga = url_descarga
        self.formato = formato

    def enviar_enlace_descarga(self):
        print(f"Enviando enlace para '{self.nombre}' a {self.url_descarga}...")
        # Lógica de envío de email aquí...

    def mostrar_info_base(self):
        info_base = super().mostrar_info_base()
        return f"{info_base} | Formato: {self.formato}, Descargable"

    # Los productos digitales usualmente no tienen costo de envío adicional
    # No es necesario sobrescribir calcular_precio_final si el de la base es suficiente.
    # O se puede sobrescribir para aclarar que no hay costo de envío.
    def calcular_precio_final(self):
        # Para este ejemplo, el precio final es solo el base + impuesto
        print(f"(Producto digital '{self.nombre}' sin costos de envío adicionales)")
        return super().calcular_precio_final()


# Subclase 3: ServicioOnline (Suscripción)
class ServicioOnline(Producto):
    def __init__(self, sku, nombre, precio_base_mensual, duracion_meses=1):
        super().__init__(sku, nombre, precio_base_mensual) # precio_base es mensual
        self.duracion_meses = duracion_meses

    def mostrar_info_base(self):
        self.fecha_activacion = datetime.now().date()
        info_base = super().mostrar_info_base().replace("Precio Base", "Precio Mensual")
        return f"{info_base} | Duración: {self.duracion_meses} mes(es) | Fecha de activación: {self.fecha_activacion}"

    def calcular_precio_final(self): # Para una primera compra o ciclo
        # El impuesto se aplica al precio mensual
        precio_mensual_final = super().calcular_precio_final()
        print(f"(Servicio '{self.nombre}' con precio total por {self.duracion_meses} mes(es))")
        return precio_mensual_final * self.duracion_meses # Asumimos pago total al inicio

    def verificar_estado_suscripcion(self):
        print(f"Verificando estado de '{self.nombre}'. Activo.")
        # Lógica de verificación...

# ... (definiciones de clases Producto, ProductoFisico, ProductoDigital, ServicioOnline) ...

# Creando instancias de nuestros productos
libro_python = ProductoFisico("LIB-001", "Python Pro", 45.00, 0.8, "20x15x3 cm")
antivirus_sub = ServicioOnline("SERV-ANTV", "Antivirus Total 1 Año", 5.00, 12) # 5 USD al mes por 12 meses
curso_video = ProductoDigital("DIG-CRS-003", "Curso P.O.O. Avanzado", 75.00, "miscursos.com/poo")

mi_carrito = [libro_python, antivirus_sub, curso_video]

def mostrar_resumen_carrito(carrito):
    print("\n--- RESUMEN DEL CARRITO ---")
    if not carrito:
        print("El carrito está vacío.")
        return

    for item in carrito:
        # Llamada polimórfica a mostrar_info_base()
        # Cada objeto usará su propia versión del método
        print(item.mostrar_info_base())
    print("---------------------------")

def calcular_total_carrito(carrito):
    total = 0
    print("\n--- CALCULANDO TOTAL DEL CARRITO ---")
    if not carrito:
        print("El carrito está vacío para calcular total.")
        return 0

    for item in carrito:
        # Llamada polimórfica a calcular_precio_final()
        # Cada objeto usará su propia lógica para calcular su precio final
        precio_item = item.calcular_precio_final()
        print(f"Precio final para '{item.nombre}': ${precio_item:.2f}")
        total += precio_item
    print("---------------------------")
    print(f"TOTAL DEL CARRITO: ${total:.2f}")
    return total

# Usando las funciones polimórficas
mostrar_resumen_carrito(mi_carrito)
gran_total = calcular_total_carrito(mi_carrito)

# Ejemplo extra de polimorfismo con una acción específica
print("\n--- PROCESANDO ITEMS ESPECÍFICOS ---")
for item in mi_carrito:
    print(f"Procesando: {item.nombre}")
    if isinstance(item, ProductoDigital):
        item.enviar_enlace_descarga() # Método específico de ProductoDigital
    elif isinstance(item, ServicioOnline):
        item.verificar_estado_suscripcion() # Método específico de ServicioOnline
    # ProductoFisico podría tener un item.preparar_envio()


def imprimir_nombre_y_sku(entidad_con_nombre_y_sku):
    # Esta función no se preocupa por el tipo, solo por los atributos/métodos
    try:
        print(f"Reporte: {entidad_con_nombre_y_sku.nombre} (SKU: {entidad_con_nombre_y_sku.sku})")
    except AttributeError:
        print(f"La entidad no tiene nombre o SKU.")

# Todos nuestros productos funcionan
imprimir_nombre_y_sku(libro_python)

class Empleado: # No hereda de Producto
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.sku = id_empleado # Usamos 'sku' para el ejemplo, podría ser 'id'

juan = Empleado("Juan Perez", "EMP-001")
print("\n--- IMPRIMIENDO INFORMACIÓN DE EMPLEADO ---")
imprimir_nombre_y_sku(juan) # ¡También funciona! (porque tiene .nombre y .sku)