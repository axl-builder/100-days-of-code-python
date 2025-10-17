# 🧭 Maze Challenge — Day 06 (100 Days of Code - Python)

Este proyecto corresponde al **"Maze Challenge" (Reto del Laberinto)** del **Day 06** del curso [*100 Days of Code – The Complete Python Pro Bootcamp for 2023*](https://www.udemy.com/course/100-days-of-code/), de Angela Yu.

---

## 🧩 Contexto del proyecto

El desafío se desarrolla dentro del entorno interactivo de **[Reeborg’s World](https://reeborg.ca/reeborg.html)**, una plataforma en línea que permite ejecutar código Python simplificado en un mundo 2D.  
En este entorno, el personaje “Reeborg” debe encontrar la salida de un laberinto siguiendo ciertas reglas lógicas.

El código original utiliza funciones que **no existen en Python real**, como:
- `move()`
- `turn_left()`
- `wall_on_right()`
- `at_goal()`

Estas funciones son **propias del entorno de Reeborg** y controlan al personaje virtual dentro de su mundo gráfico.  
Por lo tanto, el código del reto **no puede ejecutarse directamente en un intérprete de Python local**, sino que debe correrse dentro del sitio web de Reeborg.

---

## 🎯 Objetivo del reto

El objetivo es enseñar **estructuras de control (`while`, `if`, etc.)** y **pensamiento algorítmico**, haciendo que el robot encuentre la salida de un laberinto siguiendo estas reglas básicas:

1. Si **no hay una pared a la derecha**, girar a la derecha y avanzar.  
2. Si **hay una pared a la derecha**, girar a la izquierda.  
3. Repetir hasta llegar al objetivo (`at_goal()`).

Ejemplo de código base (en el entorno de Reeborg):

```python
while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    else:
        turn_left()
