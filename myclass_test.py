import myclass
import pytest

"""
Brian Le

This is the Black Box Testing File. 
Functions that needs to be tested are done
here.

"""

def test_player(): # testing the Player class
    player = myclass.Player()
    assert player._name == "Player"
    assert player._level == 1
    assert player._pokemon_count == 0

    player = myclass.Player("Ash", 5)
    assert player._name == "Ash"
    assert player._level == 5

def test_gacha_pull(): # this also tests the BST insertion
    player = myclass.Player("Ash", 5)
    assert player.gacha_pull() == 1
    assert player.gacha_pull() == 2 # each pull returns the number of pokemons the player has pulled
    assert player._pokemon_count == 2 # and the total pokemon they should have is 2
    assert player.gacha_pull() == player._pokemon_count # Therefore, these should be the same

def test_display_pokedex(): # This test the BST and LLL Display functions
    player = myclass.Player("Ash", 5)

    for i in range(10):
        player.gacha_pull() # Player should have a count of 10 pokemons in their pokedex
    
    assert player._pokemon_count == 10

def test_pokemon_create():
    obj = myclass.Grass("Chikorita", 5)
    assert obj._rarity == 5
    assert obj._name == "Chikorita"
    assert obj._weakness == "Fire"
    assert obj._type == "Grass"

def test_LLLCreation(): # This tests the linked list
    obj2 = myclass.Fire("Charmander", 5)
    testnode = myclass.Node(obj2) # The Node class has a LLL of Pokemons of the same name
    testnode.add(obj2)
    testnode.add(obj2)

    assert testnode._pokemon_count == 3 # In this node, should be 3 charmanders in the LLL



def test_NodeOperators(): # This tests the operator overloadings of the BST Node class
    obj = myclass.Grass("Chikorita", 5)
    node = myclass.Node(obj)

    assert node == "Chikorita" # node will compare their pokemon name with 2nd operator
    assert node < "Diglet"
    assert node  > "Bulbasaur"

def test_remove_pokemon(): # testing the removal funciton of BST
    player = myclass.Player("Ash", 5)
    obj = myclass.Grass("Custom Pokemon", 5)
    assert player.gacha_pull() == 1
    assert player._pokemon_count == 1

    player.insert_custom(obj)
    assert player._pokemon_count == 2

    assert player.gacha_pull() #3 pokemons in pokedex
    assert player._pokemon_count == 3


    assert player.remove_pokemon("Custom Pokemon") == 2 #Now there is 2
    assert player._pokemon_count == 2

    # Now testing if the node has 2 or more of the same pokemon
    player.insert_custom(obj)
    player.insert_custom(obj)
    player.insert_custom(obj)
    assert player._pokemon_count == 5
    assert player.remove_pokemon("Custom Pokemon") == 2

def test_remove_single(): # testing the function to remove a single pokemon in the LLL
    obj2 = myclass.Fire("Charmander", 5)
    testnode = myclass.Node(obj2) # This Node has a LLL of Charmanders
    
    for i in range(9):
        testnode.add(obj2)

    assert testnode._pokemon_count == 10
    testnode._remove_one(testnode._Node__pokedex, 0, 0) # if we want to access __privatedata with 2 underscores, we have to include _ClassName followed by the __privatedata
    assert testnode._pokemon_count == 9

    

    





    


    

    

    
    














    


    
