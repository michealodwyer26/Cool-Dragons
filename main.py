# -----------------------------------------------------------
# Cool Dragons - Mike O'Dwyer
# My take on the awesome COOL DRAGONS
#------------------------------------------------------------

import random
import time
import sys

def display_line(line):
	for char in line:
		print(char,end="",flush=True) # end="" will not print a newline, flush = True gets the timing right
		time.sleep(0.03)
		
	print()
	print()
	
def rpg_fight(user_health, dragon_health):
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
	
	choice = get_choice()
	
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
	
	on_top2 = "There is nothing much around you except the odd rock"
	display_line(on_top2)
	
	on_top3 = """
What will you do?

1 - Go back to the front of the cave
2 - Run Away"""
	display_line(on_top3)
	
	choice = get_choice()
	
	if choice == 1:
		front_of_cave()
	else:
		run_away()
		
def go_inside():
	inside1 = "You slowly go inside and look around you..."
	display_line(inside1)
	
	inside2 = "You see a large abyss in front of you..."
	display_line(inside2)
	
	inside3 = "There is a slinky vine hanging down from the top of the cave..."
	display_line(inside3)
	
	inside4 = """
What will you do?

1 - Swing by vine
2 - Jump
3 - Go back to the entrance"""
	display_line(inside4)
	
	choice = get_choice()
	
	if choice == 1:
		swing_by_vine()
	elif choice == 2:
		jump()
	else:
		front_of_cave()
		
def swing_by_vine():
	vine1 = "You nervously grab the vine and hope you\'ll make it..."
	display_line(vine1)
	
	vine2 = "You step back and..."
	display_line(vine2)
	
	var = random.randint(1, 6)
	
	if var == 1:
		vine3 = "Hopelessly fall into the abyss..."
		display_line(vine3)
		
		lost()
		
	else:
		vine3 = "Heroically swing across the abyss!"
		display_line(vine3)
		
		lake()
		
def jump():
	jump1 = "You nervously take a few steps back..."
	display_line(jump1)
	
	jump2 = "You begin to run and take a leap of faith and..."
	display_line(jump2)
	
	var = random.randint(1, 6)
	
	if var == 1:
		jump3 = "Hopelessly fall into the abyss of doom..."
		display_line(jump3)
		
		lost()
		
	else:
		jump3 = "Heroically make the jump with a foot to spare!"
		display_line(jump3)
		
		lake()
		
def lake():
	print()
	
	lake1 = "You slowly progress through the cave and you arrive at an underground lake..."
	display_line(lake1)
	
	lake2 = "You look around for a way to traverse lake..."
	display_line(lake2)
	
	lake3 = "You see a rotten old boat to your left..."
	display_line(lake3)
	
	lake4 = """
What will you do?
	
1 - Traverse the lake by boat
2 - Swim 
3 - Run away"""
	display_line(lake4)
	
	choice = get_choice()
	
	if choice == 1:
		boat()
		
	elif choice == 2:
		swim()
		
	else:
		run_away()
		
def boat():
	boat1 = "You climb into the boat to find a paddle..."
	display_line(boat1)
	
	boat2 = "You begin paddling into the lake..."
	display_line(boat2)
	
	chance = random.randint(1, 6)
	
	if chance == 1:
		boat3 = "The rotten boat begins to sink and you jump out to start swimming!"
		display_line(boat3)
		
		swim()
		
	else:
		boat3 = "You make it to the end of the lake and jump out!"
		display_line(boat3)
		
		fork()
		
def swim():
	print()
	print()
	
	swim1 = "You jump in and start swimming..."
	display_line(swim1)
	
	swim2 = "The water is freezing..."
	display_line(swim2)
	
	chance = random.randint(1, 6)
	
	if chance == 1:
		swim3 = "You begin to freeze and you can\'t swim anymore..."
		display_line(swim3)
		
		lost()
		
	else:
		swim3 = "Incredibly you make it until the end of the lake!"
		display_line(swim3)
		
		fork()
		
