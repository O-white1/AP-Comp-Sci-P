#include <stdio.h>

int main() {
    int n = 0;
    while (n <= 36) {
        if (n%2 == 0)
            printf("%d\n", n);
        n++;
    }
}