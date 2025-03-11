number = input("")
splitNumber =  number.split()
if splitNumber[0] + splitNumber[1] + splitNumber[2] == 15 and splitNumber[3] + splitNumber[4] + splitNumber[5] == 15 and splitNumber[6] + splitNumber[7] + splitNumber[8] == 15 and splitNumber[0] + splitNumber[3] + splitNumber[6] == 15 and splitNumber[1] + splitNumber[4] + splitNumber[7] == 15 and splitNumber[2] + splitNumber[5] + splitNumber[8] == 15 and splitNumber[0] + splitNumber[4] + splitNumber[8] == 15 and splitNumber[2] + splitNumber[4] + splitNumber[6]:
    print("magic")
else:
    print("muggle")
