number = (1, 2, 3, 4)
print(number[0])

# Dictionaries

customer = {
    "Name": "John Smith",
    "Age": 40,
    "is_varified": True

}
print(customer["Name"])
print(customer.get('age', 'Jan 1 2020'))

#Exercise
phone = input('Phone: ')

dic = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four'
}
output = ""
for ch in phone:
    output += dic.get(ch, '!') + " "
print(output)


#Exercise2

message = input('>')
words = message.split(" ")

emojis = {
    ':)': ''
}

