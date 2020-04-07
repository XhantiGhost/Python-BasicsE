names = ['sarah', 'John', 'bobby', 'G-Mack', 'Mosh']
print(names[2])

#Using ranages to get names
names2 = ['sarah', 'John', 'bobby', 'G-Mack', 'Mosh']
names2[0] = 'Bara'
print(names2)

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)

# 2D Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)

#List of Methods

rand_num = [1, 4, 7, 10, 11, 13]
rand_num.append(20)
rand_num.insert(0, 50)
rand_num.remove(7)
rand_num.sort()
print(rand_num)

num = [2, 2, 2, 4, 6, 4, 3, 1]
num2 = []

for number in num:
    if number not in num2:
        num2.append(number)
print(num2)