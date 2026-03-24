#include "qfin/black_scholes.hpp"

#include <cmath>
#include <random>

namespace qfin {

double norm_cdf(double x) {
    return 0.5 * (1.0 + std::erf(x / std::sqrt(2.0)));
}

double black_scholes_call(double spot, double strike, double time_years, double rate, double vol) {
    if (time_years <= 0.0 || vol <= 0.0 || spot <= 0.0 || strike <= 0.0) {
        return std::max(spot - strike, 0.0);
    }
    const double sqrt_t = std::sqrt(time_years);
    const double d1 =
        (std::log(spot / strike) + (rate + 0.5 * vol * vol) * time_years) / (vol * sqrt_t);
    const double d2 = d1 - vol * sqrt_t;
    return spot * norm_cdf(d1) - strike * std::exp(-rate * time_years) * norm_cdf(d2);
}

double monte_carlo_call(
    double spot,
    double strike,
    double time_years,
    double rate,
    double vol,
    unsigned long paths,
    unsigned int seed) {
    if (paths == 0UL || time_years <= 0.0 || vol <= 0.0 || spot <= 0.0 || strike <= 0.0) {
        return black_scholes_call(spot, strike, time_years, rate, vol);
    }
    std::mt19937 gen(seed);
    std::normal_distribution<double> dist(0.0, 1.0);
    double sum = 0.0;
    const double drift = (rate - 0.5 * vol * vol) * time_years;
    const double diffusion_coeff = vol * std::sqrt(time_years);
    const double df = std::exp(-rate * time_years);
    for (unsigned long i = 0; i < paths; ++i) {
        const double z = dist(gen);
        const double st = spot * std::exp(drift + diffusion_coeff * z);
        const double payoff = std::max(st - strike, 0.0);
        sum += df * payoff;
    }
    return sum / static_cast<double>(paths);
}

}
