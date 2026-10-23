# This is a simple implementation of run-length encoding in Python.
k = input("Enter a string to encode: ")
count = 0
for i in range(len(k)):
    count += 1
    if (i + 1) >= len(k) or k[i] != k[i + 1]:
        print( k[i] + str(count), end="")
        count = 0   