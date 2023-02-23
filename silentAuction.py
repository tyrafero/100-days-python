from replit import clear
highestBid = 0
winner = ""

def highestBidder(bid_d):
    global highestBid, winner
    for i in bid_d:
        amount = bid_d[i]
        if amount > highestBid:
            highestBid = amount
            winner = i
    print(winner, highestBid)
        

details = {}
personLeft = "y"
bids = {}

while personLeft != "n":
    print("enter your name and your bid")
    name = input("Enter the name: ")
    key = int(input("Enter your bid: "))
    bids[name] = key
    
    details[name] = key
    print(f"Your name is {name} and your bid is {key}")
    personLeft = input("Is there anyone left to bid? y/n :")
    if personLeft == "y":
        clear()
    highestBidder(bids)

# max_bid = max(details, key=lambda k: details[k])
# print(max_bid, details[max_bid])
