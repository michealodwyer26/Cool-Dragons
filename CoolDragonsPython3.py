# -----------------------------------------------------------
# Cool Dragons - Mike O'Dwyer
# My take on the awesome COOL DRAGONS
#------------------------------------------------------------

import random
import time
import sys

def display_line(line):
	for char in line:
		print(i,end='')
		time.sleep(0.0075)
		
	print()
	print()
	
def rpg_fight(user_helath, dragon_health):
	blank = ""
	border = "----------------------------------------------------------"
	line10 = " Sword Slash - 1   Run Away - 3 |    Your Health : {}    |".format(user_health)
	line20 = " Kick & Punch - 2               |    Dragon Health : {}  |".format(dragon_health)
	
	print(blank)
	print(border)
	print(line10)
	print(line20)
	print(border)
	print(blank)
	
	choice = get_choice
	
	return choice
	
def run_away():
	run_away1 = "You start running but you trip and hit your head off a rock..."
	display_line(run_away1)
	
	lost()
	
def lost():
	msg = "YOU LOST!"
	display_line(msg)
	
	msg2 = "GAME OVER!"
	display_line(msg2)
	
def get_choice():
	choice = input(">>> ")
	
	print()
	print()
	print()
	
	return int(choice)
	
def intro():
	time.sleep(1)
	
	intro1 = "You are in a land full of dragons and caves..."
	display_line(intro1)
		
	intro2 = "With your trusty sword by your side you look a yonder..."
	display_line(intro2)
	
	intro3 = "Inside the cave awaits treasure or certain death..."
	display_line(intro3)
	
	front_of_cave()
	
def front_of_cave():
	print()
	
	time.sleep(1)
	
	front1 = "You are standing in front of the entrance of a cave..."
	display_line(front1)
	
	chance = random.randint(1, 2)
	
	if chance == 1:
		front2 = "You hear the distant roar of a dragon coming from inside..."
		display_line(front2)
		
	else:
		front2 = "You listen for something inside but you are responded with an eerie silence..."
		display_line(front2)
		
	front3 = """
What will you do?
	
1 - Go inside
2 - Go on top of the cave
3 - Run Away"""

	display_line(front3)
	
	choice = get_choice()
	
	if choice == 1:
		go_inside()
	elif choice == 2:
		go_on_top()
	else:
		run_away()
		
def go_on_top():
	on_top1 = "After standing on the cave you look around you..."
	display_line(on_top1)
	
	on_top1 = "There is nothing much around you except the odd rock"
	display_line(on_top2)

	
