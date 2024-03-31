#Names: Matthew Fehr and Tin Nguyen
#Date: 10/9/23
#Description: Makes a game where a hero fights against three dragons

import dragon
import fire_dragon
import flying_dragon
import hero
import random
import check_input

def main():
  #create the dragons and the hero
  name = input("What is your name, challenger?\n")
  print(f"Welcome to dragon training, {name}")
  print("You must defeat 3 dragons.")
  the_hero = hero.Hero(name, 50)
  dragons = [dragon.Dragon("Deadly Nadder", 10), fire_dragon.FireDragon("Gronckle", 15), flying_dragon.FlyingDragon("Timberjack", 20)]

  #loop the game
  cont = True
  while cont:
    #print the heros health and dragon attack options
    print()
    print(the_hero)
    for i in range(len(dragons)):
      print(f"{i+1}. Attack {dragons[i]}")

    #choose the dragon to attack, the weapon and attack the dragon
    d_choice = check_input.get_int_range("Choose a dragon to attack: ",1, len(dragons))
    print()
    print("Attack with:")
    print("1. Sword (2 D6)")
    print("2. Arrow (1 D12)")
    w_choice = check_input.get_int_range("Enter weapon: ",1,2)
    print()
    if w_choice == 1:
      print(the_hero.basic_attack(dragons[d_choice-1]))
    else:
      print(the_hero.special_attack(dragons[d_choice-1]))

    #if dragon dies remove, then pick the attacking dragon and its attack
    if dragons[d_choice-1].hp <= 0:
      dragons.remove(dragons[d_choice-1])
    d_attack = random.randint(0,len(dragons)-1)
    d_move = random.randint(1,2)
    if d_move == 1:
      print(dragons[d_attack].basic_attack(the_hero))
    else:
      print(dragons[d_attack].special_attack(the_hero))

    #if hero dies or all the dragons die, end the game
    if the_hero.hp <= 0:
      print()
      print("You died.")
      cont=0
    elif len(dragons)==0:
      print()
      print("Congratulations! You have defeated all 3 dragons, you have passed the trials.")
      cont = 0

main()