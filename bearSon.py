
word = "bottles"
for count in  range( 99, 0, -1):
    print (count, word, "of beer on the wall.")
    print (count, word, "of beer.")
    print ("Take one down.")
    print ("Pass it around.")
    if count == 1:
        print ("No more bottles of beer on the wall.")
    else:
        if count - 1 == 1:
            word = "bottle"
        print(count - 1, word, "of beer on the wall.")
    print()
