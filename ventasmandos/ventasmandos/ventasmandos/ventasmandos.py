import os
os.system("cls")        #id facil 
import pyfiglet

mandos =[]
carrito=[]
ventas = []


script_dir = os.path.dirname(__file__)
mandos_file = os.path.join(script_dir, "mandos.txt")
ventasprod_file = os.path.join(script_dir, "ventasprod.txt")


def mostrar_menu1():
    print("\n--- Menu Principal ---")
    print("1. ventas")
    print("2. reportes")                                              
    print("3. mantenedores")
    print("4. administrador")
    print("5. salir")
    opcion = input("seleccione una opcion: ")
    return opcion
   
def mostrar_menu():
    print("\n---- Menu de ventas ---")
    print("1. mostrar mandos disponibles")
    print("2. agregar mando al carrito")
    print("3. mostrar carrito")
    print("4. borrar elemento del carrito")
    print("5. pasar a la compra")
    print("6. regresar")
    opcion = input("seleccione una opcion: ")
    return opcion

def venta_por_fecha_especifica():
    fecha = input("Ingrese la fecha (formato: DD-MM-AAAA): ")
    ventas_fecha = [venta for venta in ventas if venta[1] == fecha]
    total_ventas = sum(venta[2] for venta in ventas_fecha)
    print(f"El total de ventas para la fecha {fecha} es: {total_ventas}")
    


def venta_por_rango_de_fechas():
    fecha_inicio = input("Ingrese la fecha de inicio (formato: DD-MM-AAAA): ")
    fecha_fin = input("Ingrese la fecha de fin (formato: DD-MM-AAAA): ")
    ventas_rango = [venta for venta in ventas if fecha_inicio <= fecha_fin]
    total_ventas = sum(venta[2] for venta in ventas_rango)
    print(f"El total de ventas para el rango de fechas {fecha_inicio} - {fecha_fin} es: {total_ventas}")


def mostrar_mandos():
    print("\n--- mandos disponibles---")
    if mandos:
        for mando in mandos:
            print(f"id: {mando[0]}, nombre: {mando[1]}, cantidad: {mando[2]}, precio: {mando[3]}")
    else:
        print("no hay mandos disponibles")
    
        
def agregar_al_carrito():
    id_mando = input("Ingresa el ID del mando para agregar al carrito: ")
    cantidad = int(input("Ingresa la cantidad de mandos que deseas: "))
    
    encontrado = False
    
    for mando in mandos:
        if mando[0] == id_mando:
            encontrado = True
            if cantidad <= mando[2]:
                carrito.append([mando[1], cantidad, mando[3]])
                mando[2] -= cantidad
                print(f"Se agregaron {cantidad} {mando[1]}(s) al carrito.")
            else:
                print("Cantidad no disponible")
            break
    
    if not encontrado:
        print("Mando no encontrado")
    
    
def mostrar_carrito():
    print("\n---- Carrito de compras ----")
    if not carrito:
        print("el carrito esta vacio.")
    else:
        total = 0
        for item in carrito:
            precio_total = item[1] * item[2]
            total += precio_total
            print(f"Nombre: {item[0]}, Cantidad: {item[1]}, Precio unitario: {item[2]}, Total: {item[1] * item[2]}")
        print(f"total a pagar: {total}")
            
def borrar_del_carrito():
    nombre_mando=input("ingrese el nombre del mando a borrar del carrito: ")
    cantidad= int(input("ingresa la cantidad a borrar: "))

    for item in carrito:
        if item[0] == nombre_mando:
            if cantidad <= item[1]:
                item[1] -= cantidad
                if item[1] ==0:
                    carrito.remove(item)
                for mando in mandos:
                    if mando[1] == nombre_mando:
                        mando[2] += cantidad
                        break
                print(f"se eliminaron {cantidad} {nombre_mando} del carrito")
            else:
                print("cantidad a borrar no disponible en el carrito ")
                    
            
def pasar_a_la_compra():
    total = sum(item[1] * item[2] for item in carrito)
    if total == 0:
        print("no hay articulos en el carrito")
    else:
        print(f"\nel total a pagar es: {total}")
        confirmar = input("desea realizar la compra? (S/N):").upper()
        if confirmar == "S":
            id_venta=len(ventas) + 1
            fecha=input("ingresa la fecha de la venta (FORMATO DD-MM-AAAA): ")
            ventas.append([id_venta, fecha, total]+[item for sublist in carrito for item in sublist])

            carrito.clear()
            print("Gracias por su compra!")
        else:
            print("compra cancelada")
    
def buscar_mandos(mando_id):
    for i in range(len(mandos)):
        if mandos[i][0]==mando_id:
            return i
    return -1


