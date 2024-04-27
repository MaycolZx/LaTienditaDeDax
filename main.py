import matplotlib.pyplot as plt
from numpy import double
import time
import os

usuarios = [
    {"username": "Dax", "password": "123456"},
    {"username": "Pedro", "password": "123456"},
    {"username": "Juan", "password": "123456"},
]

detail_InProduct = [
    {"productName": "papa", "price": 5, "cantidad": 100, "popularV": 0},
    {"productName": "leche", "price": 10, "cantidad": 200, "popularV": 0},
    {"productName": "naranja", "price": 20, "cantidad": 48, "popularV": 0},
    {"productName": "teclado", "price": 50, "cantidad": 50, "popularV": 0},
    {"productName": "pc", "price": 950, "cantidad": 84, "popularV": 0},
]
detail_Client_Transaction = []

# detail_Client_Transaction = [
#     {
#         "nombre": "Pepito",
#         "earning": 10
#         "Productos": [
#             {"productName": "papa", "cantidad": 5},
#             {"productName": "naranja", "cantidad": 10},
#         ],
#     }
# ]

nombresCliente = ["Juan", "María", "Pedro"]
articulos = ["Leche", "Pan", "Huevos", "Queso"]
compras = [
    [1, 0, 1, 1],  # Juan compró Leche, Huevos y Queso
    [0, 1, 1, 0],  # María compró Pan y Huevos
    [1, 0, 0, 1],  # Pedro compró Leche y Queso
]


def diagramaCirculasPorcentage(clientName, conteoIter):
    # objetos = ["Leche", "Pan", "Huevos", "Queso"]
    objetos = []
    objListCant = []
    for i in conteoIter:
        for j in detail_Client_Transaction[i]["productos"]:
            objetos.append(j["productName"])
            objListCant.append(
                {"productName": j["productName"], "cantidad": j["cantidad"]}
            )
    objetos = list(set(objetos))
    # frecuencia = [25, 20, 30, 15]
    frecuencia = []
    for i in objetos:
        frecuencia.append(0)
    for i in objListCant:
        if i["productName"] in objetos:
            indiceIter = objetos.index(i["productName"])
            frecuencia[indiceIter] += i["cantidad"]
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
    categorias = [d["productName"] for d in detail_InProduct]
    valores = [d["popularV"] for d in detail_InProduct]
    plt.bar(categorias, valores)
    plt.xlabel("Productos")
    plt.ylabel("Cantidad")
    plt.title("Productos mas vendidos")
    plt.show()


def existProduct(valueSearch, dInProduct):
    contadorProductos = -1
    for productIterator in dInProduct:
        if (
            productIterator["productName"].upper() == valueSearch
            or productIterator["productName"].lower() == valueSearch
        ):
            print(
                f'Tenemos {productIterator["cantidad"]} de {productIterator["productName"]}'
            )
            return contadorProductos + 1
        contadorProductos += 1
    contadorProductos = -1
    return contadorProductos


def addAltNewProduct():
    valorSalida = True
    print("Producto #1 ...")
    while valorSalida:
        valorChange = False
        nombreProducto = input("Nombre del producto: ")
        iterProductList = existProduct(nombreProducto, detail_InProduct)
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


def quitarDelCarrito(valorTmp):
    valueContinue = True
    while valueContinue:
        nombreProductoR = input("Ingrese el nombre del producto que desea retirar: ")
        iterExistP = existProduct(nombreProductoR, valorTmp)
        if iterExistP == -1:
            print("Porfavor ingrese el nombre del producto correctamente")
            continue
        cantidadProductoR = int(
            input(f"Ingrese la cantidad de {nombreProductoR} que desea retirar: ")
        )
        if cantidadProductoR > valorTmp[iterExistP]["cantidad"]:
            print(
                "Por favor ingrese una cantidad valida dentro del rango establecido en su carrito."
            )
            continue
        if cantidadProductoR == valorTmp[iterExistP]["cantidad"]:
            del valorTmp[iterExistP]
        else:
            valorTmpProducto = (
                valorTmp[iterExistP + 1]["cantMonetaria"]
                / valorTmp[iterExistP + 1]["cantidad"]
            )
            valorTmp[iterExistP + 1]["cantMonetaria"] -= (
                valorTmpProducto * cantidadProductoR
            )
            valorTmp[iterExistP + 1]["cantidad"] -= cantidadProductoR

        followR = input("Desea seguir retirando? N/Y: ")
        if followR == "N" or followR == "n":
            valueContinue = False


