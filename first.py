#basic strings
name = 'John Smith';
age = 20;
is_New = True;
print(is_New);
name1 = input('what is your name: ');
color = input('What is your fav color? ');
print(name1 + ' likes ' + color);

weight = input('how much is your weight? ');
new_weight = float(weight) * 0.45;
print(new_weight);

# Condition statements
is_cold = False;
is_hot = False;

if is_cold:
    print('what the fuck')
elif is_hot:
    print("what the actual fuck though")
else:
    print('damn')

house_price = 100000;
credit = True;

if credit:
    down_payment = 0.1 * house_price
else:
    down_payment = 0.2 * house_price
print(f'Down payment: ${down_payment}');

name = 51
if name < 3:
    print('name must be atleast 3 characters long')
elif name > 50:
    print('name must have max 50 characters')
else:
    print('name looks good')


name = "Jacob"

if len(name) < 3:
    print('name must be atleast 3 characters long')
elif len(name) > 50:
    print('name must have max 50 characters')
else:
    print('name looks good')

