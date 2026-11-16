import numpy as np
from scipy.stats import norm

class BlackScholes:
    def __init__(self, spot, strike, rate, maturity, volatility):
        self.spot       = spot
        self.strike     = strike 
        self.rate       = rate
        self.maturity   = maturity
        self.volatility = volatility

    def d1_d2(self):
        d1 = ( np.log(self.spot / self.strike) + (self.rate + 0.5 * self.volatility ** 2) * self.maturity ) / (self.volatility * np.sqrt( self.maturity))
        d2 = d1 - self.volatility * np.sqrt(self.maturity)
        return d1, d2
    def call_price(self):
        d1, d2 = self.d1_d2()
        return (self.spot * norm.cdf(d1) - self.strike * np.exp(-self.rate * self.maturity) * norm.cdf(d2))

    def put_price(self):
        d1, d2 = self.d1_d2()
        return ( self.strike * np.exp(-self.rate * self.maturity) * norm.cdf(-d2) - self.spot * norm.cdf(-d1))
        