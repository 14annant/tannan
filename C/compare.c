#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x = get_int("whats x? ");
    int y = get_int("whats y? ");

    if (x < y)
    {
        printf("x: %i is less then y: %i\n",x,y);
    }
    else if (x > y)
    {
       printf("x: %i is greater then y: %i\n", x,y);
    }
    else
    {
        printf("x is equal to y %i\n",x);
    }
}