def bubble_sort(list):

	for i in range(len(list)-1):

		for j in range(len(list)-1):
			if list[j] > list[j+1]:
				temp_swap = list[j]
				list[j] = list[j+1]
				list[j+1] = temp_swap

	return list

list = input("Enter the set of numbers to be sorted separated by spaces.").split()

list = bubble_sort(list)
print(list)

while True:
	print(list)
