import random

class PlayerScore:

	def __init__(self,score):
		self.score = score

	def win(self,win_chips):
		self.score += win_chips

	def lose(self,lose_chips):
		self.score -= lose_chips


class Cards:

	def __init__(self,playing_cards):
		self.playing_cards = playing_cards

	def shuffle(self):
		random.shuffle(self.playing_cards)
		return self.playing_cards


def value(card):
	if card[0] in ['jack','queen','king','ace']:
		return 10
	else:
		return card[0]


deck_of_cards = []
for i in ['spades','clubs','hearts','diamonds']:
	for j in [2,3,4,5,6,7,8,9,10,'jack','queen','king','ace']:
		deck_of_cards.append([j,i])


my_cards = Cards(deck_of_cards)
player1 = PlayerScore(1000)

my_cards.shuffle()

print(f'SCORE  {player1.score}')

bet = 0
while not bet in ['20','40','50','100','1000']:
	bet = int(input('Place your bet 20/40/50/100/500/1000\n'))
	if not bet in ['20','40','50','100','1000']:
		print('Enter a valid bet')

print(f'COMPUTER have  {XXXX}  {my_cards.playing_cards[1]}  ')