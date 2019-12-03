#include <stdio.h>
#include <stdbool.h>

#define horst

int main() {
    bool val = true;
    
    for (int i = 0; i < 10; i ++) {
        printf("%d\t%s\n", i, val);
    }

    return 0;
}