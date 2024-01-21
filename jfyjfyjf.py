a=int(input("tell your number"))
b=int(input("tell your number"))
summ=0
summch=0
summ9=0
for i in range(a,b+1):
    if i%2!=0:
        summ+=i
    if i%2==0:
        summch+=i
    if i%9==0:
        summ9+=i
print("Сумма нечетных: ",summ)
print("Сумма четных: ",summch)
print("Сумма кратных на 9: ",summ9)
#2
length = int(input("Enter the length of the line: "))
symbol = input("Enter the symbol to fill the line: ")

for i in range(length):
    print(symbol)
    #3
print( int(input("tell your number"))
a = None
while a != 7:
    a = int(input())
    if a > 0:
        print('Number is positive')
    elif a < 0:
        print('Number is negative')
    else:
        print('Number is equal to zero')
    if a == 7:
        print('Good bye!')
        #4
print( int(input("tell your number")))
q = 0
q_max = 0
q_min = 0
while (True):
    a = int(input("Введите число"))
    if a == 7:
        print("Пока")
        break
    elif a > q_max:
        q_max = a
    q = q + a

print('Сумма введенных чисел равна ', q)
print("Максиммальное из введенных чисел это - ", q_max)

