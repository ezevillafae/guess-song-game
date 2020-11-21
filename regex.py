import unicodedata
def filtrar(cadena):
    """Toma una cadena, quita las tildes y los caracteres especiales ",.-()!¡" """
    cadena = cadena[:-1].lower() #quita el ultimo caracter "\n" y pasa a minusculas
    tildes = "áéíóú"
    especiales = ",.-()"
    nuevaCadena = ""
    for letra in cadena:
        if letra in tildes:
            if letra == "á":
                nuevaCadena = nuevaCadena + "a"
            elif letra == "é":
                nuevaCadena = nuevaCadena + "e"
            elif letra == "í":
                nuevaCadena = nuevaCadena + "i"
            elif letra == "ó":
                nuevaCadena = nuevaCadena + "o"
            elif letra == "ú":
                nuevaCadena = nuevaCadena + "u"
        elif letra in especiales:
            nuevaCadena = nuevaCadena + " "
        else:
            nuevaCadena = nuevaCadena + letra
    nuevaCadena = nuevaCadena.strip() #quito los espacios del principio y al final
    return nuevaCadena