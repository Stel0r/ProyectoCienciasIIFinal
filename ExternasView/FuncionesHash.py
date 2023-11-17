class TransfClaves():

  def obtenerClave(self,value):
    if (self.fn == "Mod"):
      clave = (value % self.tamaño)
    elif (self.fn == "Cuadratico"):
      potencia = value**2
      init = (len(str(potencia))-1) // 2 if len(str(potencia)) %2 == 0 else len(str(potencia))//2
      claveTemp = str(potencia) [init:init + len(str(self.tamaño - 1))]
      clave = 1 if claveTemp == "" else int(claveTemp) + 1
    elif (self.fn == "Truncamiento"):
      posiciones = [i for i in range(1, len(str(value)) + 1, 2)]
      digitos = []
      str_key = str(value)

      for posicion in posiciones:
          if len(str(self.tamaño))-1 > len(digitos):
            digito = str_key[posicion - 1] if posicion - 1 < len(str_key) else '0'
            digitos.append(digito)

      nueva_key = int(''.join(digitos)) + 1
      clave = nueva_key
    elif (self.fn == "Plegamiento"):
      digitos_de_rango = len(str(self.tamaño)) - 1
      numeros_significativos = 1 if digitos_de_rango == 0 else digitos_de_rango

      str_key = str(value)
      digitos_de_key = len(str_key)
      suma_digitos = 0

      for i in range(0, digitos_de_key, numeros_significativos):
          suma_digitos += int(str_key[i:i + numeros_significativos])

      str_sum_digs = str(suma_digitos)

      if len(str_sum_digs) >= numeros_significativos + 1:
          suma_digitos = int(str_sum_digs[-numeros_significativos:])

      clave = suma_digitos + 1
    else:
        raise Exception("La Funcion Dada no es Valida")
    return clave

  
  def __init__(self, funcion, tamaño):
    self.tamaño = tamaño
    self.diccionario = [[] for _ in range(self.tamaño)]
    self.fn = funcion

  def ingresarValor(self, clave, dato):
    self.diccionario[clave].append(dato)

  def buscarElemento(self, clave):
    return self.diccionario[clave]