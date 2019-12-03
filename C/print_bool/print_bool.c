#include <stdio.h>
#include <stdbool.h>

int main() {
    bool horst = true;
    
    for (int i = 0; i < 10; i ++) {
        printf("%d\t%s\n", i, horst);
    }

    return 0;
}