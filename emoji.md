# Emoji

## Questions

1. TODO
4 bytes

2. TODO
A char can only store 1 byte, which is not enough to store the
Unicode for the jack-o-lantern emoji.

3.


```c
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

emoji get_emoji(string prompt)
{
    int base = 16;
    char *endptr;
    int n = strlen(prompt);
    char prompt2[n];
    prompt2[0] = '0';
    prompt2[1] = 'x';
    bool hex = false;

    //making sure that the string is of the form U+'hex values'
    while (hex == false)
    {
        prompt = get_string("Emoji code point: ");

        for (int l = 2; l < n - 1; l++)
        {
            if (isxdigit(prompt[l]) && prompt[0] == 'U' && prompt[1] == '+')
            {
                hex = true;
            }
        }
    }

    //converting from U+hex to 0xhex
    for (int l = 2; l < n; l++)
        {
            prompt2[l] = prompt[l];
        }

        //converting the hexadecimal string to an int
        long int prompt3 = strtol(prompt2, &endptr, base);

        //returning the emoji code point
        return prompt3;
}

```

## Debrief

1. TODO
https://reference.cs50.net/stdlib/strtol
http://unicode.org/emoji/charts/full-emoji-list.html

2. TODO
2 hours
