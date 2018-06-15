file = open("myFile.txt",'r')
word = list()
final = list()
tempW = list()
couDict = list()
for line in file:
    for i in line.split():
        word.append(i)

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
for li in final:
    wc = dict()
    for i in li:
        wc[i] = wc.get(i, 0) + 1
    couDict.append(wc)

final = list()
for i in couDict:
    l = dict()
    for key, value in sorted(i.items(), key=lambda item: (item[1], item[0])):
        l[key] = value
    final.append(l)
print(final)

flag = True
enterText = input("Enter The word")
for i in final:
    if(flag):
        temp = list(i.keys())
        if enterText == temp[0]:
            print("Next Word Will Be ",temp[-1])
            flag = False
        else:
            continue
