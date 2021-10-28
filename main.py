from kayaEquation import *

pop_de = 82.4
gdp_de = 44
enInt_de = 5
carbInt_de = 0.05

print('Emissions in Germany: ' + str(kayaEquation(pop_de, gdp_de, enInt_de, carbInt_de)))

print("Using __doc__:")
print(kayaEquation.__doc__)