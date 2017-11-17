def search4vowels(words):
    """Dispaly all vowels once in an supplied word."""
    vowels = set('aeiou')
    #words = input('Provide a word to search for vowels: ')
    found = vowels.intersection(set(words))
    for vowel in found:
        print (vowel)

        
