user_name = input("Hi, I am Rasputin, what's yours?")

name = user_name.split(" ")

user_input = input(f"Hi, {name[-1]} how are you?").upper()

user_feeling = user_input.upper().split("I AM ")

user_answer = input(f"Why do you feel{user_feeling[-1].lower()}")