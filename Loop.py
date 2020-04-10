#range(start,stop,step) 
'''
for i in range(0,12,3):
	print(i)

print('')

string = "String Traversal"
for i in range(len(string)):
	print(string[i])
print('')

for char in string: 
	print(char)

print('')

for i in range(3):
	for j in range(2):
		print(j)

print('')
'''

'''
# Print 10x10 Multiplication Table
for i in range(1,11):
	print('{:<3}|' .format(i), end="")

	for j in range(1,11):
		print('{:>4}' .format(i*j), end="")
	if i == 1:
		print(''.format(""), end="")
	print("")


condition = 10 
while condition != 0:
	print(condition)
	condition = condition -1


while True:
	print("Infinite")
	break

'''
def Numbers():
	for i in range(1,11):
		if i == 5: 
			continue
		print(i)
