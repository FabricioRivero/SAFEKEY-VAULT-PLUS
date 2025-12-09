# ============================================================
# crypto.py
# Módulo de CIFRADO y DESCIFRADO.
# - Implementa cifrado César.
# - Implementa cifrado RECUSIVO (invertir texto + César).
# - Demuestra uso de recursividad (invertir_recursivo).
# ============================================================


def cifrar_cesar(texto, desplaz):
    """
    Aplica el cifrado César a 'texto' con un desplazamiento dado.
    Solo modifica letras; otros caracteres se mantienen igual.
    """
    res = []
    for c in texto:
        if c.isalpha():
            base = 'A' if c.isupper() else 'a'
            res.append(chr((ord(c) - ord(base) + desplaz) % 26 + ord(base)))
        else:
            res.append(c)
    return ''.join(res)


def descifrar_cesar(texto, desplaz):
    """
    Revierte el cifrado César usando el desplazamiento inverso.
    """
    return cifrar_cesar(texto, 26 - (desplaz % 26))


def invertir_recursivo(texto):
    """
    Función RECURSIVA que invierte una cadena de texto.
    Caso base:
        - Si el texto tiene longitud 0 o 1, lo devuelve tal cual.
    Caso recursivo:
        - Invierte el substring desde el índice 1 en adelante
          y luego añade el primer carácter al final.
    """
    if len(texto) <= 1:
        return texto
    return invertir_recursivo(texto[1:]) + texto[0]


def cifrar_recursivo(texto):
    """
    Cifrado 'REC':
    1) Invierte la contraseña de forma recursiva.
    2) Aplica cifrado César con desplazamiento 3.
    """
    invertido = invertir_recursivo(texto)
    return cifrar_cesar(invertido, 3)


def descifrar_recursivo(texto):
    """
    Descifrado del método 'REC':
    1) Revierte el César.
    2) Vuelve a invertir el texto para recuperar el original.
    """
    parcial = descifrar_cesar(texto, 3)
    return invertir_recursivo(parcial)
