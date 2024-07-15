import art

from random import choice


def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card


def set_final_status(u_score, c_score):
    if c_score == 0:
        return "You lose, Computer got a blackjack."
    elif u_score == 0:
        return "You win, You got a blackjack."
    elif u_score > 21:
        return "You went over, You Lose."
    elif c_score > 21:
        return "Opponent went over, You win."
    elif u_score == c_score:
        return "Draw"
    elif u_score > c_score:
        return "Win"
    else:
        return "Lose"


def print_hands(cards1, cards2):
    """print the players hands"""
    print(f"    User cards: {cards1}, current score: {calculate_score(cards1)}")
    print(f"    Computer first card: {cards2[0]}")


def draw_computer_cards(cards):
    """deal all the cards for the computer until it exceeds the score 16"""

    return cards


def calculate_score(cards):
    """returns cards score"""
    score = sum(cards)
    if len(cards) == 2 and score == 21:
        """this means the user go a blackjack"""
        return 0
    if 11 in cards and score > 21:
        for card in cards:
            if card == 11:
                cards.remove(card)
                cards.append(1)
        calculate_score(cards)
    return score


def game():
    print(art.logo)

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(draw_card())
        computer_cards.append(draw_card())

    # user_cards = [11, 10]
    computer_cards = [11, 10]
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print_hands(user_cards, computer_cards)
    if user_score == 0 or computer_score == 0:
        pass
    else:
        while input("Do you want another card?: ") == 'y':
            user_cards.append(draw_card())
            user_score = calculate_score(user_cards)
            print_hands(user_cards, computer_cards)
            if user_score > 21:
                break

        while computer_score < 17:
            computer_cards.append(draw_card())
            computer_score = calculate_score(computer_cards)

    win_lose_status = set_final_status(user_score, computer_score)
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(win_lose_status)


while input("Do you want to play?: ") == 'y':
    game()
    print()
