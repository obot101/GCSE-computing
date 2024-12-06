n = int(input("Start of string: "))
i = int(input("Position in string: "))

if n < i:
    while n < i:
        n += 1
    print(n)
else:
    print(f"Starting value ({n}) is already greater than or equal to the position ({i}).")