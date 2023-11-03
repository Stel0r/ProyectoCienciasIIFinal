class TransfClaves():

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