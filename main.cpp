#include <iostream>

int main() 
{
    constexpr int size = 5;
    int arr[size];
    arr[1] = 69;
    arr[3] = 420;

    for (int i = 0; i < 5; i++)
    {
        std::cout << i << std::endl;
    }

    return 0;
}