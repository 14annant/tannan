#include <stdio.h>
#include <stdlib.h>
//valgrind in the terminal this will tell you if there is memory loss


int main (void)
{
    int *x = malloc(3 * sizeof(int));

    // this is good practice
    if (x == NULL)
    {
        return 0;
    }
    
    x[0]= 20;
    x[1] = 50;
    x[2] = 60;

    free();
    return 1;
}