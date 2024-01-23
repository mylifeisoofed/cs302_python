import os
import random
from pokemon_list import *
"""
Brian Le

This pokemon game will be a "gacha" style game, where players need to pull (randomly recieve) pokemons of different rarity.
Pokemons are classified by 5 rarities, from 1 to 5, 1 being the most common, 5 being the rarest.
Depending on the rarity, the player will gain exp.

Gacha Pull rates:
Rarity 1 = 40%
Rarity 2 = 30%
Rarity 3 = 15%
Rarity 4 = 10%
Rarity 5 = 5%

This file contains the classes and their function implementations.
Pokedex Class is the node for the LLL
Node Class is the node for the BST and "has a" Pokedex
Player Class is the containing class managing the BST and LLL.

The Hierarchy:
Pokemon is the Base Class
Grass, Water, and Fire "is a" Pokemon + more

"""


"""LLL NODE CLASS"""
class Pokedex: # This is the Node for the LLL of pokemons
    def __init__(self, pokemon):
        self.next = None
        self.__pokemon = pokemon

    def __del__(self):
        self.next = None

    
    def get_next(self):
        return self.next
    
    def get_pokemon(self):
        return self.__pokemon
    
    def set_next(self, next):
        self.next = next

    def display(self): # calling the pokemon's display function here.
        self.__pokemon.display()
    
    
"""BST NODE CLASS"""
class Node: # This Node is for the BST. Each node has a linear linked list of the same pokemon type and name.
    def __init__(self, pokemon):
        self.__left = None
        self.__right = None

        #This is the LLL
        self.__pokedex = Pokedex(pokemon) # everytime a node is created, insert the pokemon into the LLL
        self._pokemon_count = 1 # this is independent from the Player class. This is the count of total pokemons of the same name per Node.
        self.__pokemon_name = pokemon.get_name()
    
    def __del__(self): # destructor
        self.__left = None
        self.__right = None
        self.__pokedex = None

    def set_right(self, right):
        self.__right = right
    
    def set_left(self, left):
        self.__left = left

    def get_right(self):
        return self.__right
    
    def get_left(self):
        return self.__left
    
    def get_count(self): # this will be used when removal is done
        return self._pokemon_count
    
    # Operator Overloadings
    def __eq__(self, to_compare): # the equality compares the names. to_compare is a string op2.
        return self.__pokemon_name == to_compare
    
    def __lt__(self, to_compare): # these operators help determine where to store the data in the BST.
        return self.__pokemon_name < to_compare
    
    def __gt__(self, to_compare):
        return self.__pokemon_name > to_compare

    
    def add(self, pokemon): # Wrapper to kickstart the pokedex append function
        self.__pokedex = self._append_pokedex(self.__pokedex, pokemon)

    def _append_pokedex(self, head, pokemon): # adding to LLL
        temp = head
        head = Pokedex(pokemon) # pretend Pokedex is a LLL Node class...
        head.set_next(temp)
        self._pokemon_count += 1

        """
        # This is old and less efficient way to add into the LLL. But it works.
        if head == None:
            head = Pokedex(pokemon)
            self._pokemon_count += 1
            return head
        
        head.set_next(self._append_pokedex(head.get_next(), pokemon))
        return head
        """

        return head
    
        
    
    def display(self): # wrapper to show every single pokemon that the LLL has
        print("List of all", self.__pokemon_name+":")

        if self.__pokedex == None:
            print("No", self.__pokemon_name, "in the pokedex!\n")
            return
            
        self.__pokedex = self._display_list(self.__pokedex)


        #for i in range(len(self.__pokedex)):
           # self.__pokedex[i].display()
        
    def _display_list(self, head, i = 1):
        if head == None:
            return # at the end of the list
        print(str(i)+")")
        head.display()
        i += 1
        head.set_next(self._display_list(head.get_next(), i))
        return head
    
    def remove_one(self): # wrapper function to remove a singular pokemon from the list. Called by the Player class's
        if self.__pokedex == None:
            print("No Pokemons in the pokedex!")
            return False
        
        self.__pokedex = self._display_list(self.__pokedex)

        index = self.__get_index() # getting the index while also doing some error checking

        """
         index = int(input("Please select a number coresponding with the Pokemon to be deleted: ")) # will raise value error if incorrect inputs given

        index -= 1 # get index
        if index < 0: # cannot be a negative index
            raise ValueError
        """
       
        self.__pokedex = self._remove_one(self.__pokedex, index, 0)

        return True
    
    def _remove_one(self, head, index, counter = 0):
        if head == None: #at the end for some odd reason
            return head
        
        if counter == index: # at the index. do the removal
            temp = head.get_next()
            head = None
            head = temp
            self._pokemon_count -= 1
            return head

        counter += 1
        head.set_next(self._remove_one(head.get_next(), index, counter))
        return head
    
    def get_pokemon_showcase(self, showcase_list): # Wrapper function to retrieve a specific Pokemon
        if self.__pokedex == None: # The LLL of pokemons is empty
            print("No Pokemons in the pokedex!")
            return
        
        self.__pokedex = self._display_list(self.__pokedex)  # print the list of pokemons
        index = self.__get_index()

        self.__pokedex = self._get_pokemon(self.__pokedex, index, showcase_list, 0)
        return
    
    def _get_pokemon(self, head, index, showcase_list, counter = 0):
        if head == None: #at the end
            return head
        
        if counter == index: # at the index. copy this pokemon.
            showcase_list.append(head.get_pokemon())
            return head
        
        counter += 1
        head.set_next(self._get_pokemon(head.get_next(), index, showcase_list, counter))
        return head


    
    def __get_index(self): # Index Getter. Basically let's me treat a LLL like an array
        index = int(input("Please select a number coresponding with the Pokemon: ")) # will raise value error if incorrect inputs given

        index -= 1 # get index
        if index < 0: # cannot be a negative index
            raise ValueError
        
        return index


