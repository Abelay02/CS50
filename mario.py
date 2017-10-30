from cs50 import get_int

# reprompts user to give an int value between 0 and 23
while True:
    print("height: ", end="")
    height = get_int()

    if height >= 0 and height < 24:
        break

for i in range(height):

    # does not print a newline after printing spaces, waits for hashes
    print(" " * (height - 1 - i), end="")
    print("#" * (2 + i))
