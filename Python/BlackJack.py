import random
suits = ('Spades','Diamonds','Clubs','Hearts')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing = True

class Card():
  def __init__(self,suit,rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return self.rank+ " of "+self.suit

class Deck():
  def __init__(self):
    self.deck = []
    for suit in suits:
      for rank in ranks:
        self.deck.append(Card(suit,rank))

  def __str__(self):
    deck_comp = ''
    for card in self.deck:
      deck_comp += '\n'+card.__str__()
    return "The deck has: "+deck_comp

  def shuffle(self):
    random.shuffle(self.deck)

  def deal(self):
    return self.deck.pop()

class Hand():
  def __init__(self):
    self.cards = []
    self.value = 0
    self.aces = 0

  def add_card(self,card):
    self.cards.append(card)
    self.value += values[card.rank]

    if card.rank == 'Ace':
      self.aces += 1

  def adjust_for_ace(self):
    while self.value > 21 and self.aces:
      self.value -= 10
      self.aces -= 1

class Chips():
  def __init__(self,total=100):
    self.total = total
    self.bet = 0

  def win_bet(self):
    self.total += self.bet

  def lose_bet(self):
    self.total -= self.bet

def take_bet(chips):
  while True:
    try:
      chips.bet = int(input("Place your bet: "))
    except:
      print("Please provide an int")
    else:
      if chips.bet > chips.total:
        print('Not enough chips! You have: {}'.format(chips.total))
      else:
        break

def hit(deck,hand):
  hand.add_card(deck.deal())
  hand.adjust_for_ace()

def hit_or_stand(deck,hand):
  global playing

  while True:
    x = input('Hit of Stand (h or s)')
    if x[0].lower() == 'h':
      hit(deck,hand)

    elif x[0].lower() == 's':
      print("Player Stands, Dealers Turn")
      playing = False

    else:
      print("Sorry, I did not understand. Please enter h or s")
      continue

    break

def player_busts(player,dealer,chips):
  print('Player Busts!')
  chips.lose_bet()

def player_wins(player,dealer,chips):
  print('Player Wins!')
  chips.win_bet()

def dealer_busts(player,dealer,chips):
  print('Dealer Busts, Player Wins!')
  chips.win_bet()

def dealer_wins(player,dealer,chips):
  print('Dealer Wins! :(')
  chips.lose_bet()

def push(player,dealer):
  print('PUSH!')

def show_some(player,dealer):
  print('DEALERS HAND: ')
  print('one card hidden!')
  print(dealer.cards[1])
  print('\nPLAYERS HAND: ')
  for card in player.cards:
    print(card)

def show_all(player,dealer):
  print('\nDEALERS HAND: ')
  for card in dealer.cards:
    print(card)
  print('\nPLAYERS HAND: ')
  for card in player.cards:
    print(card)

def main():
  global playing
  while True:
    print("Welcome to BlackJack!")
    deck = Deck()
    deck.shuffle()

    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())

    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

    player_chips = Chips()
    
    take_bet(player_chips)

    show_some(player,dealer)

    while playing:
      hit_or_stand(deck,player)
      show_some(player,dealer)
      if player.value > 21:
        player_busts(player,dealer,player_chips)
        break
    if player.value <= 21:
      while dealer.value < 17:
        hit(deck,dealer)

      show_all(player,dealer)

      if dealer.value > 21:
        dealer_busts(player,dealer,player_chips)
      elif dealer.value > player.value:
        dealer_wins(player,dealer,player_chips)
      elif dealer.value < player.value:
        player_wins(player,dealer,player_chips)
      else:
        push(player,dealer)

    print('\nPlayer total chips : {}'.format(player_chips.total))
    new_game = input("Another hand? y/n: ")
    if new_game[0].lower() == 'y':
      playing = True
      continue
    else:
      print('Thanks for playing!')
      break

if __name__ == "__main__":
  main()