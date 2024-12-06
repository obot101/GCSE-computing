n = int(input("Start of string: "))
i = int(input("Position in string: "))
whole_string = str(n)
while True:
    n += 1
    whole_string = whole_string + str(n)
    if len(n) >= i:
        print(whole_string[i])
        break
    else:
        continue