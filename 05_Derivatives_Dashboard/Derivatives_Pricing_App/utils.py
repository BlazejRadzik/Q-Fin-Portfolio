import numpy as np
from scipy.stats import norm
from analytical import black_scholes_european

def calculate_vega(S, K, T, r, sigma):
    """Calculates the Vega Greek of an option."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    return S * np.sqrt(T) * norm.pdf(d1)

def implied_volatility(target_price, S, K, T, r, option_type="call"):
    """Calculates implied volatility using the Newton-Raphson method."""
    sigma = 0.2  
    
    for i in range(100):
        price = black_scholes_european(S, K, T, r, sigma, option_type)
        vega = calculate_vega(S, K, T, r, sigma)
        
        if vega == 0.0:
            break  
            
        diff = target_price - price
        
        if abs(diff) < 1e-6:
            return sigma
            
        sigma = sigma + diff / vega  
        
    return sigma
