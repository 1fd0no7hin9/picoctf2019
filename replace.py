def replace(source, char, index):
	return source[:index]+char+source[index+1:]

a="0"*32
char = ['d', '7', 'r', '5', 'r', 'c', '4', '3', 'b', '_', '4', '3', 't', 'c', 'l', 'H', 'c', '_', 'm', '5', 'r', '3', '4', 'T', 'H', '1', 'f', '_', '3', 'e', '5', 'd']
index = [0, 29, 4, 2, 23, 3, 17, 1, 7, 10, 5, 9, 11, 15, 8, 12, 20, 14, 6, 24, 18, 13, 19, 21, 16, 27, 30, 25, 22, 28, 26, 31]

for i in range(32):

	a=replace(a, char[i], index[i])

print(a)