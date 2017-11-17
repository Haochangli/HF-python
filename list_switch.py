K = int(input("Please provide a value K: "))
ls = list(input("Please provide a list:"))
newls = []
output = []

for i in range(0,len(ls),K):
    newls.append(ls[i:i+K])

for list_len in range(len(newls)):
    newls[list_len].reverse()

for list_len in range(len(newls)):
    for value_k in range(K):
        try:
            output.append(newls[list_len][value_k])
        except:
            break
            
print(output)
