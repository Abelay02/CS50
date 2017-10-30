from cs50 import get_string
import sys

key = int(sys.argv[1])

# making sure that the correct number of command line arguments exists
if (len(sys.argv) != 2):
    print("error")
    exit(1)

# prompting user for plaintext string
print("plaintext: ", end="")
string = get_string()
string2 = ""

for i in range(len(string)):

    if string[i].isalpha():

        # algoritm for enciphering uppercase letters
        if string[i].isupper():
            string2 += chr(((ord(string[i]) - 65 + key) % 26) + 65)

        # algorithm for enciphering lowercase letters
        if string[i].islower():
            string2 += chr(((ord(string[i]) - 97 + key) % 26) + 97)

    else:
        string2 += string[i]

print("ciphertext:", string2)
