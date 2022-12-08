#include <stdio.h>
#include <cs50.h>
#include <math.h>

// q -25c, d -10c, n-5c, p -1c

int main(void)
{

    float change; //ask user about the change
    do //do this loop until you get a positive imput from a user
    {
        change = get_float("How much change is owned: "); //get_float function
    }
    while (change < 0); //positive number condition


    int convertCents = round(change * 100); //convert dollars to cents
    int coins = 0; //initial amount of coins

    while (convertCents >= 25) //loop for quaters
    {
        convertCents = convertCents - 25;
        coins++;
    }
    while (convertCents >= 10) //loop for dimes
    {
        convertCents = convertCents - 10;
        coins++;
    }
    while (convertCents >= 5) //loop for nicles
    {
        convertCents = convertCents - 5;
        coins++;
    }
    while (convertCents >= 1 && convertCents > 0) //loop for pennies
    {
        convertCents = convertCents - 1;
        coins++;
    }

    printf("%d\n", coins); //printing total amount of coins

}