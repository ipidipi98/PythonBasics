fruit = input()
day_of_week = input()
amount = float(input())
price = 0

if fruit not in ['banana' , 'apple' , 'orange' , 'grapefruit' ,'kiwi' , 'pineapple' ,  'grapes'] :
    print('error')
if day_of_week in ['Monday', 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday']:
    if fruit == 'banana':
        price = amount * 2.50
    elif fruit == 'apple':
        price = amount * 1.20
    elif fruit == 'orange':
        price = amount * 0.85
    elif fruit == 'grapefruit':
        price = amount * 1.45
    elif fruit == 'kiwi':
        price = amount * 2.70
    elif fruit == 'pineapple':
        price = amount * 5.50
    elif fruit == 'grapes':
        price = amount * 3.85

elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if fruit == 'banana':
        price = amount * 2.70
    elif fruit == 'apple':
        price = amount * 1.25
    elif fruit == 'orange':
        price = amount * 0.90
    elif fruit == 'grapefruit':
        price = amount * 1.60
    elif fruit == 'kiwi':
        price = amount * 3.00
    elif fruit == 'pineapple':
        prive = amount * 5.60
    elif fruit == 'grapes':
        price = amount * 4.20
else:
    print('error')

print(f'{price * amount:.2f}')


