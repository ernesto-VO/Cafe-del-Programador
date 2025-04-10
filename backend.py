import csv
import datetime
import re

# ----- CARGA DE DATOS DESDE CSV -----
def guardar_todos_los_datos():
    Inventario.guardar_ingredientes_csv()  # Guardar ingredientes
    Producto.guardar_productos_csv()       # Guardar productos
    guardar_clientes_csv()                 # Guardar clientes
    guardar_empleados_csv()                # Guardar empleados
    guardar_promos_csv()                   # Guardar promociones
    guardar_pedidos_realizados_csv()       # Guardar pedidos realizados
    guardar_opciones_extra_csv()           # Guardar opciones extra



def cargar_todos_los_datos():
    cargar_ingredientes_csv()    # Cargar ingredientes
    cargar_productos_csv()       # Cargar productos
    cargar_clientes_csv()        # Cargar clientes
    cargar_empleados_csv()       # Cargar empleados
    cargar_promos_csv()          # Cargar promociones
    cargar_opciones_extra_csv()  # Cargar opciones extra



def cargar_ingredientes_csv():
    Inventario.lista_ingredientes.clear()
    try:
        with open('ingredientes.csv', newline='') as archivo:
            reader = csv.DictReader(archivo)
            for row in reader:
                Inventario(int(row['id']), row['nombre'], float(row['cantidad']), row['unidadMedida'])
    except FileNotFoundError:
        print("No se encontró ingredientes.csv")

def guardar_ingredientes_csv():
    with open('ingredientes.csv', 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['id', 'nombre', 'cantidad', 'unidadMedida'])  # Escribe los encabezados
        for ing in Inventario.lista_ingredientes:
            writer.writerow([ing.id, ing.nombre, ing.cantidad, ing.unidadMedida])  # Escribe cada ingrediente



def cargar_productos_csv():
    Producto.todosLosProductos.clear()
    try:
        with open('productos.csv', newline='') as archivo:
            reader = csv.DictReader(archivo)
            for row in reader:
                ingredientes = []
                ingredientes_str = row['ingredientes'].split(';')
                for ing_str in ingredientes_str:
                    nombre, cantidad = ing_str.split(':')
                    for ing in Inventario.lista_ingredientes:
                        if ing.nombre == nombre:
                            ingredientes.append((ing, float(cantidad)))
                Producto(row['nombre'], float(row['precio']), row['info'], ingredientes, row['puntos'])
    except FileNotFoundError:
        print("No se encontró productos.csv")

def guardar_productos_csv():
    with open('productos.csv', 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['nombre', 'precio', 'info', 'ingredientes', 'puntos'])  # Escribe los encabezados
        for producto in Producto.todosLosProductos:
            # Convertimos los ingredientes en un string con formato 'nombre:cantidad'
            ingredientes_str = ';'.join(f"{ing.nombre}:{cant}" for ing, cant in producto.ingredientes)
            writer.writerow([producto.nombre, producto.precio, producto.info, ingredientes_str, producto.puntos])  # Escribe el producto


        


def cargar_clientes_csv():
    ClienteRegistrado.listaClientesRegustrados.clear()
    try:
        with open('clientes.csv', newline='') as archivo:
            reader = csv.DictReader(archivo)
            for row in reader:
                ClienteRegistrado(row['nombre'], row['contraseña'], row['telefono'], row['email'], row['puntos_acumulados'])
    except FileNotFoundError:
        print("No se encontró clientes.csv")
    
def guardar_clientes_csv():
    with open('clientes.csv', 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['nombre', 'contraseña', 'telefono', 'email', 'puntos_acumulados'])
        for cliente in ClienteRegistrado.listaClientesRegustrados:
            writer.writerow([cliente.nombre, cliente.contraseña, cliente.telefono, cliente.email, cliente.puntos_acumulados])

