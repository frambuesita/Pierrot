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


def analyze(card_list):
    value_list = [100, 99, 85, 80, 70, 55, 35, 15, 8, 0]
    fun_list = [isRoyalFlush(card_list), isStraightFlush(card_list), isFourofaKind(card_list), isFullHouse(card_list),
                isFlush(card_list), isStraight(card_list), isThreeofaKind(card_list), isTwoPairs(card_list), isPair(card_list), 0]
    
    compute_list = []
    for i in range(0, len(fun_list)):
        if fun_list[i] == 0:
            compute_list = fun_list[0:(i+1)]
            break
    
    initial_index = len(compute_list) -1
    initial_value = value_list[initial_index]

    size_list = [5, 5, 4, 5, 5, 5, 3, 4, 2, 1] 
    new_list = []
    for i in range(0, len(compute_list)):
        if compute_list[i] == 6:
            new_list.append(0)
        else:
            new_list.append(size_list[i] - compute_list[i])
    
    extra_value = 0
    total_to_mean = 0
    for i in size_list:
        total_to_mean += i
    
    for i in range(0,len(compute_list)):
        weight = size_list[i] / total_to_mean 
        extra_value += (value_list[i] - initial_value) * weight
    
    extra_value = extra_value / 4
    return_value = initial_value + extra_value

    return return_value
            
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
    return_value = 0
    min_missing_values = 4

    cards_values = [card.value for card in card_list]
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