"""PLAYER CLASS"""
class Player: # The avatar class. this class will also be managing the BST.
    def __init__(self, name = "Player", level = 1):
        self._name = name
        self._level = level
        self._pokemon_count = 0 # the total number of pokemons pulled.
        self.__max_exp = 100 # need 100xp to level up
        self.__exp = 0
        self.__showcase = [] # allows players to show off their coolest/favorite pokemons

        #self._pokedex = pokedex.copy() # list of pokemons that the player has

        self.__root = None
    
    def __del__(self):
        self.__root = None

    def gacha_pull(self): # gacha pull function
        rarities = [5, 4, 3, 2, 1]
        pull_rates = [5, 10, 15, 30, 40]

        # Getting Random Rarity
        num = random.choices(rarities, pull_rates, k = 1) # pulling the rarity

         # Getting Random Elements
        element = random.randint(0, 2) # getting the element type
        if element == 0:
            pokemon_index = random.randint(0, len(pokemon_list_fire) - 1)
            pokemon = pokemon_list_fire[pokemon_index] # Getting a random fire pokemon
            pokemon_pull = Fire(pokemon, num[0])
        
        if element == 1:
            pokemon_index = random.randint(0, len(pokemon_list_water) - 1)
            pokemon = pokemon_list_water[pokemon_index]
            pokemon_pull = Water(pokemon, num[0])

        if element == 2:
            pokemon_index = random.randint(0, len(pokemon_list_grass) - 1)
            pokemon = pokemon_list_grass[pokemon_index]
            pokemon_pull = Grass(pokemon, num[0])

        print("You got a",pokemon,"of",num[0], "star rarity!")

        # calculating the xp gain
        if num[0] == 5:
            self.__exp_calculate(20)
            print("20 XP Gained")
        elif num[0] == 4:
            self.__exp_calculate(10)
            print("10 XP Gained")
        else:
            self.__exp_calculate(5)
            print("5 XP Gained")
        

        # insert into the bst
        self._pokemon_count +=1
        self._insert(pokemon_pull)
        return self._pokemon_count

    def __exp_calculate(self, gained): # xp calculation
        self.__exp += gained
        if self.__exp >= self.__max_exp: # Level up!
            self._level +=1
            leftover = self.__exp - self.__max_exp
            self.__exp = leftover
            print("Leveled Up to",str(self._level)+"!")
        return self._level
    
    def display_player(self): # function to show player/avatar info
        print("")
        print("Player Name:",self._name)
        print("Level:",self._level)
        print("Pokemon Count:",self._pokemon_count)
        print("EXP:",str(self.__exp)+"/"+str(self.__max_exp))
        print("Pokemon Showcase:")
        if self._pokemon_count == 0:
            print("User has not showcase any Pokemons")
        else:
            print("")
            for i in range(len(self.__showcase)):
                self.__showcase[i].display()
            

        print("")
    
    def insert_custom(self, pokemon): # function for inserting custom pokemons
        self._insert(pokemon)
        self._pokemon_count += 1
        
    def _insert(self, pokemon): # wrapper function to add the pokemon that the player has pulled
        self.__root = self._append(self.__root, pokemon)
    
    def _append(self, root, pokemon): # function to add the pokemon into the BST. if the node exists, then it will be appeneded into the LLL
        if root == None:
            root = Node(pokemon)
            print("New Pokemon Discovered!")
            return root
        
        
        if root == pokemon.get_name(): # using our operator overloading
            root.add(pokemon)
            return root
        
        if root > pokemon.get_name():
            root.set_left(self._append(root.get_left(), pokemon))

        elif root < pokemon.get_name():
            root.set_right(self._append(root.get_right(), pokemon))

        return root
    
    def display_pokedex(self): # wrapper function to display all pokemons that the user has pulled
        self.__root = self._display(self.__root)
        return self._pokemon_count
    
    def _display(self, root): # show all pokemon
        if root == None:
            return root
        
        root.display()
        root.set_left(self._display(root.get_left()))
        root.set_right(self._display(root.get_right()))
        return root
    
    def retrieve(self, pokemon_name): # wrapper function to display only the pokemon given

        assert pokemon_name != ""

        if self.__root == None:
            print("There are no Pokemons in your Pokedex")
            return
        
        self.__root = self.__retrieve(self.__root, pokemon_name)

    def __retrieve(self, root, pokemon_name): 
        if root == None: # at the end
            return root
        
        if root == pokemon_name: # we found a match
            root.display()
            return root
        
        root.set_left(self.__retrieve(root.get_left(), pokemon_name))
        root.set_right(self.__retrieve(root.get_right(), pokemon_name))
        return root
    
    def remove_pokemon(self, pokemon_name): # wrapper for the remove pokemon
        if self.__root == None: # empty
            return self._pokemon_count
        
        self.__root = self.__remove_pokemon(self.__root, pokemon_name)
        return self._pokemon_count
    
        
    
    def __remove_pokemon(self, root, pokemon_name): # removal function
        if root == None: # at the end
            return root
        
        if root == pokemon_name: # match found. delete.
            self._pokemon_count -= root.get_count()
            if not root.get_left() and not root.get_right(): # leaf or no children
                root = None
                return root

            if root.get_left() and not root.get_right(): # one left child
                temp = root.get_left()
                root = None
                root = temp
                return root
            
            if root.get_right() and not root.get_left(): # one right child
                temp = root.get_right()
                root = None
                root = temp
                return root

            if root.get_right() and root.get_left(): # 2 children
                # find ios
                ios = root.get_right()

                if ios.get_left() == None: # checking if the right children is the ios.
                    ios.set_left(root.get_left())
                    root = None
                    root = ios
                    return root
            
                while ios.get_left() != None: # traverse to the left most of this subtree
                    prev = ios
                    ios = ios.get_left()
                
                # make ios replace the deleted node.
                ios.set_right(root.get_right())
                ios.set_left(root.get_left())
                root = None
                root = ios
                prev.set_left(None) # disconnect the ios to prevent a cycle.
                return root
            
            
        root.set_left(self.__remove_pokemon(root.get_left(), pokemon_name))
        root.set_right(self.__remove_pokemon(root.get_right(), pokemon_name))
        return root
    
    def remove_single(self, pokemon_name): # wrapper function to remove A pokemon from the LLL/pokedex
        if self.__root == None: #empty tree
            print("You have not discovered any Pokemons!")
            return False
        
        self.__root = self.__remove_single(self.__root, pokemon_name)
        return True
    
    def __remove_single(self, root, pokemon_name):
        if root == None: #hit the end
            return root
        
        if root == pokemon_name: # found the pokemon, time to figure out which to remove
            root.remove_one() # all the remove stuff happens in this call
            self._pokemon_count -= 1
            return root
        
        root.set_left(self.__remove_single(root.get_left(), pokemon_name))
        root.set_right(self.__remove_single(root.get_right(), pokemon_name))
        return root
    
    def add_showcase(self, pokemon_name): # Basically our wrapper function to retrieve a Pokemon object into the List
        if self.__root == None: # empty tree = no pokemons discovered/pulled
            print("You have not discovered any Pokemons!")
            return False
        
        self.__root = self.__add_showcase(self.__root, pokemon_name, self.__showcase)
        return True

    def __add_showcase(self, root, pokemon_name, showcase_list): # its showtime!
        if root == None: # at the end
            return root
        
        if root == pokemon_name: # found the match, begin to add into the showcase list
            root.get_pokemon_showcase(showcase_list)
            return root
        
        root.set_left(self.__add_showcase(root.get_left(), pokemon_name, showcase_list))
        root.set_right(self.__add_showcase(root.get_right(), pokemon_name, showcase_list))
        return root

        

