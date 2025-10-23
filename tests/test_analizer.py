import pytest
from logic.analyzer import *
from src.classes import Card

"""

Modo de ejecución de los tests:
    - Ejecución normal: ❯ pytest
    - Ejecución resumida (que para cada test diga PASSED o FAILED): ❯ pytest -v

Pego aqui los emoticonos de cada palo porque puede estar guay usarlos por ahi en algun momento:

Spades (Espadas): ♠
Hearts (Corazones): ♥
Diamonds (Diamantes): ♦
Clubs (Tréboles): ♣
"""

# ========== Instancias de Card() para de carta de la baraja para los tests ==========
ace_of_spades = Card("Spades", "Ace", 14)
two_of_spades = Card("Spades", "2", 2)
three_of_spades = Card("Spades", "3", 3)
four_of_spades = Card("Spades", "4", 4)
five_of_spades = Card("Spades", "5", 5)
six_of_spades = Card("Spades", "6", 6)
seven_of_spades = Card("Spades", "7", 7)
eight_of_spades = Card("Spades", "8", 8)
nine_of_spades = Card("Spades", "9", 9)
ten_of_spades = Card("Spades", "10", 10)
jack_of_spades = Card("Spades", "Jack", 11)
queen_of_spades = Card("Spades", "Queen", 12)
king_of_spades = Card("Spades", "King", 13)

ace_of_clubs = Card("Clubs", "Ace", 14)
two_of_clubs = Card("Clubs", "2", 2)
three_of_clubs = Card("Clubs", "3", 3)
four_of_clubs = Card("Clubs", "4", 4)
five_of_clubs = Card("Clubs", "5", 5)
six_of_clubs = Card("Clubs", "6", 6)
seven_of_clubs = Card("Clubs", "7", 7)
eight_of_clubs = Card("Clubs", "8", 8)
nine_of_clubs = Card("Clubs", "9", 9)
ten_of_clubs = Card("Clubs", "10", 10)
jack_of_clubs = Card("Clubs", "Jack", 11)
queen_of_clubs = Card("Clubs", "Queen", 12)
king_of_clubs = Card("Clubs", "King", 13)

ace_of_diamonds = Card("Diamonds", "Ace", 14)
two_of_diamonds = Card("Diamonds", "2", 2)
three_of_diamonds = Card("Diamonds", "3", 3)
four_of_diamonds = Card("Diamonds", "4", 4)
five_of_diamonds = Card("Diamonds", "5", 5)
six_of_diamonds = Card("Diamonds", "6", 6)
seven_of_diamonds = Card("Diamonds", "7", 7)
eight_of_diamonds = Card("Diamonds", "8", 8)
nine_of_diamonds = Card("Diamonds", "9", 9)
ten_of_diamonds = Card("Diamonds", "10", 10)
jack_of_diamonds = Card("Diamonds", "Jack", 11)
queen_of_diamonds = Card("Diamonds", "Queen", 12)
king_of_diamonds = Card("Diamonds", "King", 13)

ace_of_hearts = Card("Hearts", "Ace", 14)
two_of_hearts = Card("Hearts", "2", 2)
three_of_hearts = Card("Hearts", "3", 3)
four_of_hearts = Card("Hearts", "4", 4)
five_of_hearts = Card("Hearts", "5", 5)
six_of_hearts = Card("Hearts", "6", 6)
seven_of_hearts = Card("Hearts", "7", 7)
eight_of_hearts = Card("Hearts", "8", 8)
nine_of_hearts = Card("Hearts", "9", 9)
ten_of_hearts = Card("Hearts", "10", 10)
jack_of_hearts = Card("Hearts", "Jack", 11)
queen_of_hearts = Card("Hearts", "Queen", 12)
king_of_hearts = Card("Hearts", "King", 13)

# ========== Tests ==========

# Reminder: 
#   return 0 = You've already got the hand you wanted
#   return 6 = You can't get this hand with your actual cards

def test_isRoyalFlush():
    assert isRoyalFlush([ace_of_clubs, six_of_diamonds, eight_of_clubs, two_of_hearts, jack_of_diamonds]) == 6
    assert isRoyalFlush([ace_of_clubs, queen_of_clubs, jack_of_clubs, king_of_clubs, ten_of_clubs]) == 0