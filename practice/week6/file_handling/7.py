import os

source=input("Enter source: ")
destination=input("Enter destination: ")


def S():
  with open (source) as srs:
    return srs.read()


with open (destination, 'w') as dst:
  dst.write(S())
