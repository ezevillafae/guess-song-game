import re
def filtrar(cadena):
    """Borra caracteres especiales y reemplaza caracteres acentuados a caracteres sin acentuar"""
    cadena = cadena.lower() 
    cadena = re.sub("[\-()!¡\n\.]", "",cadena) #borra caracteres especiales
    #remplaza los caracteres acentuados
    cadena = cadena.replace("á","a")
    cadena = cadena.replace("é","e")
    cadena = cadena.replace("í","i")
    cadena = cadena.replace("ó","o")
    cadena = cadena.replace("ú","u")
    return cadena

    





