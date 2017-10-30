from cs50 import get_float

# reprompting user until input is a positive numerical value
while True:
    print("change owed: ", end="")
    change = get_float()

    if change > 0:
        break

# converting change from dollars to cents
cents = int(change * 100)

# number of whole quarters that can go into change value
quarters = cents // 25
cents = cents % 25

# number of whole dimes that can go into remaining change value
dimes = cents // 10
cents = cents % 10

# number of whole nickels that can go into remaining change value
nickels = cents // 5
cents = cents % 5

pennies = cents

coins = quarters + dimes + nickels + pennies
print(coins)
