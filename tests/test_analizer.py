import pytest
from logic.analyzer import *
from src.classes import Card


# Modo de ejecución de los tests recomendado: ❯ pytest -v     #

# ====================== Instancias de Card() para de carta de la baraja para los tests ======================
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

# ====================== Tests ======================
# Reminder: 
#   return 0 = You've already got the hand you wanted
#   return 6 = You can't get this hand with your actual cards

def test_isRoyalFlush_cases():
    # === CASOS PERFECTOS (0) ===
    assert isRoyalFlush([ace_of_clubs, queen_of_clubs, jack_of_clubs, king_of_clubs, ten_of_clubs]) == 0
    assert isRoyalFlush([nine_of_diamonds, queen_of_spades, three_of_hearts, ace_of_spades, ten_of_spades, king_of_spades, jack_of_spades]) == 0
    assert isRoyalFlush([ten_of_spades, jack_of_spades, queen_of_spades, king_of_spades, ace_of_spades]) == 0
    assert isRoyalFlush([two_of_clubs, three_of_diamonds, ten_of_spades, jack_of_spades, queen_of_spades, king_of_spades, ace_of_spades]) == 0

    # === CASOS FALTAN 1 CARTA (1) ===
    assert isRoyalFlush([ace_of_clubs, queen_of_clubs, jack_of_clubs, king_of_clubs, ten_of_diamonds, two_of_clubs]) == 1
    assert isRoyalFlush([ten_of_clubs, jack_of_clubs, queen_of_clubs, king_of_clubs]) == 1
    assert isRoyalFlush([ten_of_hearts, jack_of_hearts, king_of_hearts, ace_of_hearts, two_of_diamonds]) == 1

    # === CASOS FALTAN 2 CARTAS (2) ===
    assert isRoyalFlush([ten_of_diamonds, jack_of_diamonds, queen_of_diamonds]) == 2
    assert isRoyalFlush([ten_of_clubs, jack_of_clubs, queen_of_clubs]) == 2

    # === CASOS FALTAN 3 CARTAS (3) ===
    assert isRoyalFlush([ten_of_hearts, jack_of_hearts]) == 3
    assert isRoyalFlush([queen_of_spades, ace_of_spades]) == 3

    # === CASOS FALTAN 4 CARTAS (4) ===
    assert isRoyalFlush([ace_of_spades, eight_of_diamonds, seven_of_hearts]) == 4
    assert isRoyalFlush([king_of_diamonds]) == 4

    # === CASOS FALTAN 5 CARTAS (5) ===
    assert isRoyalFlush([two_of_spades, three_of_spades]) == 5
    assert isRoyalFlush([ nine_of_clubs]) == 5

    # === CASOS IMPOSIBLES (6) ===
    assert isRoyalFlush([ace_of_clubs, six_of_diamonds, eight_of_clubs, two_of_hearts, jack_of_diamonds]) == 6
    assert isRoyalFlush([ace_of_clubs, king_of_diamonds, queen_of_hearts, jack_of_spades, ten_of_hearts]) == 6
    assert isRoyalFlush([ace_of_clubs, king_of_diamonds, three_of_hearts, two_of_spades, nine_of_spades, four_of_diamonds, seven_of_hearts]) == 6
    assert isRoyalFlush([two_of_spades, three_of_spades, four_of_spades, five_of_spades, six_of_spades, seven_of_spades, eight_of_spades]) == 6

    # === CASOS BORDE ===
    assert isRoyalFlush([ten_of_clubs, ace_of_clubs]) == 3
    assert isRoyalFlush([ten_of_spades, jack_of_spades, queen_of_hearts, king_of_hearts, ace_of_diamonds, two_of_clubs, three_of_spades]) == 6



