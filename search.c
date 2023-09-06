#include <stdio.h>
#include <cs50.h>
#include <string.h>

//error handling echo $? in the terminal

int main(void)
{
    //int numbers[] = {20, 500, 10, 5, 100,1,50};
    string strings[] = {"battleship", "boot", "cannon", "iron", "thumble", "top hat"};

    //int n = get_int("Number: ");
    string s = get_string("String: ");
    for (int i = 0; i < 6; i++)
    {
        //if (numbers[i] == n)
        if (strcmp(strings[i], s) == 0)
        {
            printf("Found\n ");
            //return tells the compiler the program is done 0 signifies the program came here
            return 0;
        }
    }
    printf("Not found: \n");
    //return tells the compiler the program is done 1 signifies the program came here
    return 1;
}