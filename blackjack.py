def value_of_card(card):
    match card:
        case "A":
            return 1
        case "J" | "Q" | "K":
            return 10
        case _:
            return int(card)
        
def higher_card(card_one, card_two):
    if (value_of_card(card_one) > value_of_card(card_two)):
        return card_one
    elif (value_of_card(card_one) < value_of_card(card_two)):
        return card_two
    else:
        return (card_one, card_two)
    
def value_of_ace(card_one, card_two):

    if (card_one == "A" or card_two == "A"): return 1


    if (value_of_card(card_one) + value_of_card(card_two)) <= 10:
        return 11
    else:
        return 1
        
print(value_of_card('A'))
print(value_of_card('J'))
print(value_of_card('4'))
print(value_of_card(5))

print('test higher_card')
print(higher_card('A','K'))
print(higher_card('A', 5))
print(higher_card('J','Q'))


print("testing value_of_ace")
print(value_of_ace('K','Q'))
print(value_of_ace('A','Q'))
print(value_of_ace(2,3))

