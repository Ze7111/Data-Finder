// make a program that takes the area of a triangle and prints the perimeter of the triangle

#include <stdio.h>

int main(void)
{
    float area, perimeter;
    float base, height;
    
    printf("Enter the base and height of the triangle: ");
    scanf("%f %f", &base, &height);
    
    area = (base * height) / 2;
    perimeter = base + height + (base * height);
    
    printf("The area of the triangle is %f\n", area);
    printf("The perimeter of the triangle is %f\n", perimeter);
    
    return 0;
}