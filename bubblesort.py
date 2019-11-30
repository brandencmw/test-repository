def bubble_sort(list):

	for i in range(len(list)-1):

		for j in range(len(list)-1):
			if list[j] > list[j+1]:
				temp_swap = list[j]
				list[j] = list[j+1]
				list[j+1] = temp_swap

	return list

list = [3, 6, 1, 9, 2, 6, 8]

list = bubble_sort(list)
print(list)

while True:
	print(list)