def main():
    for i in usuarios:
        print(i)

    contador = 2
    valorEncontrado = False
    while contador >= 0:
        inputName = input("Username: ")
        inputPassword = input("Password: ")
        for userIterator in usuarios:
            if inputName == userIterator["username"]:
                if inputPassword == userIterator["password"]:
                    valorEncontrado = True
                    break
        if valorEncontrado:
            # print(f"BIENVENIDO {inputName}")
            print("Autenticación exitosa. Bienvenido: ", inputName)
            # time.sleep(3) #Si queremos anadir un tiempo de espera al logearnos
            break
        # print(
        #     f"Nombre de usuario o contrasena incorrectas.\nIntentos restantes-({contador})"
        # )
        print("Credenciales incorrectas. Intentos restantes:", contador)
        contador -= 1
    if contador == -1:
        # print("Se hicieron mas de 3 intentos")
        print("Ha excedido el número máximo de intentos. Acceso bloqueado.")
        return 0

    valorR_X = True
    clientTmp = {"customerName": "none", "earning": 0}
    # productTmp = [{"productName": "none", "cantidad": 0, "cantMonetaria": 0}]
    productTmp = []

    while valorR_X:
        print(
            "\n--------------------------------\nMENU PRINCIPAL\n1. REGISTRAR INGRESO DEL CLIENTE\n2. REGISTAR INGRESO DEL PRODUCTO\n3. REGISTRAR VENTA\n4. BUSCAR VENDEDOR/PRODUCTO\n5. REPORTES/GRAFICOS\n6. SALIR\n--------------------------------"
        )
        opcionIn = int(input("Seleccione una opcion: "))
        os.system("clear")

        if opcionIn == 1:
            clientN = input("Ingresar el nombre del cliente: ")
            ingresoC = double(input("Ingreso del Cliente: "))
            clientTmp["customerName"] = clientN
            clientTmp["earning"] = ingresoC

        if opcionIn == 2:
            print("El inventario es: \n")
            for i in detail_InProduct:
                print(f'Hay {i["cantidad"]} de {i["productName"]} a ${i["price"]}')
            valueContinue = True
            while valueContinue:
                nombreBP = input("Ingrese el nombre producto: ")
                nombreBP_exist = existProduct(nombreBP, detail_InProduct)
                nombreBP_e_Save = existProduct(nombreBP, productTmp)
                if nombreBP_exist == -1:
                    print(
                        "El nombre del producto no existe. Por favor vuelva a intentarlo"
                    )
                    continue
                cantidadBP = int(input("Cuantos desea llevar: "))
                if cantidadBP > detail_InProduct[nombreBP_exist]["cantidad"]:
                    print(
                        "La cantidad que usted quiere excede al numero almacenado en la Tienda. Vuelva a intentarlo."
                    )
                    continue
                detail_InProduct[nombreBP_exist]["cantidad"] -= cantidadBP
                detail_InProduct[nombreBP_exist]["popularV"] += cantidadBP
                cantMonetaria = cantidadBP * detail_InProduct[nombreBP_exist]["price"]
                if nombreBP_e_Save != -1:
                    productTmp[nombreBP_e_Save]["cantidad"] += cantidadBP
                    productTmp[nombreBP_e_Save]["cantMonetaria"] += cantMonetaria
                else:
                    productTmp.append(
                        {
                            "productName": nombreBP,
                            "cantidad": cantidadBP,
                            "cantMonetaria": cantMonetaria,
                        }
                    )
                valorSalidaChar = input("Desea continuar N/Y: ")
                if valorSalidaChar == "N" or valorSalidaChar == "n":
                    valueContinue = False

        if opcionIn == 3:
            valueContinue = True
            while valueContinue:
                print(f"Carrito del sr.{clientTmp['customerName']}")
                cantidadTotalC = 0
                for i in productTmp:
                    cantidadTotalC += i["cantMonetaria"]
                    print(
                        f"{i['productName']} x{i['cantidad']}\t\t=\t${i['cantMonetaria']}\n"
                    )
                print(f"Cantidad Total: ${cantidadTotalC}")
                print(f"Cantidad ingresada al inicio: ${clientTmp['earning']}")
                diferenciaInicial = clientTmp["earning"] - cantidadTotalC
                if diferenciaInicial < 0:
                    print(
                        f"Para completar la compra se necesita + ${-1*diferenciaInicial}."
                    )
                    wannaAument = input("Desea aumentar la direrencia? N/Y: ")
                    if wannaAument == "N" or wannaAument == "n":
                        print(
                            "Por favor retire algunos productos del carrito para continuar con la compra."
                        )
                        quitarDelCarrito(productTmp)
                        continue
                    else:
                        clientTmp["earning"] += -1 * diferenciaInicial
                else:
                    valorSalidaChar = input("Desea finalizar con la comprar ? N/Y: ")
                    if valorSalidaChar == "N" or valorSalidaChar == "n":
                        print(
                            "Desea ...\n[1] - Modificar el carrito\n[2] - Cancelar la compra\n[3] - Finalizar la compra"
                        )
                        cancelOcontinue = int(input("Elija una opcion: "))
                        if cancelOcontinue == 1:
                            print(
                                "Aqui se anadira una funcion para agregar o quitar cosas del carrito. Coming soon ."
                            )
                        if cancelOcontinue == 2:
                            clientTmp = {"customerName": "none", "earning": 0}
                            productTmp = []
                            print("Gracias por visita.")
                            break
                        if cancelOcontinue == 3:
                            print(
                                f"Su cambio es de {diferenciaInicial}. Gracias por su compra"
                            )
                            print("Generando Factura ...")
                            detail_Client_Transaction.append(
                                {
                                    "nombreC": clientTmp["customerName"],
                                    "earningC": clientTmp["earning"]
                                    + diferenciaInicial,
                                    "productos": productTmp,
                                }
                            )
                            # Limpiar
                            clientTmp = {"customerName": "none", "earning": 0}
                            productTmp = []

                            valueContinue = False

                    else:
                        print(
                            f"Su cambio es de {diferenciaInicial}. Gracias por su compra"
                        )
                        print("Generando Factura ...")
                        valueContinue = False
                        detail_Client_Transaction.append(
                            {
                                "nombreC": clientTmp["customerName"],
                                "earningC": clientTmp["earning"] + diferenciaInicial,
                                "productos": productTmp,
                            }
                        )
                        clientTmp = {"customerName": "none", "earning": 0}
                        productTmp = [
                            {
                                "productName": "none",
                                "cantidad": 0,
                                "cantMonetaria": 0,
                            }
                        ]

        if opcionIn == 4:
            valorSalida = True
            while valorSalida:
                valueSearch = input("Ingrese el nombre del producto o vendedor: ")
                valorDeBusqueda = existProduct(valueSearch, detail_InProduct)

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
                print(detail_Client_Transaction)
                pass
            if valorInDiagrama == 2:
                showMeGraphicsPopular()
            if valorInDiagrama == 3:
                salidaF = True
                while salidaF:
                    specificName = input("Ingrese el nombre del cliente: ")
                    listContIter = []
                    conteoIter = 0
                    for iterClient in detail_Client_Transaction:
                        if specificName in iterClient["nombreC"]:
                            listContIter.append(conteoIter)
                        conteoIter += 1
                    if listContIter != []:
                        diagramaCirculasPorcentage(specificName, listContIter)
                    else:
                        print("Nombre de usuario incorrecto. Pruebe con otro nombre")
                    valorSalidaChar = input(
                        "Desea ver el diagrama de otro cliente? N/Y: "
                    )
                    if valorSalidaChar == "N" or valorSalidaChar == "n":
                        salidaF = False
        if opcionIn == 6:
            valorR_X = False
        if opcionIn >= 7 or opcionIn <= 0:
            print("Ingrese una opcion valida por favor")
            continue


if __name__ == "__main__":
    main()
