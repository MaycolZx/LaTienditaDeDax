import matplotlib.pyplot as plt
from numpy import double
import time
import os

candidatos = []

usuarios = [
    {"username": "Dax", "password": "123456"},
    {"username": "Pedro", "password": "123456"},
    {"username": "Juan", "password": "123456"},
]

detail_InProduct = [
    {"productName": "papa", "price": 5, "cantidad": 100},
    {"productName": "leche", "price": 10, "cantidad": 200},
    {"productName": "naranja", "price": 20, "cantidad": 48},
    {"productName": "teclado", "price": 50, "cantidad": 50},
    {"productName": "pc", "price": 950, "cantidad": 84},
]

detail_popular_Venta = [
    {"categoria": "papa", "valor": 10},
    {"categoria": "leche", "valor": 20},
    {"categoria": "naranja", "valor": 15},
    {"categoria": "teclado", "valor": 25},
    {"categoria": "mainframe", "valor": 5},
]

detail_Client_Transaction = [
    {
        "nombre": "Pepito",
        "Productos": [
            {"productName": "papa", "cantidad": 5},
            {"productName": "naranja", "cantidad": 10},
        ],
    }
]

nombresCliente = ["Juan", "María", "Pedro"]
articulos = ["Leche", "Pan", "Huevos", "Queso"]
compras = [
    [1, 0, 1, 1],  # Juan compró Leche, Huevos y Queso
    [0, 1, 1, 0],  # María compró Pan y Huevos
    [1, 0, 0, 1],  # Pedro compró Leche y Queso
]


def debuggerPrint():
    print(detail_InProduct)


def billGenerator():
    print("Aqui tienes tu factura")


