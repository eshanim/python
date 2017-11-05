class Dog():
	def __init__(self, furColor):
		self.furColor = furColor
	
	def bark(self):
		print("Woof!")
		
	def returnFurColor(self):
		return self.furColor
		
		
class GermanShepard(Dog):
	def __init__(self, furColor, eyeColor, isPoliceDog):
		Dog.__init__(self, furColor)
		self.eyeColor = eyeColor
		self.isPoliceDog = isPoliceDog
	
	def protect(self, whoIsProtected):
		print(whoIsProtected + " is being protected.")