def guardar_empleados_csv():
    with open('empleados.csv', 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['nombre', 'contraseña', 'ide', 'numero', 'email', 'rol'])
        for emp in Empleado.listaEmpleados:
            writer.writerow([emp.nombre, emp.contraseña, emp.ide, emp.numero, emp.email, emp.rol])

def cargar_empleados_csv():
    Empleado.listaEmpleados.clear()
    try:
        with open('empleados.csv', newline='') as archivo:
            reader = csv.DictReader(archivo)
            for row in reader:
                Empleado(row['nombre'], row['contraseña'], row['ide'], row['numero'], row['email'], row['rol'])
    except FileNotFoundError:
        print("No se encontró empleados.csv")


def guardar_promos_csv():
    with open('promociones.csv', 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['nombre', 'descripcion', 'tipo', 'modificador', 'condicion'])
        for promo in PromocionesPuntos.listaPromos:
            writer.writerow([promo.nombre, promo.descripcion, promo.tipo, promo.modificador, promo.condicion])

def cargar_promos_csv():
    PromocionesPuntos.listaPromos.clear()
    try:
        with open('promociones.csv', newline='') as archivo:
            reader = csv.DictReader(archivo)
            for row in reader:
                PromocionesPuntos(row['nombre'], row['descripcion'], row['tipo'], float(row['modificador']), int(row['condicion']))
    except FileNotFoundError:
        print("No se encontró promociones.csv")



def guardar_pedidos_realizados_csv():
    with open('pedidos_realizados.csv', 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['nombreCliente', 'productos', 'precio', 'fecha', 'estado'])
        for pedido in Pedido.listaPedidoEchos:
            productos_str = '|'.join([f"{p.producto.nombre}:{p.cantidad}" for p in pedido.lista_productos_pedido])
            writer.writerow([pedido.nombreCliente, productos_str, pedido.precio, pedido.fecha, pedido.estado])

def guardar_opciones_extra_csv():
    with open('opciones_extra.csv', 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['nombre', 'costo', 'ingredienteAModificar', 'modificador', 'descripcion', 'producto'])
        for opcion in OpcionExtra.listaOpcionesExtra:
            writer.writerow([opcion.nombre, opcion.costo, opcion.ingredienteAModificar.nombre, opcion.modificador, opcion.descripcion, opcion.ProsuctoAlQuePertenece.nombre])

def cargar_opciones_extra_csv():
    OpcionExtra.listaOpcionesExtra.clear()
    try:
        with open('opciones_extra.csv', newline='') as archivo:
            reader = csv.DictReader(archivo)
            for row in reader:
                # Buscar el producto correspondiente y el ingrediente al que modificar
                producto = next((p for p in Producto.todosLosProductos if p.nombre == row['producto']), None)
                ingrediente = next((i for i in Inventario.lista_ingredientes if i.nombre == row['ingredienteAModificar']), None)
                if producto and ingrediente:
                    OpcionExtra(row['nombre'], float(row['costo']), ingrediente, float(row['modificador']), row['descripcion'], producto)
    except FileNotFoundError:
        print("No se encontró opciones_extra.csv")



