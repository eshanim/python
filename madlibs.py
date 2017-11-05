"""
Make sure your lunch is (adj1) and (adj2), because the school cafeteria's food is (adj3).
Their burgers are (color1), fried in (noun) and made of (animal1) meat.
Instead of eating that, you could eat a sandwich made of (vegetable) and (animal2) meat.
Drink (color2) milk, instead of (adj4) sodas.
"""

adj1 = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
adj3 = input("Enter another adjective: ")
adj4 = input("Enter another adjective: ")

color1 = input("Enter a color: ")
color2 = input("Enter another color: ")

noun1 = input("Enter a noun: ")

animal1 = input("Enter an animal: ")
animal2 = input("Enter another animal: ")

vegetable1 = input("Enter a vegetable (plural): ")

line1 = "Make sure your lunch is " + adj1 + " and " + adj2 + ", because the school cafeteria's food is " + adj3 + ". "
line2 = "Their burgers are " + color1 + ", fried in " + noun1 + " and made of " + animal1 + " meat. "
line3 = "Instead of eating that, you could eat a sandwich made of " + vegetable1 + " and " + animal2 + " meat. "
line4 = "Drink " + color2 + " milk, instead of " + adj4 + " sodas."

print( line1 + line2 + line3 + line4)