 def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

a = float(input('First: '))
b = float(input('Second: '))
op = input('Operation (sum/sub/mul/div): ')

if op == 'sum':
    print(f'a + b = {sum(a, b)}')
elif op == 'sub':
    print(f'a - b = {sub(a, b)}')
elif op == 'mul':
    print(f'a * b = {mul(a, b)}')
elif op == 'div':
    print(f'a / b = {div(a, b)}')
else:
    print('Invalid Operation!')
