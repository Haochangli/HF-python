pharse = "Don't panice!"
plist = list(pharse)
print (pharse)
print (plist)

new_pharse = plist[1:8]
new_pharse.remove("'")
new_pharse.insert(2,new_pharse.pop(3))
new_pharse.extend([new_pharse.pop(),new_pharse.pop()])
new_pharse = "".join(new_pharse)

print(plist)
print (new_pharse)
