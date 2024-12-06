n = int(input("Start of string:"))
i = int(input("Position in string:"))
whole_string = str(n)

while n > i:
    n = n + 1
    i = i - 1
    if i == 0:
        print(n)
        break
    else:
        continue
print(whole_string)