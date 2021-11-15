#include <cstdio>
int main (int argc, char **argv)
{
    int result = 0; 
    char *c = argv[1];  
    while(*c != 0)
    { 
        result *= 10;           
        result += (*c - 48);
        c++;    
    }
printf("%d\n", result);
}
