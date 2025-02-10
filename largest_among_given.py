num1 = int(input('enter 1st num: '))
num2 = int(input('enter 2nd num: '))
num3 = int(input('enter 3rd num: '))
if num1 > num2 and num1 > num3:
    print('num1 is the largest num')
elif num2 > num1 and num2 > num3:
    print('num2 is the largest num')
elif num3 > num1 and num3 > num2:
    print('num3 is the largest num')
else:
    print('null')