def sum_nums(num1, num2):
	
	sum = num1 + num2

	return sum

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum = sum_nums(num1, num2)

print("The sum is {}".format(sum))