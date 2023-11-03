from BusquedasInView.Estructuras.EstructuraInterna import EstructuraInterna


class Secuencial(EstructuraInterna):
  def __init__(self, matriz,r,d):
    super().__init__(matriz,r,d)

  def busqueda(self,valor):
    accesos = 0
    for i in range(len(self.matriz)):
      if self.matriz[i] == valor:
        return "(Secuencial) la clave "+str(valor)+" se encontro en la direccion "+ str(i+1) + " tras "+str(accesos+1)+ " accesos"
      accesos += 1
    return "(Secuencial) la clave "+str(valor)+" no se encontro"
  
  def ingresarDato(self, valor):
    if(len(str(valor))>self.digitos):
      return "la clave supera la cantidad de digitos"
    if (len(self.matriz) < self.rango):
      if(valor in self.matriz):
        return "La clave "+str(valor)+" ya se encuentra en la estructura"
      self.matriz.append(valor)
      self.matriz.sort()
      return "Se ha ingresado la clave "+str(valor)+" con exito en la direccion "+str(self.matriz.index(valor)+1)
    else:
        return "La Estructura ya esta llena"
