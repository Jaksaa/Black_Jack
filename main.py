import random
from art import logo
from replit import clear

def blackjack():
	print(logo)
	start = input("Welcome to the Black Jack game do you want to start 'yes' or 'no': ")
	clear()
	if start == "yes":
		dealer = []
		player = []
		for i in range(2):
			player.append(draw_card())
			dealer.append(draw_card())
	player_score = score(player)
	computer_score = score(dealer)
	if computer_score == 0:
		print("Computer got blakcjack. You lose.")
		blackjack()
	elif player_score == 0:
		print(f"You got blakcjack. With hand {player}")
		blackjack()
	while computer_score < 17:
			dealer.append(draw_card())
			computer_score = score(dealer)
	print(f"Your cards are {player} and your current score is {player_score}\nComputer's first card is : {dealer[0]}")
	draw_again = input("Do you want to draw another card?, type 'yes' or 'no': ") 
	if draw_again == "yes":
		player.append(draw_card())
		player_score = score(player)
		print(f"Your cards are {player} and your final score is {player_score}\nComputer's cards are: {dealer}, final score {computer_score}")
		game_end(player_score, computer_score, player, dealer)
	else:
		game_end(player_score, computer_score, player, dealer)

def draw_card():
	cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	card = random.choice(cards)
	return card

def score(cards):
	if sum(cards) == 21:
		return 0
	return sum(cards)

def game_end(player_score, computer_score, player, dealer):
	if player_score > 21 and 11 in player: 
		player[player.index(11)] = 1
		player_score = score(player)
		if player_score > 21:
			print(f"Your score is {player_score} it's a bust. You lose.") 
	if computer_score > 21 and 11 in dealer:
		dealer[dealer.index(11)] = 1
		computer_score = score(dealer)
		if computer_score > 21:
			print(f"Computer score is {computer_score} it's a bust. You won.") 
	if player_score > computer_score and player_score > 21:
		print(f"Your score is {player_score} and Computer's score is {computer_score}. You lose.")
	elif player_score > computer_score:
		print(f"Your score is {player_score} and Computer's score is {computer_score}. You won.")
	if player_score < computer_score and computer_score > 21:
		print(f"Your score is {player_score} and Computer's score is {computer_score}. You won.")
	elif player_score < computer_score:
		print(f"Your score is {player_score} and Computer's score is {computer_score}. You lose.")
	if player_score == computer_score:
		print(f"Your score is {player_score} and Computer's score is {computer_score}. It's a draw.")
	blackjack()

blackjack()
