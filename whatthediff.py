#file diff from command
#xxd kitter.jpg >> kitter
#xxd cattos.jpg >> cattos
#diff cattos kitter >> diff
file = []
with open('diff','r') as diff:
	
	for i in diff:
		# print(type(i), i)
		file.append(i)
original = []
new = []
for i in file:
	if i[0]=="<":
		# print("original : ", i)
		original.append(i)
	if i[0]==">":
		# print("new : ", i)
		new.append(i)
#split '<' '>' and address
index = 12
length = 39
#compre get hex which different
hexencode = ""
for i in range(len(new)):
	original[i] = original[i][index:index+length]	
	new[i] = new[i][index:index+length]
	hexOriginal = ""
	hexNew = ""
	j=0
	while j < len(new[i]):
		hexOriginal = original[i][j:j+4]
		hexNew = new[i][j:j+4] 
		j=j+5
		if hexOriginal[:2] != hexNew[:2]:
			hexencode += hexOriginal[:2]
		if hexOriginal[2:] != hexNew[2:]:
			hexencode += hexOriginal[2:]

print(hexencode)