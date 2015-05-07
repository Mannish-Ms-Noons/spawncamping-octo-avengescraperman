import mibian
import sys
cmdargs = str(sys.argv)

#BS([underlyingPrice, strikePrice, interestRate, daysToExpiration], volatility=x, callPrice=y, putPrice=z)

c = mibian.BS([78.1, 78, 1, 7], callPrice=1.30)
print(c.impliedVolatility)
