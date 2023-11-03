def densidad_ocupacinal_expasion(estructura, listaDatos, porcentaje):
  total_espacios = sum(len(cubeta) for cubeta in estructura)
  total_espacios_ocupados = listaDatos
  if (total_espacios_ocupados / total_espacios) * 100 >= porcentaje:
      return True
  else:
      return False

def densidad_ocupacinal_resuccion(cubetas, listaDatos, porcentaje):
  total_cubetas = cubetas
  total_registros = len(listaDatos)
  if (total_registros / total_cubetas) * 100 <= porcentaje:
      return True
  else:
      return False

def hash_mod(CLave, NCubetas):
  return CLave % NCubetas