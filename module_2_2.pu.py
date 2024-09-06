first=input('введите число:')
second=input('введите число:')
third=input('введите число:')
if first == second == third:
    print('3')
elif first==second or second == third or first == third:
    print('2')
else:
    print('0')