print('welcom to ATM')
a=(input('insert card here: '))
print(a)
if a=='yes':
    print('card inserted successfully')
elif a=='no':
    print('please insert card')
    exit()
b=int(input('enter 4 digit pin:'))
print(b)
if b==1234:
    print('pin is correct')
else:
    print('pin is incorrect')
    exit()
c=(input('select language:'))
print(c)
if c=='1':
    print('you have selected language: English')
elif c=='2':
    print('you have selected language: Hindi')
elif c=='3':
    print('you have selected language: Telugu')
d=(input('select option:'))
print(d)
if d=='1':
    print('you have selected option: withdraw')
elif d=='2':
    print('you have selected option: deposit')
elif d=='3':
    print('you have selected option: balance enquiry')
e=int(input('enter amount to withdraw:'))
if (e<=0 and e>=10000):
    print(e)
    print('insufficient balance')
    exit()
print('plese wait')
print('please collect your cash')
f=(input('do you want to check balance:'))
if f=='yes':
    print('your balance is 9000')
elif f=='no':
    print('thank you for using ATM')
g=(input('do you want to print receipt:'))
if g=='yes':
    print('receipt printed successfully')  
elif g=='no':
    print('thank you for using ATM')
