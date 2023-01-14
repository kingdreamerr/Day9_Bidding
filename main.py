import os
from art import logo
print(logo)

oction = []

def add_bid(name, price):
    oction.append({
        name:price
    })

def winner(array):
  highest = 0
  winner = ""
  for dic in array:
    for person in dic:
        if dic[person] > highest:
            highest = dic[person]
            winner = person
  print(f"The winner is {winner} with a bid of ${highest}")

more_bids = True
