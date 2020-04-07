
try:
    person = int(input("Age: "))
    income = 20000
    risk = income / person
    print(person)
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('invalid expression')
