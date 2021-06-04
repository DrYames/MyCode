#main method for Week 12 CIS3145 James Porter
from BusinessTier import Card, Deck, Hand

def main():
    deck = Deck()
    print("DECK")
    print(deck)
    deck.shuffle()
    print("Shuffled deck count: ",deck.count())
    print("\nHAND")
    hand = Hand()
    for i in range(5):
        i = deck.dealCard()
        print(str(i))
        hand.addCard(i)

    print("\nHand Points: ", hand.totalPoints())
    print("Hand count: ", hand.count())
    print("Deck count: ", deck.count())
    
if __name__ == "__main__":
    main()
