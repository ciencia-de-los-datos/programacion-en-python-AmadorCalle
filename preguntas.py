"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
with open("data.csv", "r") as file:
        data = file.readlines()
data = [line.replace("\n", "") for line in data]
data = [line.split("\t") for line in data]

def pregunta_01():

    suma = 0
    for i in range(0, len(data)):
        suma = suma + int(data[i][1])
    return suma


def pregunta_02():
    letras = ["A", "B", "C", "D", "E"]
    resultado = []
    suma1 = 0
    suma2 = 0
    suma3 = 0
    suma4 = 0
    suma5 = 0
    for i in range(0, len(data)):
        if data[i][0] == "A":
            suma1 = suma1 + 1
        if data[i][0] == "B":
            suma2 = suma2 + 1
        if data[i][0] == "C":
            suma3 = suma3 + 1
        if data[i][0] == "D":
            suma4 = suma4 + 1
        if data[i][0] == "E":
            suma5 = suma5 + 1
    sumas = [suma1, suma2, suma3, suma4, suma5]

    for j in range(0, len(sumas)):
        resultado.append((letras[j], sumas[j]))
    return resultado


def pregunta_03():
    letras = ["A", "B", "C", "D", "E"]
    resultado = []
    suma1 = 0
    suma2 = 0
    suma3 = 0
    suma4 = 0
    suma5 = 0
    for i in range(0, len(data)):
        if data[i][0] == "A":
            suma1 = suma1 + int(data[i][1])
        if data[i][0] == "B":
            suma2 = suma2 + int(data[i][1])
        if data[i][0] == "C":
            suma3 = suma3 + int(data[i][1])
        if data[i][0] == "D":
            suma4 = suma4 + int(data[i][1])
        if data[i][0] == "E":
            suma5 = suma5 + int(data[i][1])
    sumas = [suma1, suma2, suma3, suma4, suma5]

    for j in range(0, len(sumas)):
        resultado.append((letras[j], sumas[j]))
    return resultado


def pregunta_04():
    letras = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    resultado = []
    suma1 = 0
    suma2 = 0
    suma3 = 0
    suma4 = 0
    suma5 = 0
    suma6 = 0
    suma7 = 0
    suma8 = 0
    suma9 = 0
    suma10 = 0
    suma11 = 0
    suma12 = 0
    for i in range(0, len(data)):
        if data[i][2].find("-01-") != -1:
            suma1 = suma1 + 1
        if data[i][2].find("-02-") != -1:
            suma2 = suma2 + 1
        if data[i][2].find("-03-") != -1:
            suma3 = suma3 + 1
        if data[i][2].find("-04-") != -1:
            suma4 = suma4 + 1
        if data[i][2].find("-05-") != -1:
            suma5 = suma5 + 1
        if data[i][2].find("-06-") != -1:
            suma6 = suma6 + 1
        if data[i][2].find("-07-") != -1:
            suma7 = suma7 + 1
        if data[i][2].find("-08-") != -1:
            suma8 = suma8 + 1
        if data[i][2].find("-09-") != -1:
            suma9 = suma9 + 1
        if data[i][2].find("-10-") != -1:
            suma10 = suma10 + 1
        if data[i][2].find("-11-") != -1:
            suma11 = suma11 + 1
        if data[i][2].find("-12-") != -1:
            suma12 = suma12 + 1
    
    sumas = [suma1, suma2, suma3, suma4, suma5, suma6, suma7, suma8, suma9, suma10, suma11, suma12]

    for j in range(0, len(sumas)):
        resultado.append((letras[j], sumas[j]))    
    return resultado

def pregunta_05():
    letras = ["A", "B", "C", "D", "E"]
    resultado = []
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    for i in range(0, len(data)):
        if data[i][0] == "A":
            list1.append(int(data[i][1]))
        if data[i][0] == "B":
            list2.append(int(data[i][1]))
        if data[i][0] == "C":
            list3.append(int(data[i][1]))
        if data[i][0] == "D":
            list4.append(int(data[i][1]))
        if data[i][0] == "E":
            list5.append(int(data[i][1]))
    lista = [list1, list2, list3, list4, list5]

    for j in range(0, len(lista)):
        resultado.append((letras[j], max(lista[j]), min(lista[j])))
    return resultado

