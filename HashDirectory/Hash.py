import math
import time

class TransfClaves():
  def solColiLineal(self, valorCol, posicion):
    recorrido = posicion
    origen = posicion
    save = True
    count = 0
    while save:
      count+=1
      if recorrido >= self.tamaño:
        recorrido = 0
      if recorrido == origen - 1:
        self.mError = "La estructura esta llena, no se pudo solucionar la colisión para la clave " + str(origen)
        save = False
        break
      if recorrido + 1 not in self.estructura:
        self.estructura[recorrido +1] = valorCol
        save = False
        recorrido = recorrido + 1
        self.mSolColision = "Se aplica el método de solución lineal. Se encuentra disponible la dirección de memoria " + str(recorrido) + " para la clave " + str(valorCol) + ". Se aplico el método de solución " + str(count) + " veces"
        break
      recorrido+=1

  def solColiCuadratica(self, valorCol, posicion):
    for i in range(0, self.tamaño):
      nuevaClave = posicion + (i + 1)**2
      if nuevaClave >= self.tamaño:
        nuevaClave = nuevaClave % self.tamaño

      if nuevaClave not in self.estructura:
        self.estructura[nuevaClave] = valorCol
        self.mSolColision = "Se aplica el método de solución cuadrática.  Se encuentra disponible la dirección de memoria " + str(nuevaClave) + " para la clave " + str(valorCol) + ". Último cálculo para encontrar la dirección: " + str(i+1) + "^2"
        return

    self.mError = ("No se encontro solución de colisión para la clave " + str(valorCol) + " usando el método cuadrático, se realizaron: " + str(self.tamaño) +
                   " calculos de solución sin resultados efectivos")

  def solColiDobleHash(self, valorCol, posicion):
    danterior = posicion
    d = posicion
    for i in range(0, self.tamaño):
      danterior = d
      d = ((d + 1) % self.tamaño) + 1
      if d not in self.estructura:
        self.estructura[d] = valorCol
        self.mSolColision = ("Se aplica el método de solución doble función hash. Se encuentra disponible la dirección de memoria " + str(d) + " para la clave " + str(valorCol) +
                             ". Se aplica la función H(" + str(danterior) + ") = ((" + str(
                  danterior) + " + 1) mod " + str(self.tamaño) + ") + 1")
        return
    self.mError = ("No se encontro solución de colisión para la clave " + str(
      valorCol) + " usando el método doble función hash, se realizaron: " + str(self.tamaño) +
                   " calculos de solución sin resultados efectivos")

    
  def ordenar(self):
    temp_estructura = {}
    claves = sorted(self.estructura.keys())
    for clave in claves:
      temp_estructura[clave] = self.estructura[clave]

    self.estructura = temp_estructura

  def obtenerClave(self,value):
    if (self.fn == "Mod"):
      clave = (value % self.tamaño) + 1
    elif (self.fn == "Cuadratico"):
      potencia = value**2
      init = (len(str(potencia))-1) // 2 if len(str(potencia)) %2 == 0 else len(str(potencia))//2
      claveTemp = str(potencia) [init:init + len(str(self.tamaño - 1))]
      clave = 1 if claveTemp == "" else int(claveTemp) + 1
    elif (self.fn == "Truncamiento"):
      init = len(str(self.tamaño)) - 1
      if init == 0:
        init += 1
      value_str = str(value)
      sub_strings = [
          int(digit) for i, digit in enumerate(value_str) if i % 2 == 0
      ]
      clave = int(''.join(str(num) for num in sub_strings)) + 1
    elif (self.fn == "Plegamiento"):
      init = len(str(self.tamaño)) - 1
      if init == 0:
        init += 1
      value_str = str(value)
      sub_strings = [
          value_str[i:i + init] for i in range(0, len(value_str), init)
      ]
      clave = sum(int(sub) for sub in sub_strings) + 1
      if clave > self.tamaño:
        clave = clave % (10**init)
    else:
        raise Exception("La función dada no es válida")
    return clave

  def ingresarValor(self, value):
    if (value in self.estructura.values()):
      self.mError = "la clave ya se encuentra en la estructura"
      return
    self.mIngreso = ""
    self.mError = ""
    self.mColision = ""
    self.mSolColision = ""
    clave = self.obtenerClave(value)

    if (len(self.estructura) < self.tamaño):
      if(clave in self.estructura):
        self.mColision = "La clave "+ str(value) + " presenta una colisión con la clave "+str(self.estructura.get(clave))+ " al intentar insertarla en la dirección de memoria "+str(clave)
        if self.colision == "Lineal":
          self.solColiLineal(value, clave)
        elif self.colision == "Cuadratico":
          self.solColiCuadratica(value, clave)
        elif self.colision == "Doble Hash":
           self.solColiDobleHash(value, clave)
          
      else:
        self.estructura[clave] = value
        self.mIngreso = "Se ha insertado exitosamente la clave "+str(value)+ " en la dirección de memoria "+str(clave)
    else:
      self.mError = "La estructura ya esta llena, no es posible insertar la clave " + str(value)
    self.ordenar()
  
  def __init__(self, funcion, tamaño, colision):
    self.tamaño = tamaño
    self.estructura = {}
    self.fn = funcion
    self.colision = colision

    self.mIngreso = ""
    self.mError = ""
    self.mColision = ""
    self.mSolColision = ""

  def buscarElemento(self,elemento):
    clave = self.obtenerClave(elemento)
    print("la clave de "+str(elemento)+" es "+str(clave))
    if(clave in self.estructura):
      if(self.estructura.get(clave) == elemento):
        return "La clave " + str(elemento)+" se encuentra en la estructura con la direccion "+str(clave)
      else:
        return "\033" +str(elemento)+" No esta en la estructura. La direccion " + str(clave)+" contiene a "+str(self.estructura.get(clave))+"\033"  
    else:
      return "\033"+"La estructura No contiene la clave " + str(clave)+"\033"