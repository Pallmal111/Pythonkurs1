print('calculator')
x =float(input('ENTER FIRST NUMBER'))
y=float(input('ENTER SECOND NUMBER'))

e =(input('ENTER THE OPERATION >>> (+,-,/,*,mod,pow,div) = '))

if e=='+':
    result=x+y
elif e=='-':
    result=x-y
elif e=='*':
    result=x*y
elif e=='mod':
    result=x%y
elif y != 0:
    if e=='/':
     result=x/y
    elif e==pow:
        result=pow(x,y)
    elif e=='div':
        result=x//y
elif y == 0:
    result='Деление на ноль!'
print('Result of operations>>>',result)


# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
