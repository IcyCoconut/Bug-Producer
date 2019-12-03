#include <stdio.h>
#include <stdbool.h>

int main() {
    bool val = true;
    
    for (int i = 0; i < 10; i ++) {
        printf("%d\t%d\n", i, val);
    }

    return 0;
}