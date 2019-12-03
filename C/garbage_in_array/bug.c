#include <stdio.h>

int main() {
    char str[10][20];

    // assign values to string
    for (int i = 0; i < 10; i ++) {
        for (int j = 0; j < 10; j ++) {
            str[i][j] = j + 48;
        }
    }

    printf("--- print values using %%c ---\n");
    for (int i = 0; i < 10; i ++) {
        printf("line %d: ", i);
        for (int j = 0; j < 20; j ++) {
            printf("%c", str[i][j]);
        }
        printf("\n");
    }

    printf("--- print values using %%s ---\n");
    for (int i = 0; i < 10; i ++) {
        printf("line %d: %s\n", i, str[i]);
    }

    return 0;
}