treeDigit = int(input("Please enter a 3 digit nunber"))

print(treeDigit // 100)
lastTwo = (treeDigit % 100) // 10
print(lastTwo // 10)
print(treeDigit % 10)