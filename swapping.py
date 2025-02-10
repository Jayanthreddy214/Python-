a=int(input("enter the 1st num: "))
b=int(input('enter the 2nd num: '))
print('the values of x and y before swapping are {},{}' .format(a,b))
a,b = b,a
print('the values of x,y after swapping are {},{}' .format(a,b))