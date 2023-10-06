from BusquedasInView.Estructuras.EstructuraInterna import EstructuraInterna


class Binario(EstructuraInterna):
    def __init__(self, matriz,r):
        super.__init__(matriz,r)

    def busqueda(self, valor):
        tamaño = len(self.matriz)
        while True:
            central = round(tamaño / 2) - 1
            if valor == self.matriz[central]:
                return "(Binario) la clave numerica "+valor+" se encontro"
            elif valor < self.matriz[central] and not tamaño <= 1:
                self.matriz = self.matriz[:central]
            elif self.valor > self.matriz[central] and not tamaño <= 1:
                self.matriz = self.matriz[central + 1:]
            elif tamaño <= 1:
                return f"(Binario) el valor "+valor+" no se encontro"
            tamaño = len(self.matriz)

    def ingresarDato(self, valor):
        if (len(self.matriz) < self.rango):
            for x in range(self.matriz):
                if self.matriz[x] == valor:
                    return "la clave numerica ya se encuentra en la estructura"
                if self.matriz[x] < valor:
                    self.matriz.insert(x,valor)
                    return "la clave "+valor+" ha sido ingresada con exito"
            self.matriz.append(valor)
        else:
            return "la estructura ya se encuentra llena"