class Cliente:
    def __init__(self):
        self.rol = "cliente"
        self.lista_productos_pedido = []
        self.promocionesAplicadas = []

    def agregarAlPedido(self, producto, cantidad = 1, extras=None):
        pedido = ProductoPedidoTemporal(producto, cantidad, extras)
        self.lista_productos_pedido.append(pedido)

    def calcular_total_parcial(self):
        cantidad_total = 0
        for producto in self.lista_productos_pedido:
          cantidad_total += producto.calcularTotalPrecioProducto()
        return cantidad_total 
            
    def calcular_total(self):
        precio = self.calcular_total_parcial()
        texto = ""
        if len(self.promocionesAplicadas):
            for promo in  self.promocionesAplicadas:
                texto+=f" promocion aplicada: {promo.nombre} \n"
                precio -= PromocionesPuntos.aplicarPromo(self, self.calcular_total_parcial(), promo)
                print(precio)
            return f"{texto} promocion aplicada correctamente precio final: ${precio}"
        else:
            return f"total: ${precio}"
        
    def quitar_producto_pedido(self, producto):
        if producto in self.lista_productos_pedido:
            self.lista_productos_pedido.remove(producto)
        else:
            return False
    
    def agregarPromo(self, promo):
        self.promocionesAplicadas.append(promo)
        
    def hacerPedido(self):
        nombre = input("a nombre de quien es el pedido?")

        print("confirmacion del pedido:")
        print(f"nombre: {nombre}\npedido:")
        
        for producto_pedido in self.lista_productos_pedido:
            print(f"- {producto_pedido}")  # Aquí se invoca el __str__() de ProductoPedidoTemporal
        
        print(f"{self.calcular_total()}")

        respuesta = input("desea segir con el pago? (y/n)")
        if respuesta == "y":
            pago= False
            while pago == False:
                nombrecompleto = input("ingresa tu nombre")
                numero_tarjeta = input("ingresa el nuemro de la tarjeta")
                fecha_vencimiento = input("ingresa la fehca de vencimiento (MM/AA)")
                cvv = input("ingresa el cvv")
                pago = Cliente.verificar_tarjeta(nombrecompleto, numero_tarjeta, fecha_vencimiento, cvv)
            Inventario.quitarPorPedido(self)

            if isinstance(self,  ClienteNoRegistrado):
                pedidoUsuario = Pedido(nombre, self.lista_productos_pedido, self.calcular_total())
                print("pedido realizado correctamente!")
                self.lista_productos_pedido = []

            elif isinstance(self, ClienteRegistrado):
                pedidoUsuario = Pedido(nombre, self.lista_productos_pedido, self.calcular_total())
                print(f"{self.nombre} tu pedido a nombre de {nombre} fue  realizado correctamente!")
                self.lista_pedidos.append(pedidoUsuario)
                puntosTotales = 0
                for productoObj in self.lista_productos_pedido:
                        puntosTotales+= productoObj.producto.puntos*productoObj.cantidad
                self.puntos_acumulados += puntosTotales
                self.lista_productos_pedido = []
        else: 
            print("pago cancelado (tu pedido no a sido descartado, aun puedes egir ordenando)")



    
    @classmethod
    def pagar(self, nombre_completo, numero_tarjeta, fecha_vencimiento, cvv):
        fecha_actual = datetime.date.today()

        if len(nombre_completo) > 5 and self.verificar_tarjeta(numero_tarjeta) and fecha_actual < fecha_vencimiento and cvv <= 4:
            print("Pago exitoso.")
            return True
        else:
            print("Pago fallido. Verifique los detalles de pago.")
            return False

    @classmethod
    def verificar_tarjeta(cls, nombre_completo, numero_tarjeta, fecha_vencimiento, cvv):

        # 1. Validación del nombre
        if len(nombre_completo) < 5:
            print("Nombre inválido. Debe tener al menos 5 caracteres.")
            return False

        # 2. Validación del número de tarjeta
        numero_tarjeta = ''.join(filter(str.isdigit, numero_tarjeta))
        if not re.match(r'^\d{13,19}$', numero_tarjeta):  # Acepta longitudes comunes de tarjetas
            print("Número de tarjeta inválido. Debe contener solo dígitos y tener una longitud válida.")
            return False

        # Algoritmo de Luhn (opcional, para verificar la validez del número)
        n_digitos = len(numero_tarjeta)
        n_sum = 0
        es_segundo_digito = False
        for i in range(n_digitos - 1, -1, -1):
            d = int(numero_tarjeta[i])
            if es_segundo_digito:
                d *= 2
                if d > 9:
                    d -= 9
            n_sum += d
            es_segundo_digito = not es_segundo_digito
        if (n_sum % 10) != 0:
            print("Número de tarjeta inválido (falla el algoritmo de Luhn).")
            return False

        # 3. Validación de la fecha de vencimiento
        try:
            mes, anio = map(int, fecha_vencimiento.split('/'))
            fecha_vencimiento = datetime.date(2000 + anio, mes, 1)  # Asume el siglo XXI
            fecha_actual = datetime.date.today()
            if fecha_vencimiento < fecha_actual:
                print("Fecha de vencimiento inválida. La tarjeta ha expirado.")
                return False
        except ValueError:
            print("Formato de fecha de vencimiento inválido. Debe ser MM/AA.")
            return False

        # 4. Validación del CVV
        if not re.match(r'^\d{3,4}$', cvv):
            print("CVV inválido. Debe contener 3 o 4 dígitos.")
            return False

        return True

