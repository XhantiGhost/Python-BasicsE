# index = 1
#
# while index <= 10:
#     print('*' * index)
#     index = index + 1
# print("done")
#
# #For loops
#
# for item in "Python":
#     print(item)
#
# for item in ['Mosh', 'xhanti', 'sarah', 'baker']:
#     print(item)
#
# for item in [1, 2, 3, 4]:
#     print(item)
#
# for item in range(100):
#     print(item)

prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f'total: {total}')

#Nested Loops

for x in range(5):
    for y in range(5):
        print(f'({x}, {y})')

#Challenage

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    Output = ''
    for count in range(x_count):
        Output += 'x'
    print(Output)