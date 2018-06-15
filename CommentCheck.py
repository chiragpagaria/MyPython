positiveword = list()
negativeword = list()
file = open("PositiveWord.txt","r")

for line in file:
    for i in line.split():
        positiveword.append(i.lower())

file.close()

print(positiveword)

file = open("NegativeWord.txt","r")

for line in file:
    for i in line.split():
        negativeword.append(i.lower())

file.close()

print(negativeword)
sentence = list()
statement = input("Enter Statement")

for i in statement.split():
    sentence.append(i.lower())

positive = 0
negative = 0
neutral = 0
i = 0
while(i < len(sentence)):
    if sentence[i] in positiveword:
        positive += 1
    elif sentence[i] in negativeword:
        negative += 1
    else:
        neutral += 1

    i+=1

print("Length Of Sentence : ",len(sentence))
print("Number Of Positive Words : ",positive)
print("Number Of Negative Words : ",negative)
print("Number Of Neutral Words : ",neutral)