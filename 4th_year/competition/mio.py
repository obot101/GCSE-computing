n = int(input("Start of string:"))
i = int(input("Position in string:"))
q = 0
whole_string = str(n)

for i in range(2):
    n = n+1
    whole_string = whole_string + str(n)
    
print(whole_string)