def test_isStraightFlush_cases():
    # === CASOS PERFECTOS (0) ===
    assert isStraightFlush([nine_of_spades, ten_of_spades, jack_of_spades, queen_of_spades, king_of_spades]) == 0
    assert isStraightFlush([three_of_hearts, four_of_hearts, five_of_hearts, six_of_hearts, seven_of_hearts]) == 0
    assert isStraightFlush([ace_of_clubs, queen_of_clubs, queen_of_hearts, jack_of_clubs, king_of_clubs, ten_of_clubs]) == 0
    assert isStraightFlush([ten_of_diamonds, jack_of_diamonds, queen_of_diamonds, king_of_diamonds, ace_of_diamonds]) == 0
    assert isStraightFlush([ace_of_spades, two_of_spades, three_of_spades, four_of_spades, five_of_spades]) == 0

    # === FALTA 1 CARTA (1) ===
    assert isStraightFlush([two_of_hearts, ten_of_hearts, jack_of_hearts, queen_of_hearts, king_of_hearts, ace_of_clubs]) == 1
    assert isStraightFlush([nine_of_spades, ten_of_spades, jack_of_spades, king_of_spades]) == 1
    assert isStraightFlush([jack_of_clubs, queen_of_clubs, king_of_clubs, ace_of_clubs, two_of_hearts]) == 1

    # === FALTAN 2 CARTAS (2) ===
    assert isStraightFlush([ten_of_hearts, jack_of_hearts, queen_of_hearts, three_of_spades, seven_of_clubs]) == 2
    assert isStraightFlush([queen_of_diamonds, king_of_diamonds, ace_of_diamonds, four_of_clubs]) == 2

    # === FALTAN 3 CARTAS (3) ===
    assert isStraightFlush([jack_of_clubs, nine_of_clubs, two_of_hearts, five_of_diamonds]) == 3
    assert isStraightFlush([jack_of_spades, ace_of_spades, three_of_hearts]) == 3

    # === FALTAN 4 CARTAS (4) ===
    assert isStraightFlush([king_of_diamonds, nine_of_hearts, two_of_clubs]) == 4
    assert isStraightFlush([five_of_hearts, seven_of_spades, nine_of_clubs]) == 4

    # === IMPOSIBLE (6) ===
    assert isStraightFlush([ten_of_clubs, jack_of_hearts, queen_of_diamonds, king_of_spades, ace_of_hearts, two_of_spades, three_of_clubs]) == 6
    assert isStraightFlush([ten_of_hearts, jack_of_clubs, queen_of_spades, king_of_diamonds, ace_of_hearts]) == 6
    assert isStraightFlush([two_of_spades, four_of_spades, six_of_spades, eight_of_spades, ten_of_spades, queen_of_spades, ace_of_spades]) == 6

    # === CASOS BORDE / INTERESANTES ===
    assert isStraightFlush([jack_of_diamonds, jack_of_spades, ten_of_diamonds, nine_of_diamonds]) == 2
    assert isStraightFlush([king_of_clubs, ten_of_clubs, three_of_hearts, five_of_spades]) == 3



def test_isFourofaKind_cases():
    # === CASOS PERFECTOS (0) ===
    assert isFourofaKind([seven_of_clubs, seven_of_diamonds, seven_of_hearts, seven_of_spades, ace_of_diamonds]) == 0
    assert isFourofaKind([king_of_clubs, king_of_diamonds, king_of_hearts, king_of_spades, two_of_spades, three_of_diamonds]) == 0
    assert isFourofaKind([ace_of_clubs, ace_of_diamonds, ace_of_hearts, ace_of_spades]) == 0

    # === FALTA 1 CARTA (1) ===
    assert isFourofaKind([nine_of_clubs, nine_of_diamonds, nine_of_hearts, jack_of_spades]) == 1
    assert isFourofaKind([two_of_clubs, two_of_diamonds, two_of_spades, five_of_hearts, six_of_diamonds]) == 1

    # === FALTAN 2 CARTAS (2) ===
    assert isFourofaKind([six_of_diamonds, three_of_hearts, three_of_clubs, four_of_clubs]) == 2
    assert isFourofaKind([queen_of_hearts, queen_of_clubs, ten_of_spades, two_of_diamonds]) == 2
    assert isFourofaKind([jack_of_spades, jack_of_diamonds, five_of_clubs, eight_of_hearts, nine_of_diamonds]) == 2

    # === FALTAN 3 CARTAS (3) ===
    assert isFourofaKind([four_of_clubs, nine_of_spades]) == 3
    assert isFourofaKind([king_of_diamonds, five_of_diamonds, queen_of_hearts]) == 3

    # === IMPOSIBLE (6) ===
    assert isFourofaKind([ace_of_clubs, ace_of_diamonds, king_of_hearts, king_of_spades, queen_of_clubs, jack_of_diamonds]) == 6
    assert isFourofaKind([two_of_spades, three_of_spades, four_of_spades, five_of_spades, six_of_spades, seven_of_spades, eight_of_spades]) == 6
    assert isFourofaKind([ten_of_hearts, jack_of_hearts, queen_of_hearts, king_of_hearts, ace_of_hearts, two_of_diamonds, three_of_clubs]) == 6

    # === OTROS ===
    assert isFourofaKind([three_of_clubs, three_of_hearts]) == 2
    assert isFourofaKind([eight_of_spades, eight_of_clubs, eight_of_hearts]) == 1
    assert isFourofaKind([four_of_clubs, five_of_clubs, six_of_clubs, seven_of_clubs, eight_of_clubs, nine_of_clubs, ten_of_clubs]) == 6


def test_isFullHouse_cases():
    # caso/s válido/s
    assert isFullHouse([ten_of_hearts, king_of_spades, three_of_spades, king_of_diamonds, eight_of_diamonds, ten_of_clubs, king_of_hearts]) == 0
    assert isFullHouse([ace_of_clubs, ace_of_diamonds, ace_of_hearts, king_of_spades, king_of_diamonds]) == 0
    assert isFullHouse([four_of_hearts, four_of_diamonds, four_of_clubs, nine_of_spades, nine_of_diamonds]) == 0

    # caso/s falta 1 carta
    assert isFullHouse([jack_of_hearts, jack_of_diamonds, jack_of_clubs, seven_of_spades]) == 1
    assert isFullHouse([six_of_hearts, six_of_diamonds, three_of_clubs, three_of_spades, two_of_hearts, five_of_diamonds]) == 1
    assert isFullHouse([queen_of_hearts, queen_of_diamonds, queen_of_clubs, ten_of_spades, two_of_hearts]) == 1

    # caso/s falta 2 cartas
    assert isFullHouse([nine_of_hearts, nine_of_diamonds, four_of_clubs]) == 2
    assert isFullHouse([five_of_hearts, five_of_diamonds, two_of_spades, three_of_clubs]) == 2
    assert isFullHouse([king_of_hearts, king_of_diamonds, six_of_spades]) == 2

    # caso/s falta 3 cartas
    assert isFullHouse([eight_of_hearts, eight_of_diamonds]) == 3
    assert isFullHouse([three_of_clubs, three_of_spades]) == 3
    assert isFullHouse([ace_of_hearts, three_of_clubs]) == 3

    # caso/s imposible
    assert isFullHouse([two_of_hearts, four_of_diamonds, six_of_clubs, eight_of_spades, ten_of_hearts, queen_of_diamonds, king_of_clubs]) == 6
    assert isFullHouse([ace_of_clubs, ace_of_diamonds, king_of_hearts, six_of_spades, queen_of_clubs, jack_of_diamonds]) == 6
    assert isFullHouse([ace_of_hearts, two_of_hearts, three_of_hearts, four_of_hearts, five_of_hearts]) == 6

