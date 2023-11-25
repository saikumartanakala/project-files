'''while statement:-
if support repeated execution of statements that is controlled
by conditional expression
while 0<10(print("hello world"))
while statement can also include in else clause
two sort of loops:
while and for
while loop is a special statement along with while statement  are break
and continuous
if the loop condition is false then the while stetement ends
if the loop condition is true then the while stetement gets executed
loop condition is given with some operatives
the loop body should contain code which eventually makes loop condition false
a loop that is in a function body also ends if a return ststement is provided
'''
number = 21

prize1="book"

prize2="python"

trials=3;


while(trials>0):
    userno = eval(input("guess the number"))
    if userno == number:
        print("congrats")
        print(" iam winner")
        option = eval(input("please choose your prize, press 1 for workbook or 2 for  instabook "))
        if option == 1:
            print("prize1+ has been packed")
        elif option == 2:
            print("prize2+ has been packed")
        else:
            print("sorry wrong value, plz try again")
        print("your trial  ghjgjhgjhgjg is ends")
    else:
        print("wrong guess")
        print("plz enter the number")
        call = eval(input("its working"))
        if call == 2:
            print("it is done")
    trials=trials-1
print("your trial  is ends")


'''

sample = 20
output = eval(input("enter required number"))

case1="working"
case2="not working"

trials=1;

while(trials>0):
    output2 = eval(input("enter value"))
    if output == sample:
        print("winner")
        print("congrats")
    elif output2 == 2:
        print("prize2+ has been packed")
    else:
        print("you lose the game")
        print("try again")
    trials=trials-1'''