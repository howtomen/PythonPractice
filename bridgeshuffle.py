


print("Welcome to Bridge Shuffle, Enter two list:\n")
input_string = input("Enter a list of Numbers or letters seperated by spaces:")
input_string2 = input("Enter a second list of Numbers or letters seperated by spaces:")

list1 = input_string.split()
list2 = input_string2.split()

list1_longer = False

if len(list1) > len(list2):
	ShuffleConstant = len(list2)
	remainder = len(list1)
	list1_longer = True
else:
	ShuffleConstant = len(list1)
	remainder = len(list2)

NewList = list()
for x in range(ShuffleConstant):
	NewList.append(list1[x])
	NewList.append(list2[x])

for x in range(ShuffleConstant, remainder):
	if list1_longer == True:
		NewList.append(list1[x])
	else:
		NewList.append(list2[x])

print("Here is the new list: \n", NewList)