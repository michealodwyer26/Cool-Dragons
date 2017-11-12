# -----------------------------------------------------------
# Cool Dragons - Mike O'Dwyer
# My take on the awesome COOL DRAGONS
#------------------------------------------------------------

import random
import time

def getDragonLocation():
	chance = random.randint(1, 2)
	
	if chance == 1:
		return "upper"
	else:
		return "lower"
		
def displayLine(line):
	for char in line:
		print(char,end="",flush=True) # end="" will not print a newline, flush = True gets the timing right
		time.sleep(delay)
		
	print()
	print()
	
def rpgFight(user_health, dragon_health):
	print()
	print("----------------------------------------------------------")
	print(" Sword Slash - 1   Run Away - 3 |    Your Health : {}    |".format(user_health))
	print(" Kick & Punch - 2               |    Dragon Health : {}  |".format(dragon_health))
	print("----------------------------------------------------------")
	print()	
	
	choice = getChoice()
	return choice
	
def runAway():
	displayLine("You start running but you trip and hit your head off a rock...")
	lost()
	
def lost():
	displayLine("YOU LOST!")
	displayLine("GAME OVER!")
	
def getChoice():
	choice = input(">>> ")
	print("\n\n\n")
	
	return int(choice)
	
def intro():
	time.sleep(1)
	
	displayLine("You are in a land full of dragons and caves...")
	displayLine("With your trusty sword by your side you look a yonder...")
	displayLine("Inside the cave awaits treasure or certain death...")
	
	frontOfCave()
	
def frontOfCave():
	print()
	time.sleep(1)
	displayLine("You are standing in front of the entrance of a cave...")
	
	chance = random.randint(1, 2)
	if chance == 1:
		displayLine("You hear the distant roar of a dragon coming from inside...")	
	else:
		displayLine("You listen for something inside but you are responded with an eerie silence...")
		
	displayLine("\nWhat will you do?\n\n1 - Go inside\n2 - Go on top of the cave\n3 - Run Away")
	
	choice = getChoice()
	if choice == 1:
		goInside()
	elif choice == 2:
		goOnTop()
	else:
		runAway()
		
def goOnTop():
	displayLine("After standing on the cave you look around you...")
	displayLine("There is nothing much around you except the odd rock")
	
	displayLine("\nWhat will you do?\n\n1 - Go back to the front of the cave\n2 - Run Away")
	
	choice = getChoice()
	if choice == 1:
		frontOfCave()
	else:
		runAway()
		
def goInside():
	displayLine("You slowly go inside and look around you...")
	displayLine("You see a large abyss in front of you...")
	displayLine("There is a slinky vine hanging down from the top of the cave...")

	displayLine("\nWhat will you do?\n\n1 - Swing by vine\n2 - Jump\n3 - Go back to the entrance")
	
	choice = getChoice()
	if choice == 1:
		swingByVine()
	elif choice == 2:
		jump()
	else:
		frontOfCave()
		
def swingByVine():
	displayLine("You nervously grab the vine and hope you\'ll make it...")
	displayLine("You step back and...")
	
	chance = random.randint(1, 6)
	if chance == 1:
		displayLine("Hopelessly fall into the abyss...")
		lost()
	else:
		displayLine("Heroically swing across the abyss!")
		lake()
		
def jump():
	displayLine("You nervously take a few steps back...")
	displayLine("You begin to run and take a leap of faith and...")
	
	chance = random.randint(1, 6)
	
	if chance == 1:
		displayLine("Hopelessly fall into the abyss of doom...")
		lost()
	else:
		displayLine("Heroically make the jump with a foot to spare!")
		lake()
		
def lake():
	print()
	displayLine("You slowly progress through the cave and you arrive at an underground lake...")
	displayLine("You look around for a way to traverse lake...")
	displayLine("You see a rotten old boat to your left...")

	displayLine("\nWhat will you do?\n\n1 - Traverse the lake by boat\n2 - Swim\n3 - Run away")
	
	choice = getChoice()
	if choice == 1:
		boat()
	elif choice == 2:
		swim()
	else:
		runAway()
		
def boat():
	displayLine("You climb into the boat to find a paddle...")
	displayLine("You begin paddling into the lake...")
	
	chance = random.randint(1, 6)
	
	if chance == 1:
		displayLine("The rotten boat begins to sink and you jump out to start swimming!")
		swim()
	else:
		displayLine("You make it to the end of the lake and jump out!")
		fork()
		
def swim():
	print()
	print()
	displayLine("You jump in and start swimming...")
	displayLine("The water is freezing...")
	
	chance = random.randint(1, 6)
	if chance == 1:
		displayLine("You begin to freeze and you can\'t swim anymore...")
		lost()
	else:
		displayLine("Incredibly you make it until the end of the lake!")
		fork()
		
def fork():
	print()
	print()
	displayLine("As you venture bravely through the cave you come upon two passages...")
	displayLine("One passage leads deeper into the cave...")
	displayLine("The other leads on to the top of the cave...")

	displayLine("\nWhat will you do?\n\n1 - Go deeper into the cave\n2 - Take the other passage to the top of the cave\n3 - Go back to the lake")
	
	choice = getChoice()
	if choice == 1:
		goDeeper()
	elif choice == 2:
		goUp()
	else:
		lake()
		
def goDeeper():
	displayLine("You slowly creep down the passage...")
	
	if dragonLocation == "lower":
		displayLine("You hear a soft growl and suddenly the dungeon is lit from the fire of the dragon!!!")
		fight()
	else:
		displayLine("To find yourself at a dead end...")
		displayLine("\nWhat will you do?\n\n1 - Go back up")
		choice = getChoice()
		if choice == 1:
			fork()
		
def goUp():
	displayLine("You climb up the steep passage and you are pleasantly exposed to increasing doses of sunshine...")
	displayLine("You finally reach the top and breathe a sigh of relief to be out of the wretched cave...")
	
	if dragonLocation == "upper":
		displayLine("Suddenly you hear a dragon roar a deafening roar!!!")
		fight()
	else:
		displayLine("You don't see much around but the weather sure is nice.")
		displayLine("\nWhat will you do?\n\n1 - Go back down into the caves\n2 - Go back toward the front of the cave via the top of the cave")
		
		choice = getChoice()
		if choice == 1:
			fork()
		elif choice == 2:
			goOnTop()
			
def fight():
	global user, dragon
	
	if user <= 0:
		youDied()
	elif dragon <= 0:
		dragonDied()
		
	choice = rpgFight(user, dragon)
	if choice == 1:
		swordSlash()
	elif choice == 2:
		kickPunch()
	else:
		runFromDragon()
		
def swordSlash():
	global user, dragon
	
	displayLine("You take your sword and swing it injuring the dragon!")
	print()
	
	dragon -= 1
	
	chance = random.randint(1, 2)
	if chance == 1:
		displayLine("The dragon is badly hurt keep fighting!")
		fight()
	else:
		hurt()
		
def kickPunch():
	displayLine("You kick and punch like a little child but the dragon dodges them all!")
	hurt()
	
def runFromDragon():
	displayLine("You shy away from the beast only to begin to stumble and fall...")
	displayLine("You hit your head off a rock...")
	lost()
	
def hurt():
	global user, dragon
	
	chance = random.randint(1, 3)
	
	if chance == 1:
		displayLine("The dragon breathes fire all over you leaving burns on you!")
		user -= 2
		fight()
	else:
		displayLine("The dragon whips you with his tail hurting you!")
		user -= 1
		fight()
		
def youDied():
	displayLine("The dragon killed you...")
	lost()
	
def dragonDied():
	displayLine("You slayed the not-so-mighty-anymore dragon!")
	won()
	
def won():
	displayLine("You won the game!")
	displayLine("You return to your hometown as a hero with as much treasure as you can carry!")
	displayLine("One day you look back on this day and think if you\'d like to do it all again...")
	displayLine("Just one more time...")
	quit()
	
dragonLocation = getDragonLocation()
delay = 0.03
user = 15
dragon = 15
intro()	
	
		
		
