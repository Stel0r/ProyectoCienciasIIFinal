from BusquedasInView.Estructuras.EstructuraInterna import EstructuraInterna


class Secuencial(EstructuraInterna):
  def __init__(self, matriz,r):
    super().__init__(matriz,r)

  def busqueda(self,valor):
    for i in range(len(self.matriz)):
      if self.matriz[i] == valor:
        return "(Secuencial) el registro "+str(valor)+" se encontro en "+ str(i+1)
    return "(Secuencial) el registro "+str(valor)+" no se encontro"
  
  def ingresarDato(self, valor):
    if (len(self.matriz) < self.rango):
      if(valor in self.matriz):
        return "El Registro "+str(valor)+" ya se encuentra en la estructura"
      self.matriz.append(valor)
      return "Se ha ingresado el registro "+str(valor)+" se ha ingresado con exito"
    else:
        return "La Estructura ya esta llena"
