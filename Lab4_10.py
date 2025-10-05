global result

def rectangle():
    a = float(input('Width: '))
    b = float(input('Height: '))
    global result
    result = a * b

def triangle():
    a = float(input('Base: '))
    h = float(input('Height: '))
    global result 
    result = 0.5 * a * h

figure = input('1 for rectangle, 2 for triangle: ')

if figure == '1':
    rectangle()
elif figure == '2':
    triangle()

print(f'Area: {result}')