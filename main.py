import art

from random import choice


def game():
    print(art.logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0

    for _ in range(2):
        user_cards.append(choice(cards))
        computer_cards.append(choice(cards))

    for card in user_cards:
        user_score += card

    print(f"User cards: {user_cards}, current score: {user_score}")
    print(f"Computer first card: {computer_cards[0]}")

    while input("Do you want another card?: ") == 'y':
        user_cards.append(choice(cards))
        for card in user_cards:
            user_score += card
        print(f"User cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")


while input("Do you want to play?: ") == 'y':
    game()
    print()
# todo: اظهر ورقتين المستخدم واظهر اول ورقة للكمبيوتر
# todo: احسب مجموع المستخدم
