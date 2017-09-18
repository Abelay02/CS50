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

        //getting the key (k) from the second command line argument (argv[1]) as an integer
        string s = argv[1];
        int k = atoi (s);

        string plain = get_string("plaintext: ");


        //iterating the cypher over every letter of the string, however long it is (strlen)
        for (int chara = 0; chara < strlen(plain); chara ++)
        {

            //only running the cyper if the character is a letter
            if (isalpha(plain[chara]))
            {
                //formula for upper case letters
                if (isupper(plain[chara]))
                {
                    plain[chara] = ((plain[chara] - 65 + k) % 26) + 65;
                }

                //formula for lower case letters
                else if (islower(plain[chara]))
                {
                    plain[chara] = ((plain[chara] - 97 + k) % 26) + 97;
                }
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

