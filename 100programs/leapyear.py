num=2020
if num%4==0:
    if num%100==0:
        if num%400==0:
            print(num,"it is leap year")
        else:
            print(num,"is not leap year")
    else:
        print(num, "it is leap year")
else:
    print(num, "it is not leap year")

