from BusquedasInView.Estructuras.EstructuraInterna import EstructuraInterna


class Binario(EstructuraInterna):
    def __init__(self, matriz,r):
        super().__init__(matriz,r)

    def busqueda(self, valor):
        tamaño = len(self.matriz)
        mat = self.matriz
        while True:
            central = round(tamaño / 2) - 1
            if valor == mat[central]:
                return "(Binario) el registro numerico "+str(valor)+" se encontro en "+str(self.matriz.index(valor) + 1)
            elif valor < mat[central] and not tamaño <= 1:
                mat = mat[:central]
            elif valor > mat[central] and not tamaño <= 1:
                mat = mat[central + 1:]
            elif tamaño <= 1:
                return f"(Binario) el registro "+str(valor)+" no se encontro"
            tamaño = len(mat)

    def ingresarDato(self, valor):
        if (len(self.matriz) < self.rango):
            for x in range(len(self.matriz)):
                if self.matriz[x] == valor:
                    return "el registro ya se encuentra en la estructura"
                if self.matriz[x] > valor:
                    self.matriz.append(valor)
                    self.matriz = sorted(self.matriz)
                    return "el registro "+str(valor)+" ha sido ingresado con exito"
            self.matriz.append(valor)
            return "el registro "+str(valor)+" ha sido ingresado con exito al final"
        else:
            return "la estructura ya se encuentra llena"
