#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char *s = get_string("s: ");
    if (s == NULL)
    {
        return 1;
    }

    char *t = malloc(strlen(s) + 1);
    if (t == NULL)
    {
        return 1;
    }

    strcpy(t, s);

    /* Not needeed strcpy does the same thing
    for (int i = 0; n = strlen(s) + 1, i< n ;i++)
    {
        t[i]= s[i];
    }
    */

    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    printf("s: %s\n", s);
    printf("t: %s\n", t);

    //this is good practice but is not necessary when using malloc
    free(t);

    return 0;
}