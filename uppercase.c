#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

int main (void)
{
    string name = get_string("Before: ");
    printf("After ");

    for(int i = 0, x = strlen(name); i < x  ; i++)
    {
        printf("%c", toupper(name[i]));
    }
    printf("\n");
}