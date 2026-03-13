import numpy as np

def monte_carlo_pricing(S, K, T, r, sigma, iterations=100000, option_type="call", barrier=None):
    """Vectorized Monte Carlo option pricing."""
    
    # For European options, we only need the price at maturity T
    z = np.random.standard_normal(iterations)
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * z)
    
    if barrier:
        payoffs = np.where(ST > barrier, 0, np.maximum(ST - K, 0))
    else:
        if option_type == "call":
            payoffs = np.maximum(ST - K, 0)
        else:
            payoffs = np.maximum(K - ST, 0)
            
    return np.exp(-r * T) * np.mean(payoffs)