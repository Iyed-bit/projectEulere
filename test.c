#include <stdio.h>
#include <stdlib.h>

int main() {
    const char *myString = "22918802058777319719839450180888072429661980811197";

    // Variables for error checking
    char *endptr;
    long long myLongLong = strtoll(myString, &endptr, 10);

    // Check for conversion errors
    if (*endptr != '\0') {
        fprintf(stderr, "Conversion error: %s\n", endptr);
        return 1;
    }

    // Print the result
    printf("Converted long long: %lld\n", myLongLong);

    return 0;
}