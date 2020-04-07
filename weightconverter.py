weight = input("What is your weight? ")
unit = input(f'(L)ls or (K)kg')

if unit.upper() == "L":
    new_weight = 0.45 * float(weight)
    print(f'you are {new_weight} pounds')
elif unit.upper() == "K":
    new_weight = float(weight) / 0.45
    print(f'you are {new_weight} kilos')
print(new_weight)
