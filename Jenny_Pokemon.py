# Jiayin(Jenny) Yu, March 26th 2023

import random

class Jenny_Pokemon():
  """
  This is the parent class of all 3 pokemons. It sets up the common attribute of SPATK Modifier and method of Do Nothing that these pokemons share. 
  """
  def __init__(self):
    """
    This function defines the attribute of SPATK Modifier for the class of Jenny_Pokemon. 
    """
    self.SPATK_modifier = 5
    
  def Do_nothing(self):
    """
    This function defines the method of Do Nothing for the class of Jenny_Pokemon. 
    """
    print("You pokemon did nothing and both pokemon stats remain unchanged.")
    pass
  
  

class Charmander(Jenny_Pokemon):
  """
  This is a child class of Jenny_Pokemon called Charmander. It sets up some basic attributes of Charmander and its tackle, SPATK, and taking-damage calculation methods. 
  """
  def __str__(self):
    """
    Call this function to print the self-introduction of Charmander Pokemon. 
    """
    return("This is Charmander！I’m absolutely the cuttest with iconic orange skin:)")
  
  def __init__(self, name):
    super().__init__()
    self.Trainer = name
    self.Pokemon_name = "Charmander"
    self.Type = "Fire"
    self.HP = random.randint(37, 42)
    self.ATK = 17
    self.SPATK = 21
    self.DEF = 12
    self.SPDEF = 17

  
  def tackle(self):
    """
    This function takes no input and returns 2 outputs of "normal attack" and the ATK of Charmander.
    """
    return "normal attack", self.ATK
  
  def special(self):
    """
    This function takes no input and returns 3 outputs of "special attack", the SPATK, and the type of Charmander.
    """
    return "special attack", self.SPATK, self.Type
   
  def take_dmg(self, incoming_damage):
    """
    This function takes the incoming attack as input and justifies whether it is a "normal attack", "not very effective special attack", or "super effective special attack". Then it does the damage calculation to modify the current Charmander
status.
    """
    if (incoming_damage[0] == "normal attack"):
      print("This is a normal attack.")
      self.HP = self.HP - (incoming_damage[1] - self.DEF)
      
    elif (incoming_damage[0] == "special attack"):
      print("This is a special attack.")
      if (incoming_damage[2] == "Fire" or incoming_damage[2] == "Grass & Poison"):
        print("Not very effective")
        self.HP = self.HP - (incoming_damage[1] - self.SPDEF - self.SPATK_modifier)
      elif (incoming_damage[2] == "Water" ):
        print("Super effective")
        self.HP = self.HP - (incoming_damage[1] - self.SPDEF + self.SPATK_modifier)


class Bulbasaur(Jenny_Pokemon):
  """
  This is a child class of Jenny_Pokemon called Bulbasaur. It sets up some basic attributes of Bulbasaur. 
  """
  def __str__(self):
    """
    Call this function to print the self-introduction of Bulbasaur Pokemon. 
    """
    return("This is Bulbasaur！I’m one hundred percent the most stylish guy because my green is in trend this year! Let's shame our enemy aesthetically at first sight!")
    
  def __init__(self, name):
    super().__init__()
    self.Trainer = name
    self.Pokemon_name = "Bulbasaur"
    self.Type = "Water"
    self.HP = random.randint(43, 48)
    self.ATK = 15
    self.SPATK = 23
    self.DEF = 13
    self.SPDEF = 16
    
  def tackle(self):
    """
    This function takes no input and returns 2 outputs of "normal attack" and the ATK of Bulbasaur.
    """
    return "normal attack", self.ATK
  
  def special(self):
    """
    This function takes no input and returns 3 outputs of "special attack", the SPATK, and the type of Bulbasaur.
    """
    return "special attack", self.SPATK, self.Type
   
  def take_dmg(self, incoming_damage):
    """
    This function takes the incoming attack as input and justifies whether it is a "normal attack", "not very effective special attack", or "super effective special attack". Then it does the damage calculation to modify the current Bulbasaur
status.
    """
    if (incoming_damage[0] == "normal attack"):
      print("This is a normal attack.")
      self.HP = self.HP - (incoming_damage[1] - self.DEF)
      
    elif (incoming_damage[0] == "special attack"):
      print("This is a special attack.")
      if (incoming_damage[2] == "Water" or incoming_damage[2] == "Fire"):
        print("Not very effective")
        self.HP = self.HP - (incoming_damage[1] - self.SPDEF - self.SPATK_modifier)
      elif (incoming_damage[2] == "Grass & Poison") :
        print("Super effective")
        self.HP = self.HP - (incoming_damage[1] - self.SPDEF + self.SPATK_modifier)


        
class Squirtle (Jenny_Pokemon):
  """
  This is a child class of Jenny_Pokemon called Squirtle. It sets up some basic attributes of Squirtle. 
  """
  def __str__(self):
    """
    Call this function to print the self-introduction of Squirtle Pokemon. 
    """
    return("This is Squirtle！I’m no doubt the best defenser!")
    
  def __init__(self, name):
    super().__init__()
    self.Trainer = name
    self.Pokemon_name = "Squirtle"
    self.Type = "Grass & Poison"
    self.HP = random.randint(42, 47)
    self.ATK = 16
    self.SPATK = 22
    self.DEF = 13
    self.SPDEF = 15


  def tackle(self):
    """
    This function takes no input and returns 2 outputs of "normal attack" and the ATK of Squirtle.
    """
    return "normal attack", self.ATK
  
  def special(self):
    """
    This function takes no input and returns 3 outputs of "special attack", the SPATK, and the type of Squirtle.
    """
    return "special attack", self.SPATK, self.Type
   
  def take_dmg(self, incoming_damage):
    """
    This function takes the incoming attack as input and justifies whether it is a "normal attack", "not very effective special attack", or "super effective special attack". Then it does the damage calculation to modify the current Squirtle
status.
    """
    if (incoming_damage[0] == "normal attack"):
      print("This is a normal attack.")

      self.HP = self.HP - (incoming_damage[1] - self.DEF)

    elif incoming_damage[0] == "special attack":
      print("This is a special attack.")

      if (incoming_damage[2] == "Water" or incoming_damage[2] == "Grass & Poison"):
        print("Not very effective")
        self.HP = self.HP - (incoming_damage[1] - self.SPDEF - self.SPATK_modifier)
      elif (incoming_damage[2] == "Fire") :
        print("Super effective")
        self.HP = self.HP - (incoming_damage[1] - self.SPDEF + self.SPATK_modifier)
             
  
    