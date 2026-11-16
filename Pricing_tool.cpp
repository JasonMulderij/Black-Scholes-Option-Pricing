#include <iostream>
#include <cmath>

double normalCDF(double x)
{
    return 0.5 * std::erfc(-x / std::sqrt(2.0));
}

double call_price(double S, double K, double r, double T, double sigma)
{
    double d1 = (std::log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * std::sqrt(T));
    double d2 = d1 - sigma * std::sqrt(T);
    return S * normalCDF(d1) - K * std::exp(-r * T) * normalCDF(d2);
}

double put_price(double S, double K, double r, double T, double sigma)
{
    double d1 = (std::log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * std::sqrt(T));
    double d2 = d1 - sigma * std::sqrt(T);
    return K * std::exp(-r * T) * normalCDF(-d2) - S * normalCDF(-d1);
}

int main()
{
    double S     = 100.0;
    double K     = 100.0;
    double r     = 0.05;
    double T     = 1.0;
    double sigma = 0.2;

    std::cout << "Call Price: " << call_price(S, K, r, T, sigma) << std::endl;
    std::cout << "Put Price: " << put_price(S, K, r, T, sigma) << std::endl;

    return 0;
}