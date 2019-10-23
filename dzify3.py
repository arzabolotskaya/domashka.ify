print('C should be the ostatok from A delit na B, mate')

a = int(input('Enter A number: '))
b = int(input('Enter B number: '))
c = int(input('Enter C number: '))

x = a % b
if c == x:
    print('what a fight! you got it right!')
else:
    print('use your brain! try again!')