"""POKEMON HIERARCHY"""
class Pokemon:
    def __init__(self, name="", rarity=1): 
        if not name: # every pokemon needs a name or an error will raise
            raise ValueError
        
        self._name = name
        self._rarity = rarity


    def _display(self): # this function should be called by their derives.
        print("Pokemon Name:", self._name)
        print("Rarity:", self._rarity,"star")
    
    # Operator Overloading
    def get_name(self):
        return self._name
    
    def __eq__(self, other):
        return self._name == other
    
    def __lt__(self, other):
        return self._name < other
    
    def __gt__(self, other):
        return self._name > other


class Water(Pokemon):
    def __init__(self, name="", rarity=1):
        if not name: # every pokemon needs a name or an error will raise
            raise ValueError
        
        super().__init__(name, rarity)
        self._type = "Water"
        self._weakness = "Grass"
    
    def display(self):
        super()._display()
        print("Element Type:",self._type)
        print("Weakness:",self._weakness)
        print()
        

class Fire(Pokemon):
    def __init__(self, name="", rarity=1):
        if not name: # every pokemon needs a name or an error will raise
            raise ValueError
        
        super().__init__(name, rarity)
        self._type = "Fire"
        self._weakness = "Water"
    
    def display(self):      
        super()._display()
        print("Element Type:",self._type)
        print("Weakness:",self._weakness)
        print()

        
        
class Grass(Pokemon):
    def __init__(self, name="", rarity=1):
        if not name: # every pokemon needs a name or an error will raise
            raise ValueError
        
        super().__init__(name, rarity)
        self._type = "Grass"
        self._weakness = "Fire"
    
    def display(self):
        super()._display()
        print("Element Type:",self._type)
        print("Weakness:",self._weakness)
        print()
        