def pregunta_06():
    diccionarios = []
    for i in range(0, len(data)):
        diccionarios.append(data[i][4])

    diccionarios = [line.split(",") for line in diccionarios]

    listado = []
    for j in diccionarios:
        if type(j) == list:
            listado.extend(j)


    aaa = []
    bbb = []
    ccc = []
    ddd = []
    eee = []
    fff = []
    ggg = []
    hhh = []
    iii = []
    jjj = []

    for k in range(0, len(listado)):
        if listado[k][:3] == "aaa":
            aaa.append(int(listado[k][4:]))
        if listado[k][:3] == "bbb":
            bbb.append(int(listado[k][4:]))
        if listado[k][:3] == "ccc":
            ccc.append(int(listado[k][4:]))
        if listado[k][:3] == "ddd":
            ddd.append(int(listado[k][4:]))
        if listado[k][:3] == "eee":
            eee.append(int(listado[k][4:]))
        if listado[k][:3] == "fff":
            fff.append(int(listado[k][4:]))
        if listado[k][:3] == "ggg":
            ggg.append(int(listado[k][4:]))
        if listado[k][:3] == "hhh":
            hhh.append(int(listado[k][4:]))
        if listado[k][:3] == "iii":
            iii.append(int(listado[k][4:]))
        if listado[k][:3] == "jjj":
            jjj.append(int(listado[k][4:]))

    listas = [aaa, bbb, ccc, ddd, eee, fff, ggg, hhh, iii, jjj]
    listas_n = ["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg", "hhh", "iii", "jjj"]
    resultado = []
    for i in range(0, len(listas)):
        resultado.append((listas_n[i], min(listas[i]), max(listas[i])))
    return resultado


def pregunta_07():
    diccionario = {}

    for i in data:
        letra = i[0]
        numero = int(i[1])

        if numero in diccionario:
            diccionario[numero].append(letra)
        else:
            diccionario[numero] = [letra]

    resultado = sorted([(k, v) for k, v in diccionario.items()])
    return resultado

def pregunta_08():
    diccionario = {}

    for i in data:
        letra = i[0]
        numero = int(i[1])

        if numero in diccionario:
            diccionario[numero].append(letra)
        else:
            diccionario[numero] = [letra]
    parcial = sorted([(k, v) for k, v in diccionario.items()])

    resultado = list((t[0], sorted(list(dict.fromkeys(t[1])))) for t in parcial)
    return resultado


def pregunta_09():
    diccionario = {}
    for i in data:
        dict_ = {
            string.split(":")[0]: string.split(":")[1] for string in i[4].split(",")
        }
        for k, v in dict_.items():
            diccionario[k] = diccionario.get(k, 0) + 1
    diccionario = {k: v for k, v in sorted(diccionario.items(), key=lambda item: item[0])}

    return diccionario


def pregunta_10():
    lista_resultado = []
    for i in data:
        lista_resultado.append((
            i[0],
            len(i[3].split(',')),
            len(i[4].split(','))
        ))
    return lista_resultado


def pregunta_11():
    dic_resultado = {}
    for i in data:
        valor = int(i[1])
        letras = i[3].split(',')
        for letra in letras:
            if letra in dic_resultado.keys():
                dic_resultado[letra] += valor
            else:
                dic_resultado[letra] = valor
    resultado = sorted(dic_resultado.items(), key = lambda x: x[0])
    return resultado


def pregunta_12():
    dic_resultado = {}
    for i in data:
        if i[0] not in dic_resultado.keys():
            dic_resultado[i[0]] = 0
        letras = i[4].replace(':', ',').split(',')
        for letra in letras:
            if letra.isdigit():
                dic_resultado[i[0]] += int(letra)
    resultado = sorted(dic_resultado.items(), key = lambda x: x[0])
    return resultado
