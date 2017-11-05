def color_list(lists):
	colors = {}
	
	for item in lists:
		if item not in colors.keys():
			colors[item] = 1
		else:
			colors[item] += 1
	
	keys = colors.keys()
	print("")
	print(keys)
	print("")
	
	values = colors.values()
	print(values)
	print("")
	
	for k, v in colors.items():
		print(k, v)
	print("")
	
	maxv = max(colors.values())
	keyv = [k for k, v in colors.items() if v == maxv]
	print("Your favorite color(s) is/are: ")
	print(keyv)
	return

listocolors=[]
done = False

while not done:
	input_color = input("Enter a color (or 'no' to stop): ")
	if input_color == "no":
		done = True
	else:
		listocolors.append(input_color)

color_list(listocolors)

