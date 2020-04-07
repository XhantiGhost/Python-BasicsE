def greet_user():
    print('Hi there ')
    print('Welcome aboard')


print('start  ')
greet_user()
print('finish')


# Parameters in functions

def another_greet(first_name, last_name):
    print(f'Hi {first_name}, {last_name}')
    print('Welcome aboard')


print('start  ')
another_greet('Mary', 'Smith')
another_greet('John', 'Smith')
print('finish')


# Functions that return values

def some_func(number):
    return number * number


result = some_func(3)
print(result)

# Exercise

def emojis(message):

    output = ""
    words = message.split(" ")
    emojis = {
    ':)': 'smile',
    ':(': 'sad'}
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input('>')
print( emojis(message))