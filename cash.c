#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float change;
    do
    {
        printf("Change owed:");
        change = get_float();
    }

    //Converting floating point dollars to integer cents
    while (change < 0);
    int cents = round(change * 100);

    int coins = 0;

    //Can quarters be used?
    while (cents >= 25)
    {
        cents = cents - 25;
        coins++;
    }

    //Can dimes be used?
    while (cents >= 10)
    {
        cents = cents - 10;
        coins++;
    }

    //Can nickels be used?
    while (cents >= 5)
    {
        cents = cents - 5;
        coins++;
    }

    //Can pennies be used?
    while (cents >= 1)
    {
        cents = cents - 1;
        coins++;
    }
    printf("%i\n", coins);
}