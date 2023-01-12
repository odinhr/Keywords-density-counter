#!/usr/bin/env python
# made by @odinhr

from tools import *

text = input('Introduce the full text: ')
keywords = input('Introduce the keywords you want to find in text: ')

density,words=densityCalculator(text,keywords)

print('Total words = ',words)
print('Keywords density = ',density ,'%')

