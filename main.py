# Blackjack
import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Create a deck of cards
deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]

# Shuffle deck
random.shuffle(deck)

player_score = 0
cpu_score = 0
game_over = False


def draw_card():
    if deck:
        return deck.pop()
    else:
        print("The deck is empty. Cannot draw a card.")


def calc_score(card, current_score):
    rank = card['rank']

    if rank in ['J', 'K', 'Q']:
        return current_score + 10

    elif rank == 'A':
        return current_score + 11 if current_score + 11 <= 21 else current_score + 1
    else:
        return current_score + int(rank)


def player_draw_a_card():
    global player_score
    card = draw_card()
    player_score = calc_score(card, player_score)
    print(f"Player drew: {card['rank']} of {card['suit']}")
    if player_score > 21:
        print("You Busted!")


def cpu_draw_a_card(hidden=False):
    global cpu_score
    card = draw_card()
    cpu_score = calc_score(card, cpu_score)

    if not hidden:
        print(f"CPU drew: {card['rank']} of {card['suit']}")
    else:
        print("CPU drew a hidden card.")

    if cpu_score > 21:
        print("CPU Busted!")


print("Welcome to Blackjack Simulator.")
player_draw_a_card()
player_draw_a_card()

cpu_draw_a_card()
cpu_draw_a_card(hidden=True)

while not game_over:
    pl_input = input("Do you want to 'Hit' or 'Stand'?: ")

    if pl_input == "Hit":
        player_draw_a_card()
        if player_score > 21:
            game_over = True
    else:
        game_over = True

while True:
    if cpu_score < 17 and player_score < 21:
        cpu_draw_a_card()
    else:
        break

print(f"Final scores:\n"
      f"Player: {player_score}\n"
      f"CPU: {cpu_score}")

if cpu_score < player_score <= 21 or cpu_score > 21 >= player_score:
    print("You Win!")

elif cpu_score == player_score:
    print("It's a Draw!")

else:
    print("You Lose.")
