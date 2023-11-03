from math import trunc
from ExternasView import CalculosDinamica as calculos

class Dinamicas:
  def __init__(self, cubetas, registros, pExpaxion, pReduccion, tipo):
      self.ListClaves = []
      self.StructureDinamic = []
      self.Cubetas = cubetas
      self.Registros = registros
      self.porExpasion = pExpaxion
      self.porReduccion = pReduccion
      self.Tipo = tipo
      self.event = False
      self.historico = []
      self.Process = ""
      # Varibles expasion y reduccion parcial
      self.anECubetas = 0
      self.anRCubetas = 0
      # Lista de Espera
      self.ListEspera = []

  def verifyCompleteData(self) -> bool:
      if self.Cubetas != 0 and self.Registros != 0 and self.porExpasion != 0 and self.porReduccion != 0:
          return True
      return False

  def verifyExistClave(self, Clave: int) -> bool:
      if Clave in self.ListClaves:
          return True
      return False

  def inicializateTable(self):
      self.StructureDinamic = [[0 for _ in range(self.Cubetas)]
                               for _ in range(self.Registros)]

  def insertClave(self, Clave: int):
      if Clave != 0:
          self.Process = ""
          self.ListClaves.append(Clave)
      self.inicializateTable()
      self.ListEspera = list(self.ListClaves)
      print(self.ListEspera)
      for key in self.ListClaves:
          index = calculos.hash_mod(key,len(self.StructureDinamic[0]))
          for row in self.StructureDinamic:
              space = row[index]
              if space == 0:
                  row[index] = key
                  self.Process = self.Process + "La Clave: " + str(key) + " fue ingresada a la cubeta: " + str(index) + "\n"
                  self.ListEspera.remove(key)
                  break
          else:
              self.Process = self.Process + "La Clave: " + str(key) + " no pudo ingresar a la cubeta: " + str(index)+ " ya que esta llena\n"
    
          if not self.event:
            self.historico = self.StructureDinamic
      print(self.ListEspera)
      if calculos.densidad_ocupacinal_expasion(self.StructureDinamic, len(self.ListClaves), self.porExpasion):
              self.event = True
              if self.Tipo == "Total":
                  self.expan_table_total()
              elif self.Tipo == "Parcial":
                  self.expan_table_parcial()
              self.insertClave(0)
              #break
      self.Process = self.Process + "Lista en espera: " + self.textEspera()

  def textEspera(self) -> str:
      return "[" + ",".join([str(i) for i in self.ListEspera]) +"]"


  def expan_table_total(self):
      self.Cubetas = self.Cubetas * 2
      self.Cubetas = int(self.Cubetas)
      self.inicializateTable()

  def expan_table_parcial(self):
      if self.Cubetas == self.anECubetas:
          self.anRCubetas = self.Cubetas * 2
          self.Cubetas = self.Cubetas + round(((self.Cubetas * 2) - self.Cubetas) / 2)
      else:
          self.Cubetas = self.Cubetas + round(((self.anECubetas * 2) - self.anECubetas) / 2)
          self.anECubetas = self.Cubetas
      self.Cubetas = int(self.Cubetas)
      self.inicializateTable()

  def deleteClave(self, Clave: int):
      self.Process = ""
      self.ListClaves.remove(Clave)
      self.Process = "Se Elimino la Clave: " + str(Clave) + "\n"
      self.insertClave(0)
      if calculos.densidad_ocupacinal_resuccion(self.Cubetas, self.ListClaves, self.porReduccion):
          if self.Tipo == "Total":
              self.reduc_table_total()
          elif self.Tipo == "Parcial":
              self.reduc_table_parcial();
          self.insertClave(0)

  def reduc_table_total(self):
      self.Cubetas = self.Cubetas / 2
      self.Cubetas = int(self.Cubetas)
      self.inicializateTable()

  def reduc_table_parcial(self):
      if self.Cubetas == self.anECubetas:
          self.anECubetas = self.Cubetas / 2
          self.Cubetas = self.Cubetas + round(((self.Cubetas / 2)) / 2)
      else:
          self.Cubetas = self.Cubetas + round(((self.anRCubetas / 2)) / 2)
          self.anRCubetas = self.Cubetas
      self.Cubetas = int(self.Cubetas)
      self.inicializateTable()

  def findClave(self, Clave: int):
      self.Process = ""
      if Clave not in self.ListClaves:
          self.Process = "La Clave: "+str(Clave)+" no esta en la estructura, ni en la lista de espera de alguna cubeta"
          return
      find = True
      for i in range(0, len(self.ListClaves)):
          if Clave in self.StructureDinamic[i]:
              find = False
              self.Process = "La Clave: " + str(Clave) + " Se encontro en la cubeta: " + str(self.StructureDinamic[i].index(Clave)) + ", en el Registro: " + str(i+1)  
              break
      if find:
          self.Process = "La Clave: "+str(Clave)+" no esta en la estructura, sino en la lista de espera de la cubeta: " + str(calculos.hash_mod(Clave, self.Cubetas))