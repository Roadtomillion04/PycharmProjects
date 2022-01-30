# to acess  different directory just give name of folder
# ./ means from curent parent  folder 
#../ means like cd ..

try:
	with open("./filepath\sads.txt", mode="x") as new_file:
		print(new_file.read())

except FileNotFoundError as err:
	print("FileNotFoundError")
	raise err

except IOError as err:
	print("when machine has fault")
	raise err

except UnsupportedOperation as err:
	print("FileNotFoundError")
	raise err