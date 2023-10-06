from BusquedasInView.Estructuras.EstructuraInterna import EstructuraInterna


class Secuencial(EstructuraInterna):
  def __init__(self, matriz,r):
    super.__init__(matriz,r)

  def busqueda(self,valor):
    for i in self.matriz:
      if i == valor:
        return "(Secuencial) el valor "+valor+" se encontro"
    return "(Secuencial) el valor "+valor+" no se encontro"
  
  def ingresarDato(self, valor):
    if (len(self.matriz) < self.rango):
      self.matriz.append(valor)
      return "Se ha ingresado la clave numerica "+valor+" se ha ingresado con exito"
    else:
        return "La Estructura ya esta llena"
