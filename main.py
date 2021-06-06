""" Reto 4 - Hagame la rebajita
    Yenifer Barco Castrillón
    Junio 06-2021 """

#---------------- Zona librerias------------

#==========================================================
#    Definicion de funciones(Dividir)
# =========================================================
def total_compra(telefonos, cantidades):
    """ 
    Parameters
    ----------
    telefonos:list
        lista con las marcas de telefonos a comprar
    cantidades:list
        lista con la cantidda de cajas de cada marca de telefono
    Return:
    -------
    total:float
        precio total de la compra sin descuento    
    """  
    #Listas con las marcas posibles y sus correspondientes precios
    lista_Marcas = ["Samsung","Xiaomi","Motorola","Huawei","Alcatel"]
    lista_Precio = [950,750,720,890,670]

    #Comprobando si las listas contienen datos
    if telefonos and cantidades:
        #Comparando si las dos listas tienen la misma longitud
        if len(telefonos) == len(cantidades):
            i = 0 #contador de lista marcas y precios
            j = 0 #contados de telefonos y cantidad
            total = 0

            #Ciclo para recorrer la lista de marcas
            for dispositivos in telefonos:
                j = 0 #contados de telefonos y cantidad
                for marcas in lista_Marcas:
                    #compara si el elemento de las listas se llama igual
                    if telefonos[i]==lista_Marcas[j]:
                        total_precio=lista_Precio[j]*cantidades[i]
                        total = total + total_precio
                        #print(lista_Precio[j],cantidades[i],total_precio,total)
                        #Aumento del contador
                    j+=1
                i+=1
        else:
            total = "Error"
    #Las listas estan vacias
    #else:
    #   print("Las listas se encuentran vacias")

    return total

def descuento(telefonos,cupon,total):
    """ 
    Parameters
    ----------
    telefonos:list
        lista con las marcas de telefonos a comprar
    cupon:string
        cupon de descuento
    total:float
        precio total de la compra sin descuento
    Return:
    -------
    total_desc:float
        precio total de la compra con el descuento    
    """         
    cupon_descuento="H5K986W"
    descuento=100
    #Contadores
    i=0
    j=0 #numero de dispositivos para aplicar el descuento
    
    #Si lista de telefonos no esta vacio
    if total!="Error":
        if cupon == cupon_descuento:
            for dispositivos in telefonos:
                if telefonos[i] == "Samsung" or telefonos[i]=="Motorola" and j<=2:
                    j+=1
                i+=1
            #cantidad de descuento a aplicar
            cant_descuento=descuento*j

            #precio total con el descuento
            total_desc=total-cant_descuento
        else:
            total_desc="Cupón inválido"
    else:
        total_desc=""

    return total_desc

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

#Test
telefonos = ["Samsung","Huawei","Motorola","Alcatel"]
cantidades = [2,1,1,1]
cupon="H5K9864"
total = total_compra(telefonos,cantidades)
print(total)
total_desc = descuento(telefonos,cupon,total)
print(total_desc)