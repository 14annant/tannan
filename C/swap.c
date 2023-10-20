#include <stdio.h>
#include <stdlib.h>
//& means the address of something
//* means it is a pointer to something

void swap (int *a, int *b);

int main (void)
{
    int x = 1;
    int y = 2;

    printf("x is %i, y is %i \n", x, y);
    swap(&x, &y);
    printf("Now x is %i, y is %i \n", x, y);
}

void swap (int *a, int *b)
{

    int tmp = *a;
    *a = *b;
    *b = tmp;

}