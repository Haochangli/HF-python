from bottle_challenge_function import consume,empty_bottle_exchange,bottle_cover_exchange

current_beer_num = 5
empty_bottle_num = 0
bottle_cover_num = 0
beer_consume = 0

while (current_beer_num > 0):
    current_beer_num,empty_bottle_num, bottle_cover_num, beer_consume = consume(current_beer_num,empty_bottle_num, bottle_cover_num, beer_consume)
    current_beer_num,empty_bottle_num, bottle_cover_num, beer_consume = empty_bottle_exchange(current_beer_num,empty_bottle_num, bottle_cover_num, beer_consume)
    current_beer_num,empty_bottle_num, bottle_cover_num, beer_consume = bottle_cover_exchange(current_beer_num,empty_bottle_num, bottle_cover_num, beer_consume)
    print ("Current beer number:" + str(current_beer_num))
    print ("Current bottle number:" + str(empty_bottle_num))
    print ("Current bottle cover number:" + str(bottle_cover_num))
    print ("----------------------------------------------------")   
    
