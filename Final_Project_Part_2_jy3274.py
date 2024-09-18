# Jiayin(Jenny) Yu, March 26th 2023
from Jenny_Pokemon import *

def display_stat(object):
  """
  Call this function to display the current status of the chosen pokemon. 
  """
  print( f"Current stats of {object.Pokemon_name }: \n Trainer: {object.Trainer} \n Type:{object.Type}\n HP:{object.HP} \n ATK:{object.ATK} \n SPATK:{object.SPATK} \n DEF:{object.DEF} \n SPDEF:{object.SPDEF}"  )

list_of_actions = ["Tackle", "SPATK", "Do Nothing"]

def main(): 
  """
  Call this function to print the introduction of the "Very Best" Battle, and run the process of naming trainers, pokemon selections, and the battle. 
  """
  with open("Introduction.txt", "r") as file:
    Intro = file.read( )
    print(Intro)

  list_pokemons = []
  for cls in Jenny_Pokemon.__subclasses__():
    list_pokemons.append(cls.__name__)
  
  Trainer_name_1 = input("Trainer 1, please name yourself:\n")

  while True:
    """
    Take user input to select a pokemon for trainer #1 from the given options. 
    """
    try:
      selection = int(input(f"{Trainer_name_1}, please enter a number to select one pokemon from:\n {list_pokemons}\n"))
      if (selection > 3 or selection < 1):
        raise IndexError
        
    except ValueError:
      print("Please only choose from 1,2,3.")
    except KeyboardInterrupt:
      print("Please only choose from 1,2,3.")
    except IndexError:
      print("Please only choose from 1,2,3.")  
  
    else:
      print(list_pokemons[selection-1]+" is chosen as your representative.")
  
      break

  if selection == 1:
    pokemon = Charmander(Trainer_name_1)
  elif selection == 2:
    pokemon = Bulbasaur(Trainer_name_1)
  elif selection == 3:
    pokemon = Squirtle(Trainer_name_1)
  
  print(pokemon.__str__())
  display_stat(pokemon)

  Trainer_name_2 = input("Trainer 2, please name yourself:\n")

  while True:
    """
    Take user input to select a pokemon for trainer #2 from the given options. 
    """
    try:
      selection_2 = int(input(f"{Trainer_name_2}, please enter a number to select one pokemon from:\n {list_pokemons}\n"))
      if (selection_2 > 3 or selection_2 < 1):
        raise IndexError
        
    except ValueError:
      print("Please only choose from 1,2,3.")
    except KeyboardInterrupt:
      print("Please only choose from 1,2,3.")
    except IndexError:
      print("Please only choose from 1,2,3.")  
  
    else:
      print(list_pokemons[selection_2-1]+" is chosen as your representative.")
  
      break

  if selection_2 == 1:
    pokemon_2 = Charmander(Trainer_name_2)
  elif selection_2 == 2:
    pokemon_2 = Bulbasaur(Trainer_name_2)
  elif selection_2 == 3:
    pokemon_2 = Squirtle(Trainer_name_2)

  print(pokemon_2.__str__())
  display_stat(pokemon_2)

  
  while True:  
    """
    Take user input and apply it to the enemy pokemon's take_dmg function. Then check pokemon health and determine if there is a winner. 
    """
    while True:
      try:
        choice_of_action = int(input(f"{Trainer_name_1}, please enter a number to choose an action to perform from:\n {list_of_actions}\n"))
        if (choice_of_action > 3 or choice_of_action < 1):
            raise IndexError
            
      except ValueError:
        print("Please only choose from 1,2,3.")
      except KeyboardInterrupt:
        print("Please only choose from 1,2,3.")
      except IndexError:
        print("Please only choose from 1,2,3.")  
      
      else:
        print(list_of_actions[choice_of_action-1]+" will be carried out as your movement.")
        
        break
        
    if choice_of_action == 1:
      pokemon_2.take_dmg(pokemon.tackle())
    if choice_of_action == 2:
      pokemon_2.take_dmg(pokemon.special())
    if choice_of_action == 3:
      pokemon.Do_nothing()
  
    display_stat(pokemon_2)
  
    if pokemon_2.HP <= 0 :
      print (f"Congratulations {Trainer_name_1}! Your enemy's representative {pokemon_2.Pokemon_name} was beaten by your pokemon {pokemon.Pokemon_name}. You have won the battle with the title of \"Very Best\"! \nGood game {Trainer_name_2}! Continue striving for it and you are close to the \"Very Best\"!")
      
      break
    
    while True:
      try:
        choice_of_action_2 = int(input(f"{Trainer_name_2}, please enter a number to choose an action to perform from:\n {list_of_actions}\n"))
        if (choice_of_action_2 > 3 or choice_of_action_2 < 1):
            raise IndexError
            
      except ValueError:
        print("Please only choose from 1,2,3.")
      except KeyboardInterrupt:
        print("Please only choose from 1,2,3.")
      except IndexError:
        print("Please only choose from 1,2,3.")  
      
      else:
        print(list_of_actions[choice_of_action_2-1]+" will be carried out as your movement.")
      
        break
    
    if choice_of_action_2 == 1:
      pokemon.take_dmg(pokemon_2.tackle())
    if choice_of_action_2 == 2:
      pokemon.take_dmg(pokemon_2.special())
    if choice_of_action_2 == 3:
      pokemon_2.Do_nothing()
  
    display_stat(pokemon)
  
    if pokemon.HP <= 0 :
      print(f"Congratulations {Trainer_name_2}! Your enemy's representative {pokemon.Pokemon_name} was beaten by your pokemon {pokemon_2.Pokemon_name}. You have won the battle with the title of \"Very Best\"! \nGood game {Trainer_name_1}! Continue striving for it and you are close to the \"Very Best\"!")
      break
  
if __name__ == "__main__":
  main()