def diagramaCirculasPorcentage(clientName):
    objetos = ["Leche", "Pan", "Huevos", "Queso"]
    frecuencia = [25, 20, 30, 15]  # Porcentajes de frecuencia de compra
    colores = ["blue", "green", "orange", "red"]
    fig, ax = plt.subplots()
    ax.pie(frecuencia, labels=objetos, colors=colores, autopct="%1.1f%%", startangle=90)
    ax.legend(title="Objetos", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.title(f"Comportamiento del cliente {clientName}")
    plt.show()


# def dibujar_tabla(nombres, articulos, compras):
#     fig, ax = plt.subplots()
#     tabla = ax.table(
#         cellText=compras, rowLabels=nombres, colLabels=articulos, loc="center"
#     )
#     tabla.auto_set_font_size(False)
#     tabla.set_fontsize(12)
#     tabla.scale(1.5, 1.5)  # Ajustar tamaño de la tabla
#     ax.axis("off")
#     plt.show()


def showMeGraphicsPopular():
    categorias = [d["categoria"] for d in detail_popular_Venta]
    valores = [d["valor"] for d in detail_popular_Venta]
    plt.bar(categorias, valores)
    plt.xlabel("Productos")
    plt.ylabel("Cantidad")
    plt.title("Productos mas vendidos")
    plt.show()


def existProduct(valueSearch):
    contadorProductos = -1
    for productIterator in detail_InProduct:
        if (
            productIterator["productName"].upper() == valueSearch
            or productIterator["productName"].lower() == valueSearch
        ):
            print(
                f'Tenemos {productIterator["cantidad"]} de {productIterator["productName"]} a {productIterator["price"]}'
            )
            return contadorProductos + 1
        contadorProductos += 1
    contadorProductos = -1
    return contadorProductos


def main():
    # for i in usuarios:
    #     print(i)
    #
    # contador = 2
    # valorEncontrado = False
    # while contador >= 0:
    #     inputName = input("Username: ")
    #     inputPassword = input("Password: ")
    #     for userIterator in usuarios:
    #         if inputName == userIterator["username"]:
    #             if inputPassword == userIterator["password"]:
    #                 valorEncontrado = True
    #                 break
    #     if valorEncontrado:
    #         print(f"BIENVENIDO {inputName}")
    #         print("Autenticación exitosa. Bienvenido: ", nombre_usuario)
    #         # time.sleep(3) #Si queremos anadir un tiempo de espera al logearnos
    #         break
    #     print(
    #         f"Nombre de usuario o contrasena incorrectas.\nIntentos restantes-({contador})"
    #       print("Credenciales incorrectas. Intentos restantes:", intentos_restantes)
    #     )
    #     contador -= 1
    # if contador == -1:
    #     print("Se hicieron mas de 3 intentos")
    #   print("Ha excedido el número máximo de intentos. Acceso bloqueado.")
    #     return 0
    valorR_X = True
    while valorR_X:
        # print(
        #     "\n--------------------------------\nMENU PRINCIPAL\n1. REGISTRAR INGRESO DEL CLIENTE\n2. REGISTAR INGRESO DEL PRODUCTO\n3. REGISTRAR VENTA\n4. BUSCAR VENDEDOR/PRODUCTO\n5. REPORTES/GRAFICOS\n6. SALIR\n--------------------------------"
        # )
        print("\nSistema de Registro de Candidatos:")
        print("1. Registrar Candidato")
        print("2. Buscar Candidato por DNI")
        print("3. Generar Reporte")
        print("4. Generar Gráficos Estadísticos")
        print("5. Salir")
        opcionIn = int(input("Seleccione una opcion: "))
        os.system("clear")
        if opcionIN == 11:
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                dni = input("Ingrese el número de DNI: ")
                nombres = input("Ingrese los nombres del candidato: ")
                apellidos = input("Ingrese los apellidos del candidato: ")
                edad = int(input("Ingrese la edad del candidato: "))
                candidato = {
                    "DNI": dni,
                    "Nombres": nombres,
                    "Apellidos": apellidos,
                    "Edad": edad,
                }
                candidatos.append(candidato)
            else:
                if opcion == "2":
                    encontro = 0
                    dni = input("Ingrese el DNI del candidato a buscar: ")
                    for candidato in candidatos:
                        if candidato["DNI"] == dni:
                            print("Candidato encontrado:")
                            print("DNI:", candidato["DNI"])
                            print("Nombres:", candidato["Nombres"])
                            print("Apellidos:", candidato["Apellidos"])
                            print("Edad:", candidato["Edad"])
                            break
                        else:
                            print("Candidato no encontrado.")
                else:
                    if opcion == "3":
                        for candidato in candidatos:
                            print("DNI:", candidato["DNI"])
                            print("Nombres:", candidato["Nombres"])
                            print("Apellidos:", candidato["Apellidos"])
                            print("Edad:", candidato["Edad"])
                            print("-" * 50)
                    else:
                        if opcion == "4":
                            edades = [candidato["Edad"] for candidato in candidatos]

                            # Gráfico de edades
                            plt.hist(edades, bins=10)
                            plt.xlabel("Edad")
                            plt.ylabel("Cantidad")
                            plt.title("Distribución de Edades")
                            plt.show()

                        else:
                            if opcion == "5":
                                print("Saliendo del sistema. ¡Hasta luego!")
                                break
                            else:
                                print(
                                    "Opción no válida. Por favor, seleccione una opción válida."
                                )

        if opcionIn == 1:
            clientN = input("Ingresar el nombre del cliente: ")
            ingresoC = double(input("Ingreso del Cliente: "))

        if opcionIn == 2:
            valorSalida = True
            print("Producto #1 ...")
            while valorSalida:
                valorChange = False
                nombreProducto = input("Nombre del producto: ")
                iterProductList = existProduct(nombreProducto)
                if iterProductList != -1:
                    modCaract = input(
                        "El producto ya se encuentra registrado. Desea modificar su cantidad o precio ? N/Y: "
                    )
                    if modCaract == "Y" or modCaract == "y":
                        valorChange = True
                    else:
                        salidaF = input("Desea continuar? N/Y: ")
                        if salidaF == "N" or salidaF == "n":
                            valorSalida = False
                            continue
                        else:
                            continue
                precioProducto = double(input("Ingrese el precio: $"))
                if valorChange:
                    cantidadProducto = int(input("Cual es la nueva cantidad: "))
                    detail_InProduct[iterProductList]["price"] = precioProducto
                    detail_InProduct[iterProductList]["cantidad"] = cantidadProducto
                else:
                    cantidadProducto = int(input("Cuantos productos desea ingresar: "))
                    detail_InProduct.append(
                        {
                            "productName": nombreProducto,
                            "price": precioProducto,
                            "cantidad": cantidadProducto,
                        }
                    )
                valorSalidaChar = input("Desea seguir ingresado mas productos N/Y: ")
                if valorSalidaChar == "N" or valorSalidaChar == "n":
                    valorSalida = False

        if opcionIn == 3:
            pass

        if opcionIn == 4:
            valorSalida = True
            while valorSalida:
                valueSearch = input("Ingrese el nombre del producto o vendedor: ")
                valorDeBusqueda = existProduct(valueSearch)

                if valorDeBusqueda == -1:
                    print(
                        f"Nombre del producto ({valueSearch}) no encontrado. Vuelva a intentarlo"
                    )
                valorSalidaChar = input("Desea seguir buscando N/Y: ")
                if valorSalidaChar == "N" or valorSalidaChar == "n":
                    valorSalida = False

        if opcionIn == 5:
            print(
                "Seleccione ...\n1. Ventas por periodo\n2. Productos mas vendidos\n3. Comportamientos del cliente"
            )
            valorInDiagrama = int(input("La opcion es: "))
            if valorInDiagrama == 1:
                # dibujar_tabla(nombresCliente, articulos, compras)
                pass
            if valorInDiagrama == 2:
                showMeGraphicsPopular()
            if valorInDiagrama == 3:
                specificName = input("Ingrese el nombre del cliente: ")
                if specificName in nombresCliente:
                    diagramaCirculasPorcentage(specificName)
        if opcionIn == 6:
            valorR_X = False
        if opcionIn >= 7 or opcionIn <= 0:
            debuggerPrint()
            print("Ingrese una opcion valida por favor")
            continue


if __name__ == "__main__":
    main()
