from myclass import *

"""
Brian Le

This is the client program that users will be
playing and testing their program.

"""

def main():
    username = input("Please Enter Your Name: ")
    my_player = Player(username)
    os.system("cls")

    program = True
    total = 0.00

    while program: # The main program
        menu()

        try:
            option = int(input("Enter: "))
            print("")
        except ValueError:
            print("Not an option. Please try again")
            print("")
            continue

        if option == 1: # we can get creative and charge users every gacha pull
            os.system("cls")
            print("Each Gacha pull is $1.00. Only accepting dollar bills.") #only accepting dollar bills. No cents.
            try:
                money = float(input("Please enter the amount: $"))
            except ValueError:
                print("Not the correct amount! Please try again!")
                continue

            if money % 1 == 0 and money >= 1.00:
                total += money
                rolls = int(money)
                for i in range(rolls):
                    my_player.gacha_pull()
            else:
                print("Not the correct amount! Please try again!")
        
        if option == 2: # Display All Pokemons
            my_player.display_pokedex()
        
        if option == 3: # Display Player Profile
            os.system("cls")
            my_player.display_player()
             
        if option == 4: # Search for a specific Pokemon in the Pokedex
            print_all_pokemon()
            pokemon_name = input("Enter the name of the Pokemon (CASE SENSITIVE): ")
            try:
                my_player.retrieve(pokemon_name)
            except AssertionError:
                print("Invalid Input. Please Try Again.")

        if option == 5: # Add Pokemon to Profile Showcase
            print_all_pokemon()
            try: # Error will be caused by either the input the user given, or from the add_showcase()
                pokemon_name = input("Enter the name of the Pokemon (CASE SENSITIVE): ")
                my_player.add_showcase(pokemon_name)
            except ValueError:
                print("Invalid number given. Please try again.")
        
        if option == 6: # Exiting the Program
            print("Thanks for Playing!")
            print("You have spent: $%.2f" %total) 
            program = False

        # Options for developers
        if option == -1: # Adding our own custom Pokemon
            pokemon_name = input("Enter the name of the custom Pokemon: ")
            try:
                rarity = int(input("Enter the rarity: ")) # will raise error
                print("What Element is this Pokemon?")
                print("Water, Fire, or Grass?")
                type = input("Enter: ")

                # Now we find what type of Pokemon
                if type.lower() == "water":
                    pokemon = Water(pokemon_name, rarity)
                    my_player.insert_custom(pokemon)

                elif type.lower() == "fire":
                    pokemon = Fire(pokemon_name, rarity)
                    my_player.insert_custom(pokemon)

                elif type.lower() == "grass":
                    pokemon = Grass(pokemon_name, rarity)
                    my_player.insert_custom(pokemon)

                else:
                    print("Not a valid Element. Please Try again.")
                    print("")
            
            except ValueError: # errors raised by the type input or pokemon constructor.
                print("Not a Valid Pokemon Name or Rarity. Please Try Again.")
        
        if option == -2: # Remove ALL Pokemons by name
            print_all_pokemon()
            print("WARNING! THIS WILL REMOVE ALL SPECIFIED POKEMONS!")
            pokemon_name = input("Enter the name of the Pokemons to be deleted: ")
            my_player.remove_pokemon(pokemon_name)

        if option == -3: # Remove A Pokemon by name
            try:
                print_all_pokemon()
                print("WARNING! THIS WILL REMOVE A SPECIFIED POKEMON!")
                pokemon_name = input("Enter the name of the Pokemon to be deleted: ")
                my_player.remove_single(pokemon_name)
            except ValueError:
                print("Invalid number given. Please try again.")
            
            
def menu(): # menu function
    print("Pokemon Gacha!\n")
    print("Please select an option")
    print("1. Gacha Pull!")
    print("2. Display Pokedex")
    print("3. Show Player Profile")
    print("4. Search Pokemon")
    print("5. Add Pokemon to Profile Showcase")
    print("6. Exit")

def print_all_pokemon(): # prints all the list of pokemons in pokemon_list.py
    print("List of Water Pokemons:")
    for i in range(len(pokemon_list_water)):
        print(pokemon_list_water[i])
    print("")

    print("List of Fire Pokemons:")
    for i in range(len(pokemon_list_fire)):
        print(pokemon_list_fire[i])
    print("")

    print("List of Grass Pokemons:")
    for i in range(len(pokemon_list_grass)):
        print(pokemon_list_grass[i])
    print("")
    
        
if __name__ == "__main__":
    main()