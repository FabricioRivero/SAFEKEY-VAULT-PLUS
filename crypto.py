# crypto.py
# Funciones de cifrado y descifrado (incluye recursividad)

def cifrar_cesar(texto, desplaz):
    res = []
    for c in texto:
        if c.isalpha():
            base = 'A' if c.isupper() else 'a'
            res.append(chr((ord(c) - ord(base) + desplaz) % 26 + ord(base)))
        else:
            res.append(c)
    return ''.join(res)


def descifrar_cesar(texto, desplaz):
    return cifrar_cesar(texto, 26 - (desplaz % 26))


def invertir_recursivo(texto):
    # Función RECURSIVA que invierte un string
    if len(texto) <= 1:
        return texto
    return invertir_recursivo(texto[1:]) + texto[0]


def cifrar_recursivo(texto):
    invertido = invertir_recursivo(texto)
    return cifrar_cesar(invertido, 3)


def descifrar_recursivo(texto):
    parcial = descifrar_cesar(texto, 3)
    return invertir_recursivo(parcial)
