#include "qfin/black_scholes.hpp"

#include <iomanip>
#include <iostream>

int main() {
    const double S = 100.0;
    const double K = 100.0;
    const double T = 1.0;
    const double r = 0.05;
    const double sigma = 0.2;
    const double analytical = qfin::black_scholes_call(S, K, T, r, sigma);
    const double mc = qfin::monte_carlo_call(S, K, T, r, sigma, 500000UL, 42U);
    std::cout << std::fixed << std::setprecision(6);
    std::cout << "black_scholes_call " << analytical << "\n";
    std::cout << "monte_carlo_call    " << mc << "\n";
    return 0;
}
