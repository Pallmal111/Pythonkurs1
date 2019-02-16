a=int(input('Введите первое число:'))
b=int(input('Введите второе число:'))
if a > b:
    t = a
    a = b
    b = t
s=0
for i in range(a,b+1):
    s=s+1
    print(s)