def ingresarValor(self, value):
    self.mIngreso = ""
    self.mError = ""
    self.mColision = ""
    self.mSolColision = ""
    clave = self.obtenerClave(value)

    if (len(self.estructura) < self.tamaño):
      if(clave in self.estructura):
        self.mColision = "El elemento "+ str(value) + " presenta una colision con "+str(self.estructura.get(clave))+ " al intentar guardarlo con la clave "+str(clave)
        if self.colision == "Lineal":
          self.solColiLineal(value, clave)
        elif self.colision == "Cuadratico":
          self.solColiCuadratica(value, clave)
        elif self.colision == "Doble Hash":
           self.solColiDobleHash(value, clave)
          
      else:
        self.estructura[clave] = value
        self.mIngreso = "se ha guardado exitosamente a "+str(value)+ " | clave: "+str(clave)
    else:
      self.mError = "La estructura ya esta llena, no se ha introducido " + str(value)
    self.ordenar()
