from BusquedasInView.Estructuras.EstructuraInterna import EstructuraInterna


class Binario(EstructuraInterna):
    def __init__(self, matriz,r,d):
        super().__init__(matriz,r,d)

    def busqueda(self, valor):
        accesos = 0
        tamaño = len(self.matriz)
        mat = self.matriz
        while True:
            central = round(tamaño / 2) - 1
            if valor == mat[central]:
                return "(Binario) el registro numerico "+str(valor)+" se encontro en "+str(self.matriz.index(valor) + 1) + " tras "+str(accesos+1) + " accesos"
            elif valor < mat[central] and not tamaño <= 1:
                mat = mat[:central]
            elif valor > mat[central] and not tamaño <= 1:
                mat = mat[central + 1:]
            elif tamaño <= 1:
                return "(Binario) La clave "+str(valor)+" no se encontro"
            accesos += 1
            tamaño = len(mat)

    def ingresarDato(self, valor):
        if(len(str(valor))>self.digitos):
            return "la clave supera la cantidad de digitos"
        if (len(self.matriz) < self.rango):
            for x in range(len(self.matriz)):
                if self.matriz[x] == valor:
                    return "La clave ya se encuentra en la estructura"
                if self.matriz[x] > valor:
                    self.matriz.append(valor)
                    self.matriz = sorted(self.matriz)
                    return "La clave "+str(valor)+" ha sido ingresado con exito en la direccion " +str(self.matriz.index(valor) + 1)
            self.matriz.append(valor)
            return "La clave "+str(valor)+" ha sido ingresado en la direccion "+ str(self.matriz.index(valor) + 1)
        else:
            return "la estructura ya se encuentra llena"
