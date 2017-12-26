def consume(current_beer_num,empty_bottle_num, bottle_cover_num, beer_consume):
    current_beer_num = current_beer_num - 1
    empty_bottle_num = empty_bottle_num + 1
    bottle_cover_num = bottle_cover_num + 1
    beer_consume = beer_consume + 1
    print ("You had drunk:" + str(beer_consume) + " beer.")
    return current_beer_num,empty_bottle_num, bottle_cover_num, beer_consume

def empty_bottle_exchange(current_beer_num,empty_bottle_num, bottle_cover_num, beer_consume):
    if empty_bottle_num >= 2:
        empty_bottle_num = empty_bottle_num - 2
        current_beer_num = current_beer_num + 1
        print("Exchange new beer by empty bottle * 2")
    return current_beer_num,empty_bottle_num, bottle_cover_num, beer_consume

def bottle_cover_exchange(current_beer_num,empty_bottle_num, bottle_cover_num, beer_consume):
    if bottle_cover_num >= 4:
        bottle_cover_num = bottle_cover_num - 4
        current_beer_num = current_beer_num + 1
        print("Exchange new beer by bottle cover * 4")
    return current_beer_num,empty_bottle_num, bottle_cover_num, beer_consume
