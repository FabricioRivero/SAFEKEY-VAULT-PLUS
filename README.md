Proyecto Final Integrador – Programación I: SAFEKEY VAULT+

Autor: Luis Fabricio Rivero Aban
Carrera: Ingeniería en Sistemas
Materia: Programación I
Año: 2025

🔐 Descripción general del proyecto

SAFEKEY VAULT+ es un gestor de contraseñas desarrollado en Python, diseñado como proyecto final integrador de la materia Programación I.

El sistema permite:

Guardar contraseñas de distintos servicios

Cifrarlas y descifrarlas con dos métodos

Proteger el acceso con contraseña maestra

Analizar la fortaleza de las contraseñas

Realizar búsquedas inteligentes (con recursividad)

Registrar acciones en un archivo de auditoría

Usar archivos para persistencia de datos

SAFEKEY VAULT+ se inspira en herramientas como LastPass, 1Password o KeePass, pero construido completamente desde cero aplicando recursividad, modularidad, manejo de archivos y diseño estructurado.

🎯 Objetivos del sistema

Proteger el ingreso con una contraseña maestra cifrada

Gestionar contraseñas de múltiples servicios

Aplicar cifrado César y cifrado recursivo

Evaluar la fuerza de contraseñas nuevas

Generar contraseñas seguras

Buscar servicios mediante coincidencias exactas y recursivas

Registrar todas las acciones en un log

Verificar integridad mediante recursividad

📂 Estructura del proyecto (Modularidad)

Este proyecto sigue el principio de diseño modular (EC1), separando la lógica en varios archivos .py:

main.py
auth.py
crypto.py
storage.py
password_manager.py
search.py
integrity.py
generator.py
strength.py
log.py

🧩 ¿Qué hace cada módulo?

main.py → Control del menú principal y flujo del sistema
auth.py → Manejo de la contraseña maestra y autenticación
crypto.py → Cifrado César y cifrado recursivo (usa recursividad)
storage.py → Lectura y escritura de archivos (data.txt)
password_manager.py → CRUD de contraseñas
search.py → Buscador inteligente (incluye búsqueda recursiva)
integrity.py → Revisión recursiva de integridad
generator.py → Generación de contraseñas seguras
strength.py → Análisis de fuerza de contraseñas
log.py → Registro de acciones (log.txt)

🧪 Tecnologías y conceptos aplicados
✔ EC1 – Diseño descendente y modularidad

El sistema se divide en módulos independientes y fáciles de mantener.

✔ EC2 – Arreglos, estructuras de datos y archivos

Las contraseñas se almacenan como diccionarios dentro de una lista.

Persistencia mediante archivos:

config.txt → contraseña maestra

data.txt → registros cifrados

log.txt → auditoría

✔ EC3 – Recursividad aplicada

Inversión recursiva de texto para cifrado

Búsqueda recursiva por coincidencia parcial

Revisión de integridad recursiva

🧹 Cumplimiento del Estilo PEP 8

El proyecto fue desarrollado siguiendo las recomendaciones del estándar PEP 8, garantizando un código legible, mantenible y claro.

✔ Reglas PEP 8 aplicadas

1. Indentación con 4 espacios
Todo el código utiliza indentación consistente; no se usan tabs.

2. Nombres en minúsculas_con_guiones_bajos
Funciones y variables siguen el formato recomendado.
Constantes en MAYÚSCULAS cumplen el estándar (DATA_FILE, CONFIG_FILE).

3. Líneas de longitud razonable
Las líneas se mantienen legibles, evitando extensiones innecesarias.

4. Espacios adecuados en operadores y comas
Ejemplos correctos:
score += 1, for i, r in enumerate(registros), if a == b:

5. Comentarios y docstrings útiles
Cada módulo contiene explicación detallada al inicio.
Las funciones esenciales poseen docstrings como documentación interna.

6. Evitar globales innecesarios
El sistema pasa datos entre funciones sin depender de variables globales, salvo en el módulo de log, donde se usa un contador documentado.

Resultado:
El código cumple adecuadamente las normas esenciales de PEP 8, logrando un estilo profesional, ordenado y de fácil lectura.

🔧 Cómo ejecutar el proyecto
Requisitos:

Python 3.x instalado

Ejecución:
python main.py

Primera ejecución

Si no existe contraseña maestra, el sistema solicitará crear una y la guardará cifrada.

🔐 Funciones principales
🔸 Agregar contraseñas

Solicita servicio, usuario, contraseña y método de cifrado.

🔸 Consultar contraseñas

Muestra información del servicio y permite descifrar bajo confirmación.

🔸 Editar contraseñas
🔸 Eliminar contraseñas
🔸 Buscador inteligente

Por servicio

Por usuario

Coincidencia parcial (recursivo)

🔸 Generador de contraseñas seguras
🔸 Revisión de integridad (recursiva)
🔸 Registro de acciones

Todas las acciones van a log.txt.

📚 Archivos generados por el sistema

config.txt → contraseña maestra cifrada
data.txt → base de datos cifrada
log.txt → historial de auditoría

👨‍💻 Repositorio del proyecto

🔗 https://github.com/FabricioRivero/SAFEKEY-VAULT-PLUS

📝 Autor

Luis Fabricio Rivero Aban
Proyecto Final Integrador – Programación I
SAFEKEY VAULT+ – Gestor de Contraseñas