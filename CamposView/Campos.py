class Campos:
    # variable global que va tener la informacion de las claves y 
    # las personas    
    # diccionario de la forma:
    # diccionario {
    #   clave: {
    #     "nombre":juan,
    #     "edad":12,
    #   },
    #   clave: {
    #     "nombre":carlos,
    #     "edad":34,
    #   },
    # }
    # (son diccionarios anidados)
    diccionario = {}

    def __init__(self):
        self.diccionario = {}

    # funciones que se hacen en el diccionario
    def insertar(self,clave,_nombre,_edad):
        if clave in self.diccionario.keys():
            return False
        entrada={}
        entrada['nombre']=_nombre
        entrada['edad']=_edad
        self.diccionario[clave]=entrada
        print("insertado")
        return True     

    def eliminar(self,clave):
         del self.diccionario[clave]
         return True 

    def obtener(self,clave):

        try:
            nombre=(self.diccionario.get(clave)).get('nombre')
            edad=str((self.diccionario.get(clave)).get('edad'))
            return "El registro encontrado con la clave "+ str(clave) +" ,es: "+ nombre + ", con edad de: "+ edad +" años."
        except Exception:
            return "El registro con la clave: " + str(clave)+" no fue encontrado."

    def reset(self):
        self.diccionario={}
        print("reseteado")

# pruebas
# campos = Campos()
# campos.insertar(12,"juan",23)
# print(campos.obtener(12))
# campos.eliminar(12)
# campos.reset()
# print(campos.obtener(12))