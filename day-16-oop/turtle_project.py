# import turtle

# timmy= turtle.Turtle()
# timmy.shape('turtle')
# timmy.color('blue')
# timmy.forward(100)


# my_screen= turtle.Screen()

# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
# this is the class PrettyTable
table = PrettyTable()

#addcolumn is the function
table.add_column('Pokeman', ['Pikachu', 'Squirtle', 'Charmander']) ;table.add_column('Name',["Electric", 'Water', 'Fire'])
#this is the attribute
table.align='l'
print(table)