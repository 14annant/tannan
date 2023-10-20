#include <cs50.h>
#include <stdio.h>

int main(void)
{
// get the size of grid
int n;
do
{
    n = get_int("Size: ");
}
while (n<1);

// print grid of bricks
for (int x = 0; x<n; x++)
    {
        for(int x2 = 0; x2<n; x2++)
        {
            printf("#");
        }

     printf("\n");

    }


}