 
#####################################################################                                                                 
 #  Team Edge objects: SUPERHERO CHALLENGES 
 # 
 #   In self challenge you are going to modify self code to do the
 #   the following below. Before you begin, walkthrough the code 
 #   with your coaches.
 #   
 #   1. Change both superhero and nemesis using same class.
 #   2. Change the variables to modify gameplay and see how it affects
 #      the game outcomes.
 #   3. Make any improvements you think would make self game better.
 #   4. Complete all the comments to demonstrate you understand the code
 #      Be specific about what each code block is doing.
 #     
 # 
 # ###############################################################/
import random
from time import sleep

print("-------------------  SUPERHERO !!  -------------------")

DELAY = 3
DAMAGE_LIMIT = 5
MAJOR_BLOW = DAMAGE_LIMIT -2
LIVES_TOP_RANGE = 60
LIVES_BOTTOM_RANGE = 40
rounds = 1
game_is_on = True

#COMMENT 1: 
class Superhero:
  def __init__(self, name=None, is_alive=None, friends=None, hit_points=None, is_good=None, attack_power=None):
      self.name = name
      self.is_alive = is_alive
      self.taunts=[]
      self.cries=[]
      self.lives = []
       
       
  def attack(self, enemy):
    global game_is_on
    #COMMENT 2 ....
    if self.is_alive and enemy.is_alive: 
        print("  \n   ")
        damage = random.randint(0,DAMAGE_LIMIT)         
        enemy.lives = enemy.lives[:len(enemy.lives) - damage]
        
        if damage >= MAJOR_BLOW:
          print("Major Blow!")
          #COMMENT 3....  
          print(f"{self.name} 💬 \: {self.taunts[random.randint(0,len(self.taunts) -1)]} \n")
          print(f"{self.name} 💥X {damage} {enemy.name} {enemy.lives} \: {len(enemy.lives)} \n")

        if len(enemy.lives) <= 0:
          #COMMENT 4....
          enemy.is_alive=False
          game_is_on=False
          print(f"💀💀💀💀💀💀 {enemy.name} has been slain!!! 💀💀💀💀💀 ")
          print("GAME OVER")
          
        if len(self.lives) <= 0:
          self.is_alive = False
          game_is_on = False
          print(f"💀💀💀💀💀💀 {self.name} has been slain!!! 💀💀💀💀💀")
          print(" GAME OVER ")


  def fill_health(self):
      #COMMENT 5....
      amt = random.randint(LIVES_BOTTOM_RANGE, LIVES_TOP_RANGE)
        
      for i in range(0, amt):
          self.lives.append("💙")

#COMMENT 6....
batman = Superhero()
batman.name="Batman 🦸‍♂️"
batman.is_alive = True 
batman.lives=[]
batman.taunts=["The Dark Knight always wins!" , "You can't hang with the bat man" , "Meet my fist, scumbag" , "You Suck!"]
batman.cries=["Ouch!" , "UFF!" , "Gaaaaaaa" , "No!!!!!"]
batman.fill_health()
 
joker = Superhero()
joker.name = "Joker 🦹‍♂️"
joker.is_alive = True
joker.lives=[]
joker.taunts =["You are a schmemer" , "Don't mess with the Joker!" , "Pick your face off the ground, you might need it!", "Getting tired of the beatings?"]
joker.cries = ["Aaaa!" , "Goh!" , "Hmph!" ,"You will pay for self"]
joker.fill_health()


print(f"{joker.name} :  {joker.lives} - {len(joker.lives)}")
print(f"{batman.name} : {batman.lives} -  {len(batman.lives)}")
print(f"{batman.name} 💬 {batman.taunts[1]}  \n")
print(f"{joker.name} 💬 {joker.taunts[1]}  \n")


#COMMENT 7....
def fight(a, b):
    global rounds

    print(" ------------- ROUND -------------> " + str(rounds))
    a.attack(b)
    b.attack(a)
    rounds += 1
  
#COMMENT 8....
while game_is_on:
    fight(batman,joker) 
    print(" \n")
    sleep(DELAY)