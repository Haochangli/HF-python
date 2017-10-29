pharse = "Don't panice!"
plist = list(pharse)
print (pharse)
print (plist)

"""
new_pharse = plist[1:8]
new_pharse.remove("'")
new_pharse.insert(2,new_pharse.pop(3))
new_pharse.extend([new_pharse.pop(),new_pharse.pop()])
new_pharse = "".join(new_pharse)
"""

new_pharse = "".join(plist[1:3])
new_pharse = new_pharse + "".join([plist[5],plist[4],plist[7],plist[6]])

print(plist)
print (new_pharse)
