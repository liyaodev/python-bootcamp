#include <stdio.h>
#include <stdlib.h>

// @created on 2022/03/26
// @author Yao Li

int sum(int x)
{
    int i, res = 0;
    for (i = 0; i <= x; i ++)
    {
        res += i;
    }
    if (x > 100)
        exit(-1);

    return res;
};

int add(float a, float b)
{
    return a + b;
}

// gcc -c -fPIC -o lib/sum.o sum.c
// gcc -shared -o lib/sum.so lib/sum.o

