events = [
  ["05/02/2023", "WS2", "Window", "38"],
  ["05/02/2023", "MS1", "Motion", "2"],
  ["06/02/2023", "DS3", "Door", "1"],
  ["06/02/2023", "MS2", "Motion", "3"],
  ["06/02/2023", "MS1", "Motion", "2"],
  ["07/02/2023", "WS1", "Window", "24"],
  ["07/02/2023", "DS1", "Door", "1"]
]
userDate = input("Please enter a date:")
for event in events:
    if userDate == event[0]:
        continue