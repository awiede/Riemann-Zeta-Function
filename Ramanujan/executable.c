#include <stdio.h>
#include <math.h>

double ramanujan(int k)
{
    //on compile, must include flag -lm to include math library
    double sigma;
    sigma=0.0;
    int i; 
    double p1, p2;
    for (i=1; i<(k+1); i++)
    {
        p1 = pow(0.5,i);
        p2 = pow(i,-3);
        sigma += (p1 * p2);
    }
    double diff1 = (4.0/21.0) * pow(log(2),3);
    double diff2 = (2.0/21.0) * pow(M_PI,2) * log(2);
    sigma = ((8.0/7.0) * sigma) - diff1 + diff2;
    return sigma;
}

main()
{
    double result;
    result = ramanujan(10000); //input should not be hard coded
    //workunit should divide ranges of k
    //read in from input.txt
    //write to output.txt
    //sythesize should put results together
    printf("%f\n", result);
}