def fork():
	print()
	print()
	
	fork1 = "As you venture bravely through the cave you come upon two passages..."
	display_line(fork1)
	
	fork2 = "One passage leads deeper into the cave..."
	display_line(fork2)
	
	fork3 = "The other leads on to the top of the cave..."
	display_line(fork3)
	
	fork4 = """
What will you do?
	
1 - Go deeper into the cave
2 - Take the other passage to the top of the cave
3 - Go back to the lake"""
	display_line(fork4)
	
	choice = get_choice()
	
	if choice == 1:
		go_deeper()
	elif choice == 2:
		go_up()
	else:
		lake()
		
def go_deeper():
	go_deep1 = "You slowly creep down the passage..."
	display_line(go_deep1)
	
	if dragon_location == "lower":
		go_deep2 = "You hear a soft growl and suddenly the dungeon is lit from the fire of the dragon!!!"
		display_line(go_deep2)
		
		fight()
		
	else:
		go_deep2 = "To find yourself at a dead end..."
		display_line(go_deep2)
		
		go_deep3 = """
What will you do?
		
1 - Go back up"""
	choice = get_choice()
	
	if choice == 1:
		fork()
		
def go_up():
	goup1 = "You climb up the steep passage and you are pleasantly exposed to increasing doses of sunshine..."
	display_line(goup1)
	
	goup2 = "You finally reach the top and breathe a sigh of relief to be out of the wretched cave..."
	display_line(goup2)
	
	if dragon_location == "upper":
		goup3 = "Suddenly you hear a dragon roar a deafening roar!!!"
		display_line(goup3)
		
		fight()
		
	else:
		goup3 = "You don\'t see much around but the weather sure is nice."
		display_line(goup3)
		
		goup4 = """
What will you do? 
		
1 - Go back down into the caves
2 - Go back toward the front of the cave via the top of the cave"""
		display_line(goup4)
		
		choice = get_choice()
		
		if choice == 1:
			fork()
		
		elif choice == 2:
			go_on_top()
			
def fight():
	global user, dragon
	
	if user <= 0:
		you_died()
		
	elif dragon <= 0:
		dragon_died()
		
	choice = rpg_fight(user, dragon)
	
	if choice == 1:
		sword_slash()
	elif choice == 2:
		kick_punch()
	else:
		run_from_dragon()
		
def sword_slash():
	global user, dragon
	
	sword_slash1 = "You take your sword and swing it injuring the dragon!"
	display_line(sword_slash1)
	
	dragon -= 1
	
	print()
	
	chance = random.randint(1, 2)
	
	if chance == 1:
		sword_slash2 = "The dragon is badly hurt keep fighting!"
		display_line(sword_slash2)
		
		fight()
		
	else:
		hurt()
		
def kick_punch():
	kick_punch1 = "You kick and punch like a little child but the dragon dodges them all!"
	display_line(kick_punch1)
	
	hurt()
	
def run_from_dragon():
	run_from_dragon1 = "You shy away from the beast only to begin to stumble and fall..."
	display_line(run_from_dragon1)
	
	run_from_dragon2 = "You hit your head off a rock..."
	display_line(run_from_dragon2)
	
	lost()
	
def hurt():
	global user, dragon
	
	chance = random.randint(1, 3)
	
	if chance == 1:
		hurt1 = "The dragon breathes fire all over you leaving burns on you!"
		display_line(hurt1)
		user -= 2
		
		fight()
		
	else:
		hurt1 = "The dragon whips you with his tail hurting you!"
		display_line(hurt1)
		
		user -= 1
		fight()
		
def you_died():
	died1 = "The dragon killed you..."
	display_line(died1)
	
	lost()
	
def dragon_died():
	died1 = "You slayed the not-so-mighty-anymore dragon!"
	display_line(died1)
	
	won()
	
def won():
	won1 = "You won the game!"
	display_line(won1)
	
	won2 = "You return to your hometown as a hero with as much treasure as you can carry!"
	display_line(won2)
	
	won3 = "One day you look back on this day and think if you\'d like to do it all again..."
	display_line(won3)
	
	won4 = "Just one more time..."
	display_line(won4)
	
	sys.exit()
	
dragon_location = "lower"
user = 15
dragon = 15
go_deeper()
	
	
		
		
