file = open("myfile.txt","r")
wc = dict()
for line in file:
    word = line.split()
    for i in word:
        wc[i] = wc.get(i,0)+1
for key in sorted(wc.keys()):
    print ("%s: %s" % (key, wc[key]))
print("-------------------Second Task----------------------")
for key, value in sorted(wc.items(), key=lambda item: (item[1], item[0])):
    print ("%s: %s" % (value, key))
