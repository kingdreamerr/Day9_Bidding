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


while more_bids:
    name = input("Enter your name: ")
    price = int(input("what is your bid: "))
    add_bid(name, price)

    more = input("Are there any more bids? yes or no: ").lower()
    if more == "yes":
        os.system('clear')
    else:
      winner(oction)
      more_bids = False
