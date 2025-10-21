# 🧭 Maze Challenge — Day 06 (100 Days of Code - Python)
# -------------------------------------------------------
#
# Este proyecto corresponde al "Maze Challenge" (Reto del Laberinto)
# del **Day 06** del curso:
# 👉 "100 Days of Code – The Complete Python Pro Bootcamp for 2023" de Angela Yu.
#
# -------------------------------------------------------
# 🧩 CONTEXTO DEL PROYECTO
# -------------------------------------------------------
#
# Este desafío se desarrolla dentro del entorno interactivo de:
#     🔗 https://reeborg.ca/reeborg.html
#
# Reeborg’s World es una plataforma educativa que permite ejecutar código
# Python simplificado dentro de un mundo 2D. Allí, un personaje (Reeborg)
# debe recorrer un laberinto hasta alcanzar la meta siguiendo reglas básicas.
#
# El código original del reto depende de funciones que NO existen en Python real:
#
#   - move()
#   - turn_left()
#   - wall_on_right()
#   - at_goal()
#
# Estas funciones son provistas por el entorno de Reeborg y controlan
# al personaje dentro del mundo visual. Por eso, **este código no se puede
# ejecutar en un intérprete de Python local**, sino que debe correrse dentro
# del sitio web de Reeborg.
#
# -------------------------------------------------------
# 🎯 OBJETIVO DEL RETO
# -------------------------------------------------------
#
# El reto enseña estructuras de control (while, if) y lógica algorítmica.
# El objetivo es encontrar la salida del laberinto aplicando reglas simples:
#
#   1️⃣ Si no hay una pared a la derecha → girar a la derecha y avanzar.
#   2️⃣ Si hay una pared a la derecha → girar a la izquierda.
#   3️⃣ Repetir hasta llegar a la meta.
#
# Ejemplo de código original (dentro de Reeborg):
#
# while not at_goal():
#     if not wall_on_right():
#         turn_right()
#         move()
#     else:
#         turn_left()

cd "C:\Users\Axel\_infotech\_notebook"
jupyter notebook