def reportar_ventas():
    total_ventas = sum(venta[2] for venta in ventas)
    print(f"el total de ventas general es: {total_ventas}")


def mando_ordenado(id, nombre, stock, precio):
    for i in range(len(mandos)):
        if mandos[i][0] > id:
            mandos.insert(i, [id, nombre, stock, precio])
            return
    mandos.append([id, nombre, stock, precio])



def validar_id():
    return len(id)==4

def validar_cantidad(cantidad, stock):
    return cantidad > 0 and cantidad <= stock


def validar_respuesta(respuesta):
    return respuesta.lower() in ["s", "n"]


def validar_datos_ventas(id, cantidad, stock, respuesta):
    if not validar_id(id):
        print("ID debe tener largo de 4.")
        return False
    if not validar_cantidad(cantidad, stock):
        print("cantidad debe ser mayor que 0 y menor o igual al stock")
        return False
    if not validar_respuesta(respuesta): 
        print("respuesta debe ser 's' o 'n'.")
        return False
    return True




def validar_fecha(fecha):
    if len(fecha) != 10:
        return False
    try:
        dia, mes, año= map(int, fecha.split('-'))
        if not (1 <= dia <= 31 and 1 <= mes <= 12 and año > 2000):
            return False
        if mes == 2:
            if (año % 4 == 0 and año % 100 !=0) or (año % 400 == 0):
                return dia <= 29
            return dia <= 28
        if mes in [4, 6, 9, 11]:
            return dia <= 30
        return dia <= 31
    except ValueError:
        return False
    

def validar_datos_reportes(fecha_inicio, fecha_termino):
    if not validar_fecha(fecha_inicio):
        print("fecha de inicio no es valido")
        return False
    if not validar_fecha(fecha_termino):
        print("fecha de termino no es valida")
        return False
    return True



def validar_nombre(nombre):
    return len(nombre.strip()) > 0

def validar_stock(stock):
    return stock >=0

def validar_precio(precio):
    return precio >= 0

def validar_datos_producto(id, nombre, stock, precio):
    if not validar_id(id):
        print("ID debe tener largo de 4")
        return False
    if not validar_nombre(nombre):
        print("el nombre no debe estar vacio ")
        return False
    if not validar_stock(stock):
        print("el stock debe ser mayor o igual que 0")
        return False
    if not validar_precio(precio):
        print(" el precio debe ser mayor o igual que 0")
        return False
    return True






def cargar_datos():
    try:
        with open(mandos_file, "r") as file:
            for line in file:
                id, nombre, stock, precio = map(str.strip, line.split(","))
                mandos.append([id, nombre, int(stock), int(precio)])
        print("Datos de mandos cargados exitosamente.")
        print("mandos disponibles")
        mostrar_mandos()
    except FileNotFoundError:
        print("El archivo mandos.txt no se encontró.")
    except Exception as e:
        print(f"Error al cargar datos de mandos: {e}")

    try:
        with open(ventasprod_file, "r") as file:
            for line in file:
                datos = line.strip().split(", ")
                id_venta = int(datos[0])
                fecha = datos[1]
                total_venta = int(datos[2])
                ventas.append([id_venta, fecha, total_venta] + datos[3:])
        print("datos de ventas cargados exitosamente")
    except FileNotFoundError:
        print("el archivo ventasprod.txt no se encontro")
    except Exception as e:
        print(f"error al cargar datos de ventas: {e}")

def respaldar_datos():
    try:
        with open("productos.txt", "w") as file:
            for mando in mandos:
                file.write(", ".join(map(str, mando)) + "\n")
        print("Datos de productos respaldados exitosamente.")
    except Exception as e:
        print(f"Error al respaldar productos: {e}")

    try:
        with open("ventasprod.txt", "w") as file:
            for venta in ventas:
                file.write(", ".join(map(str, venta[:3])) + ", " + ", ".join(map(str, venta[3:])) + "\n")
        print("Datos de ventas respaldados exitosamente.")
    except Exception as e:
        print(f"Error al respaldar ventas: {e}")


def mostrar_menu_administrador():
    print("\n--- Menu Administrador ---")
    print("1. cargar datos")
    print("2. respaldar datos (grabar actualizar)")
    print("3. salir")
    opcion = input("seleccione una opcion: ")
    return opcion

print(pyfiglet.figlet_format("Venta de Mandos"))
print("""Aaron Galaz
Diego Navarrete
      """)

os.system("pause")

cargar_datos()

