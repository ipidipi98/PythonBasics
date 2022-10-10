city = input()
volume_saless = float(input())
comission = 0
flag = True
if city == 'Sofia':
    if 0 <= volume_saless <= 500:
        comission = volume_saless * 0.05
    elif 500 < volume_saless <= 1000:
        comission = volume_saless * 0.07
    elif 1000 < volume_saless <= 10000:
        comission = volume_saless * 0.08
    elif volume_saless > 10000 :
        comission = volume_saless * 0.12
    else:
        flag = False
elif city == 'Varna':
    if 0 <= volume_saless <= 500:
        comission = volume_saless * 0.045
    elif 500 < volume_saless <= 1000:
        comission = volume_saless * 0.075
    elif 1000 < volume_saless <= 10000:
        comission = volume_saless * 0.10
    elif volume_saless > 10000 :
        comission = volume_saless * 0.13
    else:
        flag = False
elif city == 'Plovdiv':
    if 0 <= volume_saless <= 500:
        comission = volume_saless * 0.055
    elif 500 < volume_saless <= 1000:
        comission = volume_saless * 0.08
    elif 1000 < volume_saless <= 10000:
        comission = volume_saless * 0.12
    elif volume_saless > 10000 :
        comission = volume_saless * 0.145
    else:
        flag = False

else:
    flag = False

if flag:
    print(f'{comission:.2f}')
else:
    print('error')