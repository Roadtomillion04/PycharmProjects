import numpy # to create large array
import time # to compare
numpy.random.seed(0)

# Naive search
def naive_search(li, target):
	for i in range(len(li)):
		if li[i] == target:
			return i
	return -1 # if not found


# Binary search
def binary_search(li:list, target, low=None, high=None): # Here we divide by half and search everytime
	assert target in li, f'The value {target} is not in the list!'
	if not low:
		low = 0
	if not high:
		high = len(li) - 1 # as index starts from 1

	midpoint = (low + high) // 2  # n/2 for even & n/2 +1 for odd

# recursion of func is faster than while loop i guess

	if li[midpoint] == target:
		return midpoint

	elif target > li[midpoint]:
		new_low = midpoint + 1
		return binary_search(li, target, new_low, high)

	else:
		#target < li[midpoint]:
		new_high = midpoint - 1
		return binary_search(li, target, low, new_high)



# Let's compare
li = numpy.sort(numpy.random.randint(1, 1000, size=(1000000,)))
target_list = li[500: 1000]

start = time.time()
for target in target_list:
	naive_search(list(li), target)
end = time.time()
print(f'Naive search time: {end - start} seconds')

start = time.time()
for target in target_list:
	binary_search(list(li), target)
end = time.time()
print(f'Binary search time: {end - start} seconds')




a, b = 5, 5
a += 5 // 2
b -= 5 // 2
print(a, b)
