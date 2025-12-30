# from turtle import Turtle, Screen


# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)


# my_screen = Screen()
# # print(my_screen.canvheight)
# my_screen.exitonclick()

# print("| Pokemon Name | Type |")
# print("---------------------")

from prettytable import PrettyTable

lista_poke = ["pikachu", "charmander", "squirtle", "venaousour", "raichu"]
lista_tipos = ["electrico", "fuego", "agua", "hierba", "electrico"]

tabla = PrettyTable()
tabla.add_column("Pokemon Name", lista_poke)
tabla.add_column("Type", lista_tipos)

tabla.align = "l"

print(tabla)
print(tabla.align)
