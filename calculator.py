
print('hey its a calculator')
print('select from thr below')
print('select 1 for addtion, 2 for multiplication, 3 for division, 4 for substract')

while True:
    try:
        opearation = int(input('select 1 or 2 or 3 or 4 : '))
        break
    except ValueError:
        print("pls enter a number")

while True:
    try:
        num1 = int(input("pls enter the first number : "))
        break
    except ValueError:
        print("pls enter a number")
while True:
    try:
        num2 = int(input("pls enter the 2nd number : "))
        break
    except ValueError:
        print("enter a number")



if opearation is 1:
    print('the sum of this is ', num1+num2)
elif opearation is 2:
    print('the multiplication of this is ', num1*num2)
elif opearation is 3:
    print('the division of this is ', num1/num2)
elif opearation is 4:
    print('the substaction of this is ', num1-num2)
else:
    print('pls select a vaild option')
