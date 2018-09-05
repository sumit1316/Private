file1 = open("test1.py", "w")
for x in range(1,11):
	print("Please enter the", x, "line : ")
	y=input()
	file1.write(y+"\n")
file1.close()
file1 = open("test1.py", "r")
print(file1.read())


#file1.write(data+"\n")