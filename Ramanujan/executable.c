#include <stdio.h>
#include <math.h>

double ramanujan(int k)
{
    //does not compile. Gives error on pow
    /*
    /tmp/cc2veuoH.o: In function `ramanujan':
    executable.c:(.text+0x36): undefined reference to `pow'
    executable.c:(.text+0x61): undefined reference to `pow'
    collect2: ld returned 1 exit status
    */

    double sigma;
    sigma=0.0;
    int i, p1, p2;
    for (i=1; i<(k+1); i++)
    {
        p1 = pow(0.5,i);
        p2 = pow(i,3);
        sigma+=p1 * (1.0/p2);
    }
    p1 = pow(log(2),3);
    p2 = pow(M_PI,2);
    double diff1 = (4.0/21) * p1;
    double diff2 = (2.0/21) * p2 * log(2);
    sigma= (8.0/7.0) * sigma - diff1 + diff2;
    return sigma;
}

main() 
{
    float result;
    result = ramanujan(100);
    printf("%f\n", result);
}