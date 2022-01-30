#my_file = open("test.txt")

#print(my_file.read()) #remeber you can read file only one time

#because the cursor moves to end of the line
# to read mulltiple times
#my_file.seek(0)
#print(my_file.read())

#my_file.seek(0)
#print(my_file.read()) 

#my_file.seek(0)
#print(my_file.readline())

#my_file.seek(0)
#print(my_file.readlines())

#my_file.close()

#instead - Now no need to close the file
'''read'''
#with open("test.txt", mode='r') as my_file:
#	print(my_file.readlines())

'''read/write''' #you only will overwrite the existing words because read cursor resets everytime you open and read/write
#with open("test.txt", mode='r+') as my_file:
#	text = my_file.write(";D")
#	print(text)

'''append''' # appends at end
#with open("test.txt", mode="a") as my_file:
#	text = my_file.write(";D")

'''write'''
with open("test.txt", mode="w") as my_file:
	text = my_file.write("Now only writing!")

#write and append mode creates new file if dosen't exists
with open("sad.txt", mode="a") as new_file:
	new_file.write("I/'m sad :-(")

