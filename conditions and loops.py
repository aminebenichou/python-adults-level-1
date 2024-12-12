



numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for i in numbers :
    print(i)

# give me a while statement that prints 
# each element of the list
i = 0
while i<len(numbers):
    print(numbers[i])
    i += 1


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
results = []
x = 0
for i in numbers:
    x = x + i
    
    results.append(x)

if (results[0]==1):
    del results[0]
print(results)
