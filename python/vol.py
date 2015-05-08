import mibian
import sys
import csv
# cmdargs = str(sys.argv)

class Security:
    pass

class Option:
    pass


#BS([underlyingPrice, strikePrice, interestRate, daysToExpiration], volatility=x, callPrice=y, putPrice=z)

def getRiskFreeRate():
    return 1

# uses mibian to calculate Implied Volatility

# Option contains:
#   bool type (true = call, false = put)
#   float premium
#   float strike
#   int daysToExpiration
#   float IV (= null, to be calculated)

def calcVol(option, secPrice, paysDividends):
    if (paysDividends):
        print("TODO")
    else:
        if (option.type):
            c = mibian.BS(
            [secPrice,
            option.strike,
            getRiskFreeRate(),
            option.daysToExpiration
            ],
            callPrice=option.premium
            )
            option.IV = c.impliedVolatility


# takes a Security, sec, as its parameter
# expects sec to contain the following:
#   int price
#   Option[] optionsChain:
#   bool paysDividends
# At the moment, only calculates IV.
def calcGreeks(sec):
    for option in sec.optionsChain:
        calcVol(option, sec.price, sec.paysDividends)

def getCSVVol(row):
    # if(isinstance(row['strike'], (int, long))):
    row['last'] = float(row['last'])
    c = mibian.BS([538.22, row['strike'], getRiskFreeRate(), 7], callPrice=row['last'])
    # print(row['strike'], c.impliedVolatility, row['imp vol'])


# testing calcGreeks
goog = Security()
goog.price = 538.22
goog.paysDividends = False
option540 = Option()
option540.type = True
option540.premium = 3.90
option540.strike = 540.0
option540.daysToExpiration = 7.0
option540.IV = None
goog.optionsChain = [option540]
calcGreeks(goog)
print(goog.optionsChain[0].IV)


# exported an options chain from options house to csv,
# using for testing calculated IV vs optionshouse IV
# with open('python/options.csv', 'rb') as csvfile:
#     fieldnames = ['strike', 'ask', 'last', 'markchg', 'bid size', 'ask size', 'delta', 'imp vol', 'imp vol chg', 'open interest', 'volume', 'bid']
#     reader = csv.DictReader(csvfile, fieldnames=fieldnames)
#     index = 0;
#     for row in reader:
#         if (index > 2 ):
#             getCSVVol(row)
#         index += 1
