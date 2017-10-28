pharse = "Don't panic"
plist = list(pharse)
print (pharse)
print (plist)

for count in range(3):
    if count == 1:
        plist.remove('D')
    plist.pop()

plist.remove("'")
plist.remove(' ')
letter_a = plist.pop()
plist.insert(3,letter_a)
plist.insert(2,' ')

new_pharse = "".join(plist)
print(plist)
print(new_pharse)
