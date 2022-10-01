from art import logo
import os

print(logo)
print("Welcome to the secret auction program.")
NewBid=True
bidders={}
highestbid=0
winner=""
def add_bidders(name,bid):
  bidders[name]=bid
while NewBid == True:
  name=input("What is your name? ")
  bid=int(input("How much are you willing to bid? $ "))
  add_bidders(name,bid)
  another=input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  os.system('cls')
  if another == "no":
    NewBid=False
for person in bidders:
  if bidders[person] > highestbid:
    highestbid=bidders[person]
    winner=person
print("The highest bidder is "+ winner + " at $" + str(bidders[winner]))