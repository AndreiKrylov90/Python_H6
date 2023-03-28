# # Проверить делится ли двадцатизначное число на 7?
# Число делится на 7, если результат вычитания удвоенной 
# последней цифры из числа десятков этого числа делится на 7 или равен 0.

s = "234523642345789812354678654323454919865"

index = 1
summa = 0
while len(s) > 0:
    troika = int(s[-3: ])
    if index % 2 == 1:
        summa = summa - int(troika)
    else:
        summa = summa + int(troika)
    index +=1
    s = s[:-3]

if summa % 7 ==  0:
    print(f"Число делится на 7")
else:
    print(f"Число не делится на 7")
