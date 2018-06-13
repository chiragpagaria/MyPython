file = open("myFile.txt",'r')
word = list()
final = list()
tempW = list()
for line in file:
    for i in line.split():
        word.append(i)

print(word)

for i in range(len(word)-1):
    tempFinal = list()
    if word[i] not in tempW:
        indices = [j for j, x in enumerate(word) if x == word[i]]
        tempW.append(word[i])
        tempFinal.append(word[i])
        for k in indices:
            try:
                tempFinal.append(word[k+1])
            except:
                continue
        final.append(tempFinal)


    else:
        continue
print("________________FINAL_________________")
for i in final:
    print(i)

