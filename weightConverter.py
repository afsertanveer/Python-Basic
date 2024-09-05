weight = int(input('Weight: '));
unit = input('(L) bs or (k)g:')
if unit.upper() == 'L' :
    weight = weight*0.45
    print(f'You are {weight} kilos')
else:
    weight = weight/0.45
    print(f'You are {weight} pound')
