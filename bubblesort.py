def bubbleSort(alist):
	for passnum in range(len(alist)-1,0,-1):
		for i in range(passnum):
			if alist[i]>alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp

blist = []
done = False

while not done:
	num = input("Enter a number (or 'no' to stop): ")
	if num == "no":
		done = True
	else:
		blist.append(int(num))

bubbleSort(blist)

print(blist)