#include <cs50.h>
#include <string.h>
#include <stdio.h>

typedef struct
{
    string name;
    string number;
}
person;

int main(void)
{
    person people[2];

    people[0].name = "Tom";
    people[0].number = "1-508-840-1000";

    people[1].name = "John";
    people[1].number = "1-508-840-1111";


    string n = get_string("Search Name: ");
    for (int i = 0; i < 2; i++)
    {

        if (strcmp(people[i].name, n) == 0)
        {
            printf("Found: %s\n", people[i].number);
            return 0;
        }

    }
    printf("Not Found\n");
    return 1;
    /*
    FILE *file = fopen("phonebook.csv", "a");

    string name = get_string("Name: ");
    string number = get_string("Number: ");

    fprintf(file, "%s,%s\n", name, number);

    fclose(file);
    */
}










/*
old code (simple)
int main(void)
{
    string names[] = {"Tom White", "John Brown"};
    string phonenumbers[] = {"1-508-840-1000", "1-508-840-1111"};

    string n = get_string("Search Name: ");
    for (int i = 0; i < 2; i++)
    {

        if (strcmp(names[i], n) == 0)
        {
            printf("Found: %s\n", phonenumbers[i]);
            return 0;
        }

    }
    printf("Not Found\n");
    return 1;
}*/