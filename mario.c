#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height;
    do
    {
        printf("Height: ");
        height = get_int();
    }
    while (height < 0 || height > 23);

    for (int row = 0; row < height; row++)
    {
        //printing spaces
        for (int k = 0; k < height - row - 1; k++)
        {
            printf(" ");
        }

        //printing hashes
        for (int j = 0; j < row + 2; j++)
        {
            printf("#");
        }

        printf("\n");
    }
}