while True:
    opcion= mostrar_menu1()
    match opcion:
        case "1":
            while True:
                opcion = mostrar_menu()
                match opcion:
                    case "1":
                        mostrar_mandos()
                    case "2":
                        id_mando=input("ingrese el id del mando: ")
                        cantidad=int(input("ingrese la cantidad de mandos que deseas: "))
                        respuesta= input("confirma la operacion (s/n): ")
                        for mando in mandos:
                            if mando[0] == id_mando:
                                if validar_datos_ventas(id_mando, cantidad, mando[2], respuesta):
                                    carrito.append([mando[1], cantidad, mando[3]])
                                    mando[2] -= cantidad
                                    print(f"se agregaron {cantidad} {mando[1]}(s) al carrito")
                                else:
                                    print("datos invalidos, intente de nuevo")
                                break
                            else:
                                print("mando no encontrado")
                    case "3":
                        mostrar_carrito()
                    case "4":
                        borrar_del_carrito()
                    case "5":
                        pasar_a_la_compra()
                    case "6":
                        break
                    case _:
                        print("Opcion no valida, seleccione una correcta porfavor.")
                        
        case "2":
            print("\n--- Reporteando ---")
            while True:
                print("""   REPORTES 
                      ----------------------
                      1. general de ventas (con total)
                      2.venta por fecha especifica (con total)
                      3.venta por rango de fecha (con total)
                      4.sair al menú principal
                      """)
                op=int(input("ingrese una opcion 1-4: "))
                match op:
                    case 1: 
                        reportar_ventas()
                    case 2:
                        fecha = input("ingresa la fecha de (formato: DD-MM-AAAA): ")
                        if validar_fecha(fecha):
                            venta_por_fecha_especifica(fecha)
                        else:
                            print("fecha no valida")
                    case 3:
                        fecha_inicio = input("ingrese la fecha de inicio(formato: DD-MM-AAAA): ")
                        fecha_fin = input("ingrese la fecha de fin(formato: DD-MM-AAAA): ")
                        if validar_datos_reportes(fecha_inicio, fecha_fin):
                            venta_por_rango_de_fechas(fecha_inicio, fecha_fin)
                        else:
                            print("fechas no validas")
                    case 4:
                        break
                    case _:
                        print("error")
                    
        case "3":
            print("\n--- Mantenedores ---")
            while True:
                print("""
                    1. Agregar
                    2. Buscar
                    3. Eliminar
                    4. Modificar
                    5. Listar
                    6. Regresar al menu principal
                    """)
                op = int(input("Ingrese la opción: "))
                match op:
                    case 1:
                        id=input("ingrese ID: ")
                        nombre=input("ingrese el nombre: ")
                        stock=int(input("ingrese stock: "))
                        precio=int(input("ingrese precio: "))
                        if validar_datos_producto(id, nombre, stock, precio):
                            mando_ordenado(id, nombre, stock, precio)
                            print("mando agregado exitosamente.")
                        else:
                            print("datos del producto no son validos")
                    case 2:
                        id=input("ingrese ID del mando: ")
                        posicion =buscar_mandos(id)
                        if posicion != -1:
                            mando = mandos[posicion]
                            print(f"ID: {mando[0]}, nombre: {mando[1]}, stock: {mando[2]}, precio: {mando[3]}")
                        else:
                            print("error, mando no existe.")
                    case 3:
                        id=input("ingrese ID del mando a eliminar: ")
                        posicion=buscar_mandos(id)
                        if posicion != -1:
                            mandos.pop(posicion)
                            print("mando eliminado exitosamente")
                        else:
                            print("error, mando no encontrado.")
                    case 4:
                        id=input("ingrese ID del mando a modificar: ")
                        posicion=buscar_mandos(id)
                        if posicion != -1:
                            nuevo_nombre=input("ingrese nuevo nombre: ")
                            nuevo_stock=int(input("ingrese nuevo stck:"))
                            nuevo_precio=int(input("ingrese nuevo precio: "))
                            if validar_datos_producto(id, nuevo_nombre, nuevo_stock, nuevo_precio):
                                mandos[posicion] = [id, nuevo_nombre, nuevo_stock, nuevo_precio]
                                print("mando modificado exitosamente")
                            else:
                                print("datos del producto no son validos")
                        else:
                            print("error, mando no existe.") 
                    case 5:
                        print("\n--- lista de mandos ---")
                        for mando in mandos:
                            print(f"ID: {mando[0]}, nombre: {mando[1]}, stock: {mando[2]}, precio: {mando[3]}")
                    case 6:
                        break
                    case _:
                        print("opcion no valida")
        case "4":
            while True:
                opcion = mostrar_menu_administrador()
                if opcion == "1":
                    cargar_datos()
                elif opcion == "2":
                    respaldar_datos()
                elif opcion == "3":
                    break
                else:
                    print("Opción no válida")
        case "5":
            print("saliendo del menu")
            break
        case _:
            print("Opcion no valida, seleccione una correcta porfavor.")