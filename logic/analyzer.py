# ***************************************************************************************
# Significados especiales de la devolución de las funciones de comprobación
# 0 : LA MANO ES DE LO QUE SEA
# 6 : YA NO SE PUEDE ALCANZAR LA MANO CON LAS CARTAS ACTUALES
# ***************************************************************************************

import json
from collections import Counter


# Funcion para cargar todas las cartas de deck.json y las devolverlas como una lista de diccionarios.
def load_deck():
    with open('database/deck.json', "r") as f:
        deck = json.load(f)
    return [card for card in deck.values()]


def analyze(hand):
    #calcular, dado una mano de cartas, la probabilidad de cada tipo de mano
    royalflush_prob = (1 / isRoyalFlush(hand) * 52) if isRoyalFlush(hand) != 6 else 0
    straightflush_prob = (1 / isStraightFlush(hand) * 13) if isStraightFlush(hand) != 6 else 0 #Aun tengo que pensar en la probabilidad de que salga carta que cumpla la condicion de straight flush
    fourofakind_prob = (1 / isFourofaKind(hand) * 13) if isFourofaKind(hand) != 6 else 0
    fullhouse_prob = (1 / isFullHouse(hand) * 13) if isFullHouse(hand) != 6 else 0
    flush_prob = (1 / isFlush(hand) * 4) if isFlush(hand) != 6 else 0
    straight_prob = (1 / isStraight(hand) * 10) if isStraight(hand) != 6 else 0
    threeofakind_prob = (1 / isThreeofaKind(hand) * 13) if isThreeofaKind(hand) != 6 else 0
    twopair_prob = (1 / isTwoPairs(hand) * 13) if isTwoPairs(hand) != 6 else 0
    par_prob = (1 / isPair(hand) * 13) if isPair(hand) != 6 else 0
    highcard_prob = 1

    #insertar en variables el valor de cada mano completa (asignado a criterio personal)
    royalflush_value = 100
    straightflush_value = 100
    fourofakind_value = 90
    fullhouse_value = 80
    flush_value = 60
    straight_value = 50
    threeofakind_value = 40
    twopair_value = 30
    par_value = 20
    highcard_value = 0
    
    total_value = (royalflush_value * royalflush_prob + straightflush_value * straightflush_prob + fourofakind_value * fourofakind_prob + fullhouse_value * fullhouse_prob +
                   flush_value * flush_prob + straight_value * straight_prob + threeofakind_value * threeofakind_prob + twopair_value * twopair_prob + par_value * par_prob + highcard_value * highcard_prob) / 9

    return total_value

def isRoyalFlush(card_list):
    return_value = 0

    # Tomamos las cartas que tengan value > 10 (es decir, que sean un [10, 'jack', 'queen', 'king' o 'ace'])
    mapped_cards = [i for i in card_list if i.value >= 10]

    cards_suit = [card.suit for card in mapped_cards]

    try: 
        counter = Counter(cards_suit)
        mode = max(counter, key=counter.get) #El palo más repetido
    except ValueError:
        mode = None #Evitar error si la mano no tiene cartas con value > 10

    remaining_card_values = [10, 11, 12, 13, 14]
    cards_values = [card.value for card in mapped_cards if card.suit == mode]
    remaining_card_values = set(remaining_card_values) - set(cards_values)

    # Si me faltan tantas cartas que en las que me faltan para 7 no podría conseguir la mano
    if len(card_list) + len(remaining_card_values) > 7: 
        return_value = 6 
    else:
        return_value = len(remaining_card_values) # Número de cartas para tener Royal Flush
    return return_value


def isStraightFlush(card_list):
    return_value = 0
    min_missing_values = 4

    cards_suit = [card.suit for card in card_list]
    counter = Counter(cards_suit)
    mode = max(counter, key=counter.get) #El palo más repetido
    cards_values = [card.value for card in card_list if card.suit == mode]
    #Ordenación y eliminación de duplicados
    cards_values = sorted(cards_values)
    # CASO 1: Tenemos un as, por lo que necesitamos comprobar tambien el caso suave (as = 1)
    if cards_values[-1] == 14: 
        cards_values_soft = cards_values.copy()
        cards_values_soft.remove(14)
        cards_values_soft.insert(0, 1)

        listas_a_comparar = [cards_values, cards_values_soft]
        minimo = 999 #Numero convenientemente alto para comparar
        for listas in listas_a_comparar:
            for value in listas:
                missing_cards = 4 
                for next_value in range(value + 1, value + 5):
                    if next_value in listas:
                        missing_cards -= 1
                minimo = min(missing_cards, minimo)
            if len(card_list) + minimo > 7:
                return_value = 6
            else:
                return_value = minimo # Para estandarizar nomenclatura

    # CASO 2: No tenemos as, por lo que comprobamos normalmente
    else:
        for value in cards_values:
            missing_cards = 4 
            for next_value in range(value + 1, value + 5):
                if next_value in cards_values:
                    missing_cards -= 1
            min_missing_values = min(missing_cards, min_missing_values)
        if len(card_list) + min_missing_values > 7:
            return_value = 6
        else:
            return_value = min_missing_values # Para estandarizar nomenclatura
    return return_value


def isFourofaKind(card_list):
    return_value = 0
    card_values = []
    for card in card_list:
        card_values.append(card.value)

    contador = Counter(card_values)
    repetidos = max(contador.values())

    if len(card_values) - repetidos > 3: #Si la cantidad de cartas dadas que no son el posible póker es mayor de 3, hacer póker es imposible
        return_value = 6
    else:
        return_value = 4 - repetidos

    return return_value


def isFullHouse(card_list):
    return_value = 0
    card_values = []
    for card in card_list:
        card_values.append(card.value)

    contador = Counter(card_values)
    repeticiones = list(contador.values())
    repeticiones.sort()

    if repeticiones[-1] >= 3: 
        if len(repeticiones) > 1 and repeticiones[-2] >= 2:
            return_value = 0
        elif len(repeticiones) > 1:
            return_value = 1
        else:
            return_value = 2
    else:
        if repeticiones[-1] == 2:
            if len(repeticiones) > 1 and repeticiones[-2] == 2:
                return_value = 1
            elif len(repeticiones) > 1:
                return_value = 2
            else:
                return_value = 3
        else:
            return_value = 3

    if len(card_values) + return_value > 7:
        return_value = 6

    return return_value

def isStraight(card_list):
    card_values = []
    for card in card_list:
        card_values.append(card.value)
        
    contador = 5
    card_values.sort()
    for i in range(len(card_values)-1): #Idea: despues de ordenar, si el valor siguiente - el actual da 1, no hace nada, si no se le resta 1 al contador. El ultimo no se hace
        if card_values[i+1] - card_values[i] == 1:
            contador -= 1
    return_value = contador
    

    return return_value

def isFlush(card_list):
    return_value = 0

    cards_suit = [card.suit for card in card_list]
    counter = Counter(cards_suit)
    mode = max(counter.values())
    missing_cards = 5 - mode
    if len(card_list) + missing_cards > 7:
        return_value = 6
    else: 
        return_value = missing_cards
    
    if return_value < 0:
        return_value = 0

    return return_value

def isThreeofaKind(card_list):
    return_value = 0
    card_values = []
    for card in card_list:
        card_values.append(card.value)

    contador = Counter(card_values)
    repetidos = max(contador.values())

    if len(card_values) - repetidos > 4:
        return_value = 6
    else:
        return_value = 3 - repetidos
    
    if repetidos == 4: # (hipotesis) Pierrot sobreestimará el valor de la mano si es poker porque tambien será trio y par, asi que en esos casos anulamos la mano anterior
        return_value = 6

    return return_value

def isTwoPairs(card_list):
    return_value = 0
    card_values = []
    for card in card_list:
        card_values.append(card.value)

    contador = Counter(card_values)
    repetidos = list(contador.values())
    repetidos.sort()

    if repetidos[-1] >= 2:
        if len(repetidos) > 1 and repetidos[-2] >= 2:
            return_value = 0
        elif len(repetidos) > 1:
            return_value = 1
        else:
            return_value = 2
    else:
        if len(repetidos) == 1:
            return_value = 3
        else:
            return_value = 2
    
    if len(card_values) + return_value > 7:
        return_value = 6

    return return_value

def isPair(card_list):
    return_value = 0
    card_values = []
    for card in card_list:
        card_values.append(card.value)

    contador = Counter(card_values)
    repetidos = max(contador.values())

    if len(card_values) - repetidos > 6:
        return_value = 6
    else:
        return_value = 2 - repetidos
    
    if len(card_list) == 7 and return_value == 1: 
        return_value = 6

    return return_value