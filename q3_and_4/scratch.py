# Just a scratchwork file.

test = ['a', 'b', 'c']

for i in range(len(test)):
    print("Before action of for loop:", test)
    test[i] = 'z'
    print("After action of for loop:", test, "\n")

print(test)