exams = [
    [10,12,2,11,11],
    [12,13,10,15,13],
    [15,6,8,9,15],
    [16,9,15,14,14],
    [5,15,9,12,5],
]

choice = input("Which day would you like the average for?").upper()
match choice:
    case "MONDAY":
        day = 0
    case "TUESDAY":
        day = 1
    case "WEDNESDAY":
        day = 2
    
MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
for i in exams:
    exams[i]