


name = input("what is your name?\n")
price = int(input("what is your bid? $ \n"))
bids = {}

bids[name] = price
should_continue = input("are there any other bidder ?type 'yes' or 'no'\n")


def find_highest_bidder(bids):
    winner = ""
    highest_bid = 0
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with a bid of {highest_bid} $")


continue_bidding = True
while continue_bidding:
    name = input("what is your name?\n")
    price = int(input("what is your bid? $ \n"))
    bids[name] = price
    should_continue = input("are there any other bidder ?type 'yes' or 'no'\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        continue_bidding = True
        print('\n*100 ')
        