#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 20:41:12 2021

@author: martinademoor
"""

archivo_canciones = open("billboard.csv","r")

#FUNCION 1
def cargar_canciones(archivo_canciones)->list:
    canciones = []
    titulo = archivo_canciones.readline(). split(",")
    datos = archivo_canciones.readline().split(",")
    while len(datos)>1 and datos != " ":
        lista_cancion = {}
        lista_cancion["posicion"] = datos[0]
        lista_cancion["nombre_cancion"] = datos[1]
        lista_cancion["nombre_artista"] = datos[2]
        lista_cancion["anio"] = datos[3]
        lista_cancion["letra"] = datos[4]
        canciones.append(lista_cancion)
        datos = archivo_canciones.readline().split(",")
    
    return canciones

canciones = cargar_canciones(archivo_canciones)


#FUNCION 2
def buscar_cancion(canciones:list, nombre_cancion:str, anio:int)-> dict:
    dic_cancion = None

    for cancion in canciones:
        if cancion["nombre_cancion"] == nombre_cancion and int(cancion["anio"]) == anio:
            dic_cancion = cancion
    
    return dic_cancion

#FUNCION 3
def canciones_anio(canciones:list, anio:int)->list:
    canciones_en_anio = []

    for cancion in canciones:
        if cancion["anio"] == anio:
            del cancion["letra"]
            canciones_en_anio.append(cancion)
            
    return canciones_en_anio

#FUNCION 4
def canciones_artista_periodo(canciones:list,nombre_artista:str,anio_inicial:int,anio_final:int)->list:
    canciones_en_periodo = []
    for cancion in canciones:
        if cancion["nombre_artista"] == nombre_artista:
            if int(cancion["anio"]) >= anio_inicial and int(cancion["anio"]) <= anio_final:
                del cancion["letra"]
                canciones_en_periodo.append(cancion)
    
    return canciones_en_periodo

#FUNCION 5
def todas_canciones_artista(canciones:list, nombre_artista:str)->list:
    canciones_de_artista = []

    for cancion in canciones:
        if cancion["nombre_artista"] == nombre_artista:
            canciones_de_artista.append(cancion["nombre_cancion"])
    
    return canciones_de_artista


#FUNCION 6
def todos_artistas_cancion(canciones:list,nombre_cancion:str)->list:
    artistas_interpretes = []

    for cancion in canciones:
        if cancion["nombre_cancion"] == nombre_cancion:
            artistas_interpretes.append(cancion["nombre_artista"])


    return artistas_interpretes

#FUNCION 7
def artistas_mas_populares(canciones:list,min_canciones:int)->dict:
    artistas = {}

    for cancion in canciones:
        nombre = cancion["nombre_artista"]
        if nombre not in artistas:
            artistas[nombre] = 1
        else:
            artistas[nombre] += 1

    artistas_populares = {}

    for artista in artistas:
        if artistas[artista] >= min_canciones:
            artistas_populares[artista] = artistas[artista]

    return artistas_populares

#FUNCION 8
def artista_estrella(canciones:list)->dict:
    artistas = {}
    conteo_artista = 0
    
    for cancion in canciones:
        nombre = cancion["nombre_artista"]
        if nombre not in artistas:
            artistas[nombre] = 1
        else:
            artistas[nombre] += 1

    artista_estrella = {}
    max_canciones = 0
    max_artista = None

    for artista in artistas:
        if artistas[artista] > max_canciones:
            max_canciones = artistas[artista]
            max_artista = artista
    
    artista_estrella[max_artista] = max_canciones

    return artista_estrella

#FUNCION 9
def artistas_y_sus_canciones(canciones:list)->dict:
    artistas_y_canciones = {}

    for cancion in canciones:
        if cancion["nombre_artista"] not in artistas_y_canciones:
            artistas_y_canciones[cancion["nombre_artista"]] = [cancion["nombre_cancion"]]
        if cancion["nombre_artista"] in artistas_y_canciones and cancion["nombre_cancion"] not in artistas_y_canciones[cancion["nombre_artista"]]:
            artistas_y_canciones[cancion["nombre_artista"]] += [cancion["nombre_cancion"]]
    
    return artistas_y_canciones

#FUNCION 10
def promedio_canciones_por_artista(canciones:list)->float:
    listado_canciones = []
    listado_artistas = []
    conteo_canciones = 0
    conteo_artistas = 0

    for cancion in canciones:
        if cancion["nombre_cancion"] not in listado_canciones:
            conteo_canciones += 1
            listado_canciones.append(cancion["nombre_cancion"])
        if cancion["nombre_artista"] not in listado_artistas:
            conteo_artistas += 1
            listado_artistas.append(cancion["nombre_artista"])
    
    promedio = conteo_canciones / conteo_artistas
    
    return promedio