def test_isStraight_cases():
    assert isStraight([nine_of_spades, ten_of_spades, jack_of_spades, queen_of_spades, king_of_spades]) == 0
    assert isStraight([three_of_hearts, four_of_hearts, five_of_hearts, six_of_hearts, seven_of_hearts]) == 0
    assert isStraight([ace_of_clubs, queen_of_clubs, queen_of_hearts, jack_of_clubs, king_of_clubs, ten_of_clubs]) == 0
    assert isStraight([ten_of_diamonds, jack_of_diamonds, queen_of_diamonds, king_of_diamonds, ace_of_diamonds]) == 0
    assert isStraight([ace_of_spades, two_of_spades, three_of_spades, four_of_spades, five_of_spades]) == 0

    # === FALTA 1 CARTA (1) ===
    assert isStraight([two_of_hearts, ten_of_hearts, jack_of_hearts, queen_of_hearts, king_of_hearts, three_of_clubs]) == 1
    assert isStraight([nine_of_spades, ten_of_spades, jack_of_spades, king_of_spades]) == 1
    assert isStraight([jack_of_clubs, queen_of_clubs, king_of_clubs, ace_of_clubs, two_of_hearts]) == 1

    # === FALTAN 2 CARTAS (2) ===
    assert isStraight([ten_of_hearts, jack_of_hearts, queen_of_hearts, three_of_spades, seven_of_clubs]) == 2
    assert isStraight([queen_of_diamonds, king_of_diamonds, ace_of_diamonds, four_of_clubs]) == 2

    # === FALTAN 3 CARTAS (3) ===
    assert isStraight([jack_of_clubs, nine_of_clubs, two_of_hearts, five_of_diamonds]) == 3
    assert isStraight([jack_of_spades, ace_of_spades, three_of_hearts]) == 3

    # === FALTAN 4 CARTAS (4) ===
    assert isStraight([king_of_diamonds, two_of_clubs]) == 4
    assert isStraight([five_of_hearts]) == 4

    # === IMPOSIBLE (6) ===
    assert isStraight([ace_of_hearts, ace_of_clubs, ace_of_spades, ace_of_diamonds, two_of_hearts]) == 6
    assert isStraight([two_of_spades, four_of_spades, six_of_spades, eight_of_spades, ten_of_spades, queen_of_spades, ace_of_spades]) == 6

def test_isFlush_cases():
    # === CASOS PERFECTOS (0) ===
    assert isFlush([two_of_hearts, five_of_hearts, seven_of_hearts, nine_of_hearts, king_of_hearts]) == 0
    assert isFlush([ace_of_spades, three_of_spades, six_of_spades, ten_of_spades, jack_of_spades, queen_of_spades]) == 0
    assert isFlush([four_of_diamonds, eight_of_diamonds, nine_of_diamonds, ten_of_diamonds, king_of_diamonds, ace_of_diamonds, two_of_diamonds]) == 0

    # === FALTA 1 CARTA (1) ===
    assert isFlush([three_of_clubs, six_of_clubs, seven_of_clubs, nine_of_clubs, queen_of_hearts]) == 1
    assert isFlush([two_of_hearts, four_of_hearts, five_of_hearts, eight_of_hearts, ace_of_spades, three_of_spades]) == 1

    # === FALTAN 2 CARTAS (2) ===
    assert isFlush([ten_of_spades, jack_of_spades, three_of_spades, six_of_diamonds]) == 2
    assert isFlush([king_of_diamonds, ace_of_diamonds, four_of_diamonds]) == 2

    # === FALTAN 3 CARTAS (3) ===
    assert isFlush([nine_of_clubs, two_of_clubs]) == 3
    assert isFlush([five_of_hearts, seven_of_hearts]) == 3

    # === FALTAN 4 CARTAS (4) ===
    assert isFlush([queen_of_spades]) == 4
    assert isFlush([three_of_diamonds, two_of_spades]) == 4

    # === IMPOSIBLE (6) ===
    assert isFlush([two_of_hearts, four_of_diamonds, six_of_clubs, eight_of_spades, ten_of_hearts, queen_of_diamonds, king_of_clubs]) == 6
    assert isFlush([ace_of_clubs, ace_of_diamonds, king_of_hearts, six_of_spades, queen_of_clubs, jack_of_diamonds]) == 6
    assert isFlush([ten_of_clubs, jack_of_hearts, queen_of_diamonds, king_of_spades, ace_of_hearts, two_of_spades, three_of_clubs]) == 6

def test_isThreeofaKind_cases():
    # === CASOS PERFECTOS (0) ===
    assert isThreeofaKind([four_of_clubs, four_of_diamonds, four_of_hearts, ace_of_spades, king_of_hearts]) == 0
    assert isThreeofaKind([jack_of_spades, jack_of_diamonds, jack_of_hearts, two_of_clubs, three_of_diamonds, five_of_hearts]) == 0
    assert isThreeofaKind([nine_of_hearts, nine_of_diamonds, nine_of_clubs]) == 0

    # === FALTA 1 CARTA (1) ===
    assert isThreeofaKind([six_of_spades, six_of_clubs, seven_of_diamonds, ten_of_hearts]) == 1
    assert isThreeofaKind([queen_of_hearts, queen_of_diamonds, two_of_clubs, ace_of_spades, two_of_hearts, three_of_diamonds]) == 1

    # === FALTAN 2 CARTAS (2) ===
    assert isThreeofaKind([eight_of_hearts, nine_of_diamonds, three_of_clubs, five_of_spades]) == 2
    assert isThreeofaKind([ten_of_clubs, ace_of_diamonds, four_of_hearts]) == 2

    # === IMPOSIBLE (6) ===
    assert isThreeofaKind([ace_of_clubs, ace_of_diamonds, king_of_hearts, king_of_spades, queen_of_clubs, jack_of_diamonds, nine_of_clubs]) == 6
    assert isThreeofaKind([two_of_spades, three_of_spades, four_of_spades, five_of_spades, six_of_spades, seven_of_spades]) == 6
    assert isThreeofaKind([ten_of_hearts, jack_of_hearts, queen_of_hearts, king_of_hearts, ace_of_hearts, three_of_diamonds, three_of_clubs]) == 6

