Tinclude <string.h>
#include <ctype.h>
#include <cs50.h>
int main(int argc, char const *argv[])
{
    int counter = 0;
    char *input = get_string();
    char *token = strtok(input," ");
    if(input == NULL)
    {
       printf("There is no box");
    }
        
	while(token != NULL)
	{

		  counter = counter + 1;
			if (strcmp(token,"cat") == 0 )
			{
				printf("The cat is the %d item in the box",counter);
			}

		token = strtok(NULL, " ");
	}
	return 0;
} 
