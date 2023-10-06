from BusquedasInView.Estructuras.EstructuraInterna import EstructuraInterna


class Binario(EstructuraInterna):
    def __init__(self, matriz,r):
        super().__init__(matriz,r)

    def busqueda(self, valor):
        tamaño = len(self.matriz)
        while True:
            central = round(tamaño / 2) - 1
            if valor == self.matriz[central]:
                return "(Binario) el registro numerico "+str(valor)+" se encontro en "+str(central+1)
            elif valor < self.matriz[central] and not tamaño <= 1:
                self.matriz = self.matriz[:central]
            elif valor > self.matriz[central] and not tamaño <= 1:
                self.matriz = self.matriz[central + 1:]
            elif tamaño <= 1:
                return f"(Binario) el registro "+str(valor)+" no se encontro"
            tamaño = len(self.matriz)

    def ingresarDato(self, valor):
        if (len(self.matriz) < self.rango):
            for x in range(len(self.matriz)):
                if self.matriz[x] == valor:
                    return "el registro ya se encuentra en la estructura"
                if self.matriz[x] > valor:
                    self.matriz.insert(x,valor)
                    return "el registro "+str(valor)+" ha sido ingresado con exito"
            self.matriz.append(valor)
            return "el registro "+str(valor)+" ha sido ingresado con exito al final"
        else:
            return "la estructura ya se encuentra llena"
