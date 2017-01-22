#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <cs50.h>
int main(int argc, char const *argv[])
{
	int counter = 0;
    char *input = get_string();
    char *token = strtok(input," ");
    char *prefix = "";
    int found = 0  ;
    if(input == NULL)
        {
        printf("There is no box");
        return 1;
       }
        
	while(token != NULL)
	{

		    counter = counter + 1;
			if (strcmp(token,"cat") == 0 )
			{
                found = found + 1;
				if(counter % 10 == 1 & counter < 100)
                {
                    prefix = "st";
                    printf("The cat is the %d%s item in the box",counter,prefix);
                }
                else if(counter % 10 == 2 && counter < 100)
                 {
                    prefix = "nd";
                    printf("The cat is the %d%s item in the box",counter,prefix);
                    
                }
                 else if(counter % 10 == 3 && counter < 100)
                 {
                    prefix = "rd";
                    printf("The cat is the %d%s item in the box",counter,prefix);
                    
                }
                else if(counter > 100 && counter % 100 < 100)
                {
                    prefix = "th";
                    printf("The cat is the %d%s item in the box",counter,prefix);
                    
                }
               
           
			}
       
		token = strtok(NULL, " ");
	}
    if(found == 0)
        {
        printf("No cat yet");
    }
	return 0;
}