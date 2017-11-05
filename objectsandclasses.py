from random import randint
class Dog: #creates a new class Dog

    def __init__(self, name): #takes in a name for each dog created
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick): 
        self.tricks.append(trick) #takes in a trick and adds it to a list of tricks that a dog can do

d = Dog('Fido') #created a dog with name "Fido"
e = Dog('Buddy') #created a dog with name "Buddy"
d.add_trick('roll over') #dog d has the trick "roll over" added to his list of tricks
e.add_trick('play dead') #dog e has the trick "play dead" added to his list of tricks
print(d.tricks) #prints a list of dog d's tricks
print(e.tricks) #prints a list of dog e's tricks

class Pet: #creates a new class Pet

    def __init__(self, name, color, species): #takes in a name, color and species for each pet created
        self.name = name
        self.color = color
        self.species = species
        
    def getName(self):
        return self.name #if this method is called, it returns the pet's name
    
    def getColor(self):
        return self.color #returns the pet's color that was originally inputted
    
    def getSpecies(self):
        return self.species #returns the pet's species

rufus = Pet("Rufus", "pink", "naked mole rat") #creates a new pet with certain attributes
print(rufus.getName() + " is a " + rufus.getColor() + " " + rufus.getSpecies()) #prints a sentence using three different methods
print (rufus.name + " is a " + rufus.color + " " + rufus.species) #does the same thing as above

class Animal:
	
	def __init__(self, name, species):
		self.name = name
		self.species = species
	
	def getSpecies(self):
		return self.species
	
	def noise(self, noise):
		print(self.name + " " + noise + "s")
	
	def sleep(self):
		print("Zzzzzzzzzzz....")
	
	def getName(self):
		return self.name
	
	def getPrey(self):
		print(self.name + " the " + self.species + " just ate " + str(randint(1,10)) + " dead rats.")

lion = Animal("Cecil", "lion")
lion.noise("ROAR")
lion.getPrey()
lion.sleep()

human = Animal("Bob", "human")
human.noise("blah blah blah")
human.getPrey()
human.sleep()

bird = Animal("Twitter", "parrot")
bird.noise("Tweet")
bird.getPrey()
bird.sleep()

uname = input("Name an animal: ")
uspec = input("What species is the animal?: ")
unoise = input("What noise does it make: ")

ran = Animal(uname, uspec)
ran.noise(unoise)
ran.getPrey()
ran.sleep()

		