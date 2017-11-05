start = """
You open your eyes and look around. You are not in your room. You are not in your bed.
In front of you is a simple sign with two arrows: North or South.
There is nowhere to go except for those two directions.
As you take a step forward, you hear a booming voice.
It says, 'Choose wisely if you want to survive.'
"""

print(start)
done = False
while not done:
	direction = input( "Type 'north' to go North and 'south' to go South: ")

	if direction == "north":
		done = True
		print("")
		print("You keep walking and soon arrive at the base of a mountain.")
		
		done2 = False
		while not done2:
			mountain = input("Type 'climb' to climb the mountain and 'nope' to go around it: ")

			if mountain == "climb":
				print("")
				print("You are halfway up the mountain and you run out of food.")
				done2= True
				
				done1 = False
				while not done1:
					food = input("Type 'down' to head back down and 'up' to keep going up: ")
			
					if food == "down":
						print("")
						print("While heading back down, you accidentally slip on some snow. Unfortunately, you keep rolling down and your dead body ends up at the base of the mountain.")
						print("")
						done1 = True
					elif food == "up":
						print("")
						print("Poor choice. As you kept climbing the combination of starvation and a lack of oxygen causes you to get hypoxia and die.")
						print("")
						done1 = True
					else:
						print("")
						print("Please type 'down' or 'up': ")
			
			elif mountain == "nope":
				print("")
				print("You start to try and walk around the base of the mountain. As you continue walking, you come across a cheetah.")
				done2 = True
				
				done3 = False
				while not done3:
					cheetah = input("Type 'scare' to try and scare away the cheetah and 'run' to subtly run away: ")
			
					if cheetah == "scare":
						print("")
						print("Well, at least now we know that cheetahs aren't scared of humans. Unfortunately, we figured that out after you died.")
						print("")
						done3 = True
					elif cheetah == "run":
						print("")
						print("Cheetahs are the fastet animals on ground. What would make you think running is a good idea? Sadly, you died of exhaustion after running for a minute.")
						print("")
						done3 = True
					else:
						print("")
						print("Please type 'scare' or 'run': ")
						
			else:
				print("")
				print("Please type 'climb' or 'nope': ")
	
	elif direction == 'south':
		done = True
		print("")
		print("You keep walking and soon arrive at an empty beach.")
		
		done4 = False
		while not done4:
			beach = input("Type 'swim' to go for a swim and 'sun' to sunbathe: ")
			
			if beach == "swim":
				print("")
				print("While swimming in the ocean, you come across a dead jellyfish.")
				done4 = True
			
				done5 = False
				while not done5:
					jelly = input("Type 'pick' to pick up the dead jellyfish and 'leave' to leave it alone: ")
					
					if jelly == "pick":
						print("")
						print("Dead jellyfish can still sting you, and with nobody else there to help you, you died alone with a jellyfish in your hand.")
						print("")
						done5 = True
					elif jelly == "leave":
						print("")
						print("You kept swimming and came across a shark. You tried to outswim it, but alas you were dead in less than a minute.")
						print("")
						done5 = True
					else:
						print("")
						print("Please type 'pick' or 'leave': ")
			
			elif beach == "sun":
				print("")
				print("As you were peacefully sitting in the sun, you hear a noise behind you.")
				done4 = True
		
				done6 = False
				while not done6:
					noise = input("Type 'turn' to turn around and look at the source of the noise, and 'nope' to ignore it: ")
					
					if noise == "turn":
						print("")
						print("You turn around and are immediately face-to-face with a swarm of bees. You are now proof that too many bee stings can kill you.")
						print("")
						done6 = True
					elif noise == "nope":
						print("")
						print("Yay you survived! You win the game! You made great decisions!!")
						print("")
						done6 = True
					else:
						print("")
						print("Please type 'turn' or 'nope': ")
			else:
				print("")
				print("Please type 'swim' or 'sun': ")
				
	else:
		print("")
		print("Please type 'north' or 'south': ")

print("THE END")
print("By the way, this was a dream :D")
print("")