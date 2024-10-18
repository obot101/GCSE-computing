def sayHello():
    print("Hello world",)

for i in range(2):
    sayHello()

def getAge():
    return input("How old are you\n")

print(f"{getAge()}. Damn your old!")