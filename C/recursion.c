#include <cs50.h>
#include <stdio.h>

void draw(int n);

int main(void)
{
    int num = get_int("Number: ");
    draw(num);
}

void draw(int n)
{
    if (n <= 0)
    {
        return;
    }

    //this makes this it recursive
    draw(n - 1);

    for (int i = 0; i < n; i++)
    {
        printf("#");
    }
    printf("\n");
}