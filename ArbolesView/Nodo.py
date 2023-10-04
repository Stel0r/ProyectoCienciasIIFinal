class Nodo:
    def __init__(self,value = ""):
        self.valor = value
        self.niveles = 0
        self.hijos:list[Nodo] = []