class ClienteNoRegistrado(Cliente):
    def __init__(self):
        super().__init__()

class ClienteRegistrado(Cliente):

    listaClientesRegustrados = []

    def __init__(self, nombre, contraseña, telefono, email, puntos_acumulados=0):
        super().__init__()
        self.nombre = nombre
        self.contraseña = contraseña
        self.telefono = telefono
        self.email = email
        self.lista_pedidos = []
        self.puntos_acumulados = int(puntos_acumulados)
        ClienteRegistrado.listaClientesRegustrados.append(self)
    
    def cancelar_pedido(self,pedido):
        self.lista_pedidos.remove(pedido)

import datetime

class Pedido:
    listaPedidosPendientes = []
    listaPedidoEchos = []

    def __init__(self, nombreCliente, lista_productos_pedido, precio):
        self.nombreCliente = nombreCliente
        self.lista_productos_pedido = lista_productos_pedido
        self.precio = precio
        self.fecha = datetime.datetime.now()
        self.estado = "pendiente"
        Pedido.listaPedidosPendientes.append(self)

    

class Producto:
    # este si coupoa base de datos
    todosLosProductos = []

    # estos no XD
    ProductosDisponibles = []
    ProductosNoDisponibles = []

    def __init__(self, nombre, precio, info, ingredientes, puntos=0):
        self.nombre = nombre
        self.precio = precio
        self.info = info
        self.ingredientes = ingredientes
        self.puntos = int(puntos)
        Producto.todosLosProductos.append(self)

    def actualizarProductosDiscponibles(self):
        for producto in Producto.ProductosDisponibles:
            if Producto.disponibilidad(producto) == False:
                Producto.ProductosDisponibles.remove(producto)
                Producto.ProductosNoDisponibles.append(producto)
        for producto in Producto.ProductosNoDisponibles:
            if Producto.disponibilidad(producto) == True:
                Producto.ProductosDisponibles.append(producto)
                Producto.ProductosNoDisponibles.remove(producto)

    def descripcion(self):
        print(f"Nombre: {self.nombre} \nPrecio: ${self.precio} \nDescripción: {self.info}\nIngredientes:")
        for ingrediente, cantidad_necesaria in self.ingredientes:
            print(f"nombre: {ingrediente.nombre}, cantidad necesaria: {cantidad_necesaria}")

        print(f"Puntos por compra: {self.puntos}")
        print("\n")

    def agregarOpcionesExtra(self, nombre, costo, modificador, descripcion):
        opcion = OpcionExtra(nombre, costo, modificador, descripcion)
        self.opcionesExtra.append(opcion)

    def MostrarOpcionesExtra(self):
        for opcion in self.opcionesExtra:
            return (f"nombre: {opcion.nombre}, costo: ${opcion.costo} \n {opcion.descripcion}")

    def guardar_productos_csv():
        with open('productos.csv', 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(['nombre', 'precio', 'info', 'ingredientes', 'puntos'])
            for producto in Producto.todosLosProductos:
                ingredientes_str = ';'.join(f"{ing.nombre}:{cant}" for ing, cant in producto.ingredientes)
                writer.writerow([producto.nombre, producto.precio, producto.info, ingredientes_str, producto.puntos])


    @classmethod
    def disponibilidad(cls, producto):
        for ingrediente, cantidad_necesaria in producto.ingredientes:
            if ingrediente.cantidad < cantidad_necesaria:
                return False
        return True

    def __str__(self):
        return f"{self.nombre} - ${self.precio} - {self.info}"  # Incluye los atributos relevantes


class OpcionExtra():
    listaOpcionesExtra = []

    def __init__(self, nombre, costo, ingredienteAModificar, modificador, descripcion, ProsuctoAlQuePertenece):
        self.nombre = nombre
        self.costo = costo
        self.ingredienteAModificar = ingredienteAModificar
        self.modificador = modificador
        self.descripcion = descripcion
        self.ProsuctoAlQuePertenece = ProsuctoAlQuePertenece
        OpcionExtra.listaOpcionesExtra.append(self)


class ProductoPedidoTemporal():
    def __init__(self, producto, cantidad, extras):
        self.producto = producto
        self.cantidad = cantidad
        self.extras = extras

    def calcularTotalPrecioProducto(self):
        if self.extras:
            precio_total = (self.producto.precio + self.extras.costo) * self.cantidad
        else:
            precio_total = self.producto.precio * self.cantidad
        return precio_total

    def __str__(self):
        if self.extras:
            return f"{self.producto.nombre} (x{self.cantidad}), extra: {self.extras.nombre}, precio total de el producto/s: ${self.calcularTotalPrecioProducto()}"
        else:
            return f"{self.producto.nombre} (x{self.cantidad}), sin extras, precio total de el producto/s: ${self.calcularTotalPrecioProducto()}"


        
class Inventario:
    lista_ingredientes=[]

    def __init__(self, id, nombre, cantidad, unidadMedida):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidadMedida = unidadMedida
        Inventario.lista_ingredientes.append(self)
    
    def guardar_ingredientes_csv():
        with open('ingredientes.csv', 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(['id', 'nombre', 'cantidad', 'unidadMedida'])
            for ing in Inventario.lista_ingredientes:
                writer.writerow([ing.id, ing.nombre, ing.cantidad, ing.unidadMedida])
    
    def cargar_ingredientes_csv():
        Inventario.lista_ingredientes.clear()
        with open('ingredientes.csv', newline='') as archivo:
            reader = csv.DictReader(archivo)
            for row in reader:
                Inventario(int(row['id']), row['nombre'], float(row['cantidad']), row['unidadMedida'])



    @classmethod
    def quitarPorPedido(cls, pedidoComleto):
        for pedido in pedidoComleto.lista_productos_pedido:
                for ingrediente, cantidadIngrediente in pedido.producto.ingredientes:
                    if pedido.extras and ingrediente==pedido.extras.ingredienteAModificar:
                        ingrediente.cantidad -= cantidadIngrediente*pedido.extras.modificador
                    else:
                        ingrediente.cantidad -= cantidadIngrediente

    @classmethod
    def mostrar_inventario(cls):
        for ingrediente in Inventario.lista_ingredientes:
            print(f"id:{ingrediente.id}, nombre:{ingrediente.nombre}, cantidad: {ingrediente.cantidad}")
        print("\n\n")


class PromocionesPuntos():
    listaPromos = []
    def __init__(self, nombre, descripcion, tipo, modificador, condicion=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo = tipo
        self.modificador = modificador
        self.condicion = condicion
        PromocionesPuntos.listaPromos.append(self)

    @classmethod
    def aplicarPromo(cls, cliente, precio, promocion):
        if cliente.puntos_acumulados > promocion.condicion:
            if promocion.tipo=="porcentaje":
                precio*= promocion.modificador
                return precio
            if promocion.tipo == "fijo":
                precio= promocion.modificador
                return precio
        else:
            return f"no tienes los suficientes puntos apra canjear"
        
        @classmethod
        def verPromos(cls):
            for promo in PromocionesPuntos.listaPromos:
                print (promo)
            
    def __str__(self):
        return f"{self.nombre}\n{self.descripcion}"
    
class Empleado:

    listaEmpleados = []
    
    def __init__(self, nombre, contraseña, ide, numero, email, rol):
        self.nombre = nombre
        self.contraseña = contraseña
        self.ide = ide
        self.numero = numero
        self.email = email
        self.rol = rol
        Empleado.listaEmpleados.append(self)

    def verPedidosPendientes(self):
        for pedido in Pedido.listaPedidosPendientes:
            print(f"Cliente: {pedido.nombreCliente}")
            print("Productos:")
            for producto_pedido in pedido.lista_productos_pedido:
                 print(f"-{producto_pedido}")  
            print(f"Precio Final: ${pedido.precio}\n")

    def completarPedido(self, pedido):
        pedido.estado="listo"
        Pedido.listaPedidoEchos.append(pedido)
        Pedido.listaPedidosPendientes.remove(pedido)

    def agregar_mas_ingredientes(self, ingrediente, cantidad_agregar):
        ingrediente.cantidad += cantidad_agregar

    def quitar_cantidad(self, ingrediente, cantidad_agregar):
        ingrediente.cantidad -= cantidad_agregar
    

## Uso
#granocafe = Inventario(1, "Grano de Café", 100, "gramos")
#aguaPotable = Inventario(2, "Agua Potable", 5, "litros")
#azucar = Inventario(3, "Azúcar", 200, "gramos")
#harina = Inventario(6, "harina", 330, "gm")
#Chocolate = Inventario(5, "chocolate", 500, "l")
#
#cafe = Producto("Café", 25, "Café caliente", [(granocafe, 10), (aguaPotable, 0.5)], 50)
#pastel = Producto("Pastel", 50, "Pastel de chocolate", [(harina, 100), (Chocolate, 0.2)], 36)
#
#
#descafeiado = OpcionExtra("descafeinado", 0, granocafe, 0, "pues sin cafe XD", cafe)
#cafeextra = OpcionExtra("extra de cafe", 15, granocafe, 1.5, "pues con mas cafe XD", cafe)
#
#promo1=PromocionesPuntos("descuento 10%", "canjea 150 puntos por un 10 porciento de descuento en tu compra", "porcentaje", 0.10, 250)
#promo2=PromocionesPuntos("descuento de $20", "canjea 150 puntos por un 10 porciento de descuento en tu compra", "fijo", 20, 100)
#
#
##cliente = ClienteNoRegistrado()
##
### sintaxis: (producto, cantidad, extras)
##cliente.agregarAlPedido(cafe, 2, descafeiado)
##cliente.agregarAlPedido(pastel, 1)
##cliente.agregarAlPedido(cafe, 1, cafeextra)
#
#
#
## Hacer el pedido
##cliente.hacerPedido()
#
#Ernesto = ClienteRegistrado("Ernesto Velez Ortega", 2121, 2231176544, "netovelesz@gmail.com", 1000)
#Ernesto.agregarAlPedido(cafe, 1, descafeiado)
#Ernesto.agregarAlPedido(cafe, 2, cafeextra)
#Ernesto.agregarAlPedido(pastel, 5)
#Ernesto.agregarPromo(promo2)
#
#
#Ernestopromo = PromocionesPuntos.aplicarPromo(Ernesto, 355, promo2)
#precio= int(Ernesto.calcular_total_parcial())
#print(f"precio normal: {precio}, promocion: {Ernestopromo}, final{precio - Ernestopromo}")
#Ernesto.hacerPedido()
#
##print("Inventario antes del pedido:")
##Inventario.mostrar_inventario()
#
##print("\nInventario después del pedido:")
##Inventario.mostrar_inventario()
#
#
##Pedido.verPedidosPendientes()  # Esto imprimirá los pedidos pendientes sin None
#
#print(Ernesto.puntos_acumulados)