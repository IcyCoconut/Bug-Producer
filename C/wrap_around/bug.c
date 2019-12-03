#include <stdio.h>

int main()
{
    int board[5][5];

    // initialize
    for (int i = 0; i < 25; i ++) {
        board[i/5][i%5] = 0;
    }

    /*
    Expect: (wrap around edge)
     5 24 18 12  6
    10  4 23 17 11
    15  9  3 22 16
    20 14  8  2 21
    25 19 13  7  1
    */

    int x = 4, y = 4;

    for (int i = 1; i < 26; i ++) {
        board[x][y] = i;
        x = (x - 1) % 5;
        y = (y - 1) % 5;
        if (i%5 == 0) {
            x = (x + 1) % 5;
        }
    }

    for (int i = 0; i < 5; i ++) {
        for (int j = 0; j < 5; j ++) {
            printf("%2d ", board[i][j]);
        }
        printf("\n");
    }


    return 0;
}