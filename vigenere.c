#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{

    //program only runs if there are 2 command line arguments
    if (argc == 2)
    {

        //getting the key from the second command line argument (argv[1]) as a string
        string key = argv[1];

        //program won't run if there is a non-letter in the second argument (key)
        for (int letter = 0; letter < strlen(key); letter ++)
        {
            if (!(isalpha(key[letter])))
            {
                printf("SMH THATS AN ERROR\n");
                return 1;
            }
        }

        int letter;

        string plain = get_string("plaintext: ");


        //iterating the cypher over every letter of the string, however long it is (strlen)
        for (int chara = 0; chara < strlen(plain); chara ++)
        {

            //making the key loop around if it is shorter than the plaintext string
            if (letter > strlen(key) - 1)
            {
                letter = 0;
            }


            //only running the cyper if the character is a letter
            if (isalpha(plain[chara]))
            {
                //formula for upper case letters
                if (isupper(plain[chara]))
                {
                    if (isupper(key[letter]))
                    {
                        plain[chara] = ((((plain[chara] + (key[letter] - 65) - 65) % 26) + 65));
                    }

                    if (islower(key[letter]))
                    {
                        plain[chara] = ((((plain[chara] + (key[letter] - 97) - 65) % 26) + 65));
                    }
                }

                //formula for lower case letters
                if (islower(plain[chara]))
                {
                    if (islower(key[letter]))
                    {
                        plain[chara] = ((((plain[chara] + (key[letter] - 97) - 97) % 26) + 97));
                    }

                    if (isupper(key[letter]))
                    {
                        plain[chara] = ((((plain[chara] + (key[letter] - 65) - 97) % 26) + 97));
                    }
                }
                letter ++;
            }

            //if character isn't a letter, leaves it as is
            else
            {
                plain[chara] = plain[chara];
            }
        }
        printf("ciphertext: %s\n", plain);
        return 0;
    }

    else
    {
        printf("SMH THATS AN ERROR\n");
    }
    return 1;
}