def test_isTwoPairs_cases():
    # === CASOS PERFECTOS (0) ===
    assert isTwoPairs([three_of_clubs, three_of_diamonds, five_of_hearts, five_of_spades, ace_of_hearts]) == 0
    assert isTwoPairs([king_of_spades, king_of_diamonds, queen_of_hearts, queen_of_clubs, two_of_hearts, three_of_diamonds]) == 0
    assert isTwoPairs([ten_of_hearts, ten_of_diamonds, four_of_clubs, four_of_spades]) == 0

    # === FALTA 1 CARTA (1) ===
    assert isTwoPairs([nine_of_hearts, nine_of_diamonds, six_of_clubs, seven_of_spades]) == 1
    assert isTwoPairs([jack_of_hearts, jack_of_diamonds, three_of_clubs, four_of_spades, ace_of_hearts, two_of_diamonds]) == 1
    
    # === FALTAN 2 CARTAS (2) ===
    assert isTwoPairs([eight_of_hearts, nine_of_diamonds, four_of_clubs]) == 2
    assert isTwoPairs([ace_of_clubs, ace_of_diamonds, ace_of_hearts, ace_of_spades]) == 2

    # === IMPOSIBLE (6) ===
    assert isTwoPairs([ace_of_clubs, two_of_diamonds, king_of_hearts, six_of_spades, queen_of_clubs, jack_of_diamonds]) == 6
    assert isTwoPairs([two_of_spades, three_of_spades, four_of_spades, five_of_spades, six_of_spades, seven_of_spades, eight_of_spades]) == 6
    assert isTwoPairs([ten_of_clubs, jack_of_hearts, queen_of_diamonds, king_of_spades, ace_of_hearts, nine_of_clubs]) == 6

def test_isPair_cases():
    # === CASOS PERFECTOS (0) ===
    assert isPair([four_of_clubs, four_of_diamonds, ace_of_spades, king_of_hearts, seven_of_hearts]) == 0
    assert isPair([jack_of_spades, jack_of_diamonds, two_of_clubs, three_of_diamonds, five_of_hearts]) == 0
    assert isPair([nine_of_hearts, nine_of_diamonds, ace_of_clubs, king_of_clubs]) == 0

    # === FALTA 1 CARTA (1) ===
    assert isPair([six_of_spades, seven_of_clubs, ten_of_hearts, queen_of_diamonds]) == 1
    assert isPair([queen_of_hearts, king_of_diamonds, ace_of_spades, two_of_hearts, three_of_diamonds]) == 1
    
    # === IMPOSIBLE (6) ===
    assert isPair([ace_of_clubs, king_of_hearts, queen_of_clubs, jack_of_diamonds, nine_of_clubs, ten_of_clubs, six_of_clubs]) == 6
    assert isPair([two_of_spades, three_of_spades, four_of_spades, five_of_spades, six_of_spades, seven_of_spades, eight_of_clubs]) == 6
    assert isPair([ten_of_hearts, jack_of_hearts, queen_of_hearts, king_of_hearts, ace_of_hearts, three_of_diamonds, four_of_clubs]) == 6  

def test_analyze_cases():
    assert analyze([ace_of_clubs, ace_of_diamonds, ace_of_hearts, king_of_spades, king_of_diamonds]) == 80  # Full House
    assert analyze([two_of_clubs, ace_of_clubs]) == 0
    