# CS302 Python Programming Project
This was a Python programming project I had to do in CS302 at Portland State University
The project demonstrates my ability to do OOP in Python and utilize concepts like exception handling and unit testing via PyTest.
I was also required to create a specification for this project. Full specification can be found here: https://docs.google.com/document/d/1RB-k4-5OngC-f2oGx0s9aVxdLFmRVJD9h1gqjg-HxEA/edit?usp=sharing

Below is the readme file on how to utilize this program:
# Welcome to the Pokemon Gacha Game

Players will need to enter their name and begin catching Pokemons by
performing Gacha pulls. For this program, Players need to insert cash in
dollar bills to pull. The program will reject any changes/coins.

Each Pokemon that the player gets will be added into their Pokedex.
Players can display all their Pokemons in their Pokedex or 
search for a specific Pokemon in the Pokedex. Players can also
showcase their Pokemons on their profile



There are a couple options that are negative numbers since we do not want players to 
mess with these functions:

To create a custom pokemon, type "-1" as an option and carefully follow the directions.
All Pokemons, and custom ones that we add to the player's pokedex, must have a name. Otherwise, a Value Error will be raised.

To delete all specified Pokemons, type "-2" as an option. For example, entering "Charmander" will delete ALL Charmanders
in the Player's Pokedex. This is case sensitive since we have the ability to add custom pokemons

If we need to delete A Pokemon, type "-3" as an option. Enter the name of the Pokemon we wish to delete and 
all the Pokemons of that name will be displayed and indexed with a number. Entering the specified number will 
delete the Pokemon corresponding with that number. If the number given is negative, a value error will be raised.
