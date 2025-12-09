Proyecto Final Integrador – Programación I

Autor: Luis Fabricio Rivero Aban
Carrera: Ingeniería en Sistemas
Materia: Programación I
Año: 2025

🔐 Descripción general del proyecto

SAFEKEY VAULT+ es un gestor de contraseñas desarrollado en Python, diseñado como proyecto final integrador para la materia Programación I.
El sistema permite guardar, cifrar, consultar, editar y eliminar contraseñas de distintos servicios, aplicando recursividad, modularidad, arreglos, manejo de archivos y análisis de fuerza, cumpliendo así los elementos de competencia de la asignatura.

SAFEKEY VAULT+ simula el funcionamiento de herramientas reales como LastPass, 1Password o KeePass, pero construido desde cero.

🎯 Objetivos del sistema

Proteger el acceso mediante una contraseña maestra cifrada.

Administrar contraseñas de distintos servicios.

Aplicar dos métodos de cifrado (César y Recursivo).

Evaluar la fortaleza de las contraseñas ingresadas.

Generar contraseñas seguras personalizadas.

Realizar búsquedas inteligentes, incluyendo búsqueda recursiva.

Registrar todas las acciones en un archivo de auditoría.

Verificar la integridad de los datos utilizando recursividad.

📂 Estructura del proyecto (Modularidad)

Este proyecto se desarrolló siguiendo el principio de diseño modular (EC1), separando la lógica en varios archivos Python:

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

main.py → Menú principal y flujo del sistema

auth.py → Manejo de la contraseña maestra y autenticación

crypto.py → Métodos de cifrado (César y recursivo)

storage.py → Lectura y escritura de archivos (data.txt)

password_manager.py → Agregar, consultar, editar, eliminar contraseñas

search.py → Búsquedas exactas y recursivas

integrity.py → Revisión recursiva de integridad

generator.py → Generación de contraseñas seguras

strength.py → Análisis de fuerza de contraseñas

log.py → Registro de auditoría (log.txt)

🧪 Tecnologías y conceptos aplicados
✔ EC1 – Diseño descendente y modularidad

El sistema se divide en varios módulos independientes para mantener claridad, orden y mantenimiento adecuado.

✔ EC2 – Arreglos, estructuras de datos y archivos

Las contraseñas se almacenan como diccionarios dentro de una lista.

Persistencia mediante archivos:

config.txt → contraseña maestra cifrada

data.txt → base de datos de contraseñas

log.txt → registro de auditoría

✔ EC3 – Recursividad

Recursividad utilizada en:

Inversión de texto para cifrado recursivo

Búsqueda por coincidencia parcial

Revisión de integridad de registros

🔧 Cómo ejecutar el proyecto

Requisitos:

Python 3.x

Ejecutar desde consola:

python main.py

✔ Primera ejecución:

El sistema detectará si existe una contraseña maestra.
Si no existe, solicitará crear una y la almacenará cifrada.

🔐 Funciones principales
🔸 Agregar contraseñas

Solicita servicio, usuario, contraseña y método de cifrado.

🔸 Consultar contraseñas

Muestra datos y permite descifrar la contraseña bajo confirmación.

🔸 Editar contraseñas

Permite modificar contraseña y método de cifrado.

🔸 Eliminar contraseñas
🔸 Buscador inteligente

Por servicio

Por usuario

Por coincidencia parcial (recursivo)

🔸 Generador de contraseñas seguras

Opciones de longitud, símbolos, números, mayúsculas.

🔸 Revisión de integridad (recursiva)
🔸 Registro de acciones

Cada operación se almacena en log.txt.

📚 Archivos generados por el sistema

config.txt → guarda la contraseña maestra cifrada

data.txt → base de datos de contraseñas cifradas

log.txt → auditoría de acciones

👨‍💻 Repositorio del proyecto

🔗 https://github.com/FabricioRivero/SAFEKEY-VAULT-PLUS

📝 Autor

Luis Fabricio Rivero Aban
Proyecto Final Integrador – Programación I
Gestor de Contraseñas SAFEKEY VAULT+