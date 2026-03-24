#pragma once

namespace qfin {

double norm_cdf(double x);

double black_scholes_call(double spot, double strike, double time_years, double rate, double vol);

double monte_carlo_call(
    double spot,
    double strike,
    double time_years,
    double rate,
    double vol,
    unsigned long paths,
    unsigned int seed);

}
