
num = 21
userNo = eval(input("guess a number"))
if userNo == num:
    print("congrats")
    print(" iam winner")
else:
    print("wrong guess")
print("plz enter the number")



num = 21
userNo = eval(input("guess a number"))

prize1 ="instabook"
prize1="workbook"

if userNo == num:
    print("congrats")
    print(" iam winner")
    option=eval(input("please choose your prize, press 1 for workbook or 2 for  instabook "))
    if option ==1:
        print("prize1+ has been packed")
    elif option ==2:
        print("prize2+ has been packed")
    else:
        print("sorry wrong value, plz try again")
else:
    print("wrong guess")
    print("plz enter the number")