vowels = ['a','e','i','o','u']
word = input("Provide a word to search for vowels:")
found = {}
"""
for vowel in vowels:
    found[vowel] = 0
"""
for letter in word:
    if letter in vowels:
        found.setdefault(letter,0)
        found[letter] += 1

for k,v in sorted(found.items()):
    print ("Letter ", k, " appeared " , v, " time(s).")
    
