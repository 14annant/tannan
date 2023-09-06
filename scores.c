#include <stdio.h>
#include <cs50.h>

const int N = 3;

float average(int length, int array[]);



int main (void)
{
    int scores[N];

    for (int i = 0; i<N; i++)
    {
        scores[i] = get_int("type score");
    }

    printf("Average score: %f\n", average(N, scores));

}

float average(int length, int array[])
{
    int sum = 0;
    for (int i = 0; i < N; i++ )
    {
        sum = sum + array[i];
    }
    return sum / (float) N;
}