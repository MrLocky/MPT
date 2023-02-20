while True:
   print("Введите год:")
   year = int(input())
   common = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,]
   result = 0
   if year > 0 and (((year % 4 == 0) and not (year % 100 == 0)) or (year % 400 == 0)) :
        for month in range(12):
            for date in range(common[month] +1):
                if 0 < date < 10:
                    result += date
                elif date >= 10:
                    l = [int(n) for n in str(date)]
                    for p in range(2):
                        result += l[p]
        print(result + 11)
   elif year > 0:
        for month in range(12):
            for date in range(common[month] +1):
                if 0 < date < 10:
                    result += date
                elif date >= 10:
                    l = [int(n) for n in str(date)]
                    for p in range(2):
                        result += l[p]
        print(result)
   else:
       print("Не может быть года меньше 0")