import art

from random import choice


def draw_card(player_cards):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    if card == 11 and calculate_score(player_cards) + card > 21:
        card = 1
    return card


def calculate_score(cards):
    score = 0
    for card in cards:
        score += card
    if 11 in cards and score > 21:
        cards[cards.index(11)] = 1
        score = calculate_score(cards)
    return score


def game():
    print(art.logo)

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(draw_card(user_cards))
        computer_cards.append(draw_card(computer_cards))

    # user_cards = [11, 9]
    # computer_cards = [11, 9]
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"    User cards: {user_cards}, current score: {user_score}")
    print(f"    Computer first card: {computer_cards[0]}")
    if user_score == 21 or computer_score == 21:
        while computer_score < 17:
            computer_cards.append(draw_card(computer_cards))
            computer_score = calculate_score(computer_cards)

        if computer_score == 21:
            win_lose_status = "You lose, Computer got a blackjack."
        else:
            win_lose_status = "You win, You got a blackjack."
    else:
        while input("Do you want another card?: ") == 'y':
            user_cards.append(draw_card(user_cards))
            user_score = calculate_score(user_cards)
            print(f"    User cards: {user_cards}, current score: {user_score}")
            print(f"    Computer first card: {computer_cards[0]}")
            if user_score > 21:
                break

        computer_score = calculate_score(computer_cards)
        while computer_score < 17:
            computer_cards.append(draw_card(computer_cards))
            computer_score = calculate_score(computer_cards)

        if user_score > 21:
            win_lose_status = "You went over, You Lose."
        elif computer_score > 21:
            win_lose_status = "Opponent went over, You win."
        elif user_score == computer_score:
            win_lose_status = "Draw"
        elif user_score > computer_score:
            win_lose_status = "Win"
        else:
            win_lose_status = "Lose"
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(win_lose_status)


while input("Do you want to play?: ") == 'y':
    game()
    print()
