exams = [
    [10,12,2,11,11],
    [12,13,10,15,13],
    [15,6,8,9,15],
    [16,9,15,14,14],
    [5,15,9,12,5],
]
totalScore = 0
choice = input("Which day would you like the average for?").upper()
match choice:
    case "MONDAY":
        day = 0
    case "TUESDAY":
        day = 1
    case "WEDNESDAY":
        day = 2
    case "THURSDAY":
        day = 3
    case "FRIDAY":
        day = 4

for i in exams:
    totalScore = totalScore + exams[i][day]