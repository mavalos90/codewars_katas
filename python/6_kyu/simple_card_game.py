# Simple card game
# 6 kyu

'''
Steve and Josh are bored and want to play something. They don't want to think too much, so they come up with a really simple game. Write a function called winner and figure out who is going to win.

They are dealt the same number of cards. They both flip the card on the top of their deck. Whoever has a card with higher value wins the round and gets one point (if the cards are of the same value, neither of them gets a point). After this, the two cards are discarded and they flip another card from the top of their deck. They do this until they have no cards left.

deckSteve and deckJosh are arrays representing their decks. They are filled with cards, represented by a single character. The card rank is as follows (from lowest to highest):

'2','3','4','5','6','7','8','9','T','J','Q','K','A'
Every card may appear in the deck more than once. Figure out who is going to win and return who wins and with what score:

"Steve wins x to y" if Steve wins; where x is Steve's score, y is Josh's score;
"Josh wins x to y" if Josh wins; where x is Josh's score, y is Steve's score;
"Tie" if the score is tied at the end of the game.
Example
Steve is dealt: ['A','7','8']
Josh is dealt: ['K','5','9']
In the first round, ace beats king and Steve gets one point.
In the second round, 7 beats 5 and Steve gets his second point.
In the third round, 9 beats 8 and Josh gets one point.
So you should return: "Steve wins 2 to 1"
'''

def winner(deck_steve, deck_josh):
    # Modify the upper cards
    dic_cards = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    deck_steve = [dic_cards.get(card,card)  for card in deck_steve]
    deck_josh = [dic_cards.get(card,card)  for card in deck_josh]
    
    # Compute who wins
    s_wins = 0
    j_wins = 0
    for i in range(len(deck_steve)):
        if int(deck_steve[i]) > int(deck_josh[i]):
            s_wins += 1
        elif int(deck_steve[i]) < int(deck_josh[i]):
            j_wins += 1
            
    # Return the possible outcomes        
    if s_wins > j_wins: return 'Steve wins ' + str(s_wins) + ' to ' + str(j_wins)
    elif j_wins > s_wins: return 'Josh wins ' + str(j_wins) + ' to ' + str(s_wins)
    else: return "Tie"