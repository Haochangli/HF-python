vowels= {'a','e','i','o','u'}
words = input("Provide a word to search for vowels.")
i = vowels.intersection(set(words))
print (i)
