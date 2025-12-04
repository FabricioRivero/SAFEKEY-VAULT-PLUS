# strength.py
# Analiza qué tan fuerte es una contraseña

def evaluar_fuerza(contraseña):
    score = 0
    if len(contraseña) >= 8:
        score += 1
    if len(contraseña) >= 12:
        score += 1
    if any(c.isupper() for c in contraseña):
        score += 1
    if any(c.islower() for c in contraseña):
        score += 1
    if any(c.isdigit() for c in contraseña):
        score += 1
    simbolos = "!@#$%^&*()-_+=[]{};:,.<>?"
    if any(c in simbolos for c in contraseña):
        score += 1

    low = contraseña.lower()
    if "123" in low or "password" in low or "abc" in low or "qwerty" in low:
        score -= 2

    if score <= 2:
        return "DEBIL"
    elif score <= 4:
        return "MEDIA"
    elif score <= 6:
        return "FUERTE"
    else:
        return "MUY FUERTE"
