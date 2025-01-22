import time
print("Please enter 7 numbers:")
temperatures = []
for i in range(7):
    temp = int(input(f"Enter day {i + 1}: "))
    temperatures.append(temp)
average = 1
for i in temperatures:
    average = average * temperatures[i]

print(average)