import copy
print('I will take the words and divide them into each letters')
List_1 = []
List_2 = copy.copy(List_1)
while True:
	print('give me the words at ' + str(len(List_1))+ ' place')
	name_1 = input()

	if name_1 == '':
		break

	List_1 = List_1 + [[name_1]]
	
	List_2 += name_1

print('here are the words first, now i will scatter them')


print(List_1)
print('\n')
print(List_2)
for List_1 in range(len(List_1)
Str_1 = ''.join(List_1[List_1][List_1])
print(Str_1)

