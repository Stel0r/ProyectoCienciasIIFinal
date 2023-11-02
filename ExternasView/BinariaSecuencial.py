class Secuencial:
  def __init__(self, matriz, numeroBloque, valor):
    self.matriz = matriz
    self.valor = valor
    self.numeroBloque = numeroBloque

  def busqueda(self):
    j = 0
    for i in self.matriz:
      if i == self.valor:
        return f"El registro {self.valor} se encontró en el bloque {self.numeroBloque} en la posición {j+1}"
      j += 1
    return f"El registro {self.valor} no se encontró"
  
class Binario:
    def __init__(self, matriz, numeroBloque, valor):
        self.matriz = matriz
        self.valor = valor
        self.numeroBloque = numeroBloque

    def busqueda(self):
        tamaño = len(self.matriz)
        while True:
            central = round(tamaño / 2) - 1
            if self.valor == self.matriz[central]:
                return f"El registro {self.valor} se encontró en el bloque {self.numeroBloque} en la posición {self.matriz.index(self.valor)+1}"
            elif self.valor < self.matriz[central] and not tamaño <= 1:
                self.matriz = self.matriz[:central]
            elif self.valor > self.matriz[central] and not tamaño <= 1:
                self.matriz = self.matriz[central + 1:]
            elif tamaño <= 1:
                return f"El registro {self.valor} no se encontró"

            tamaño = len(self.matriz)  

import math


def calcular_tamano_bloques(total_registros):
    tamano_bloque = math.ceil(math.sqrt(total_registros))
    return tamano_bloque


def guardar_en_bloques(datos, tamano_bloque):
    multilista = []
    bloque_actual = []

    datos.sort()

    for dato in datos:
        bloque_actual.append(dato)
        if len(bloque_actual) == tamano_bloque:
            multilista.append(bloque_actual)
            bloque_actual = []
    if bloque_actual:
        multilista.append(bloque_actual)
    return multilista


def busqueda_por_bloques(listas, clave):
    bloque_actual = 1

    for bloque in listas:
        ultimo_elemento = bloque[-1]

        if clave <= ultimo_elemento:
            return bloque, bloque_actual
        bloque_actual += 1
    return -1