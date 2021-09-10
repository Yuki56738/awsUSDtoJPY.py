#!/usr/bin/env python3

from currency_converter import CurrencyConverter
import sys

print("Welcome to Yuki's AWS USD to JPY converter.")
print("Type numbers[USD]. It'll be converted to JPY/24h.")
print("\nCTRL + C to exit.")
c = CurrencyConverter()

#arg1 = sys.argv[1]


def outJpy(arg1):
  arg1Jpy = c.convert(arg1, "USD", "JPY")
  
  #print(arg1Jpy)
  
  print(arg1Jpy * 24 * 31)

try:
  while True:
    arg1 = input(">>")
    outJpy(arg1)
except KeyboardInterrupt:
  print("\nThank you for using this tool!")
  sys.exit(0)
