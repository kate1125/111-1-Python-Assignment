from hw5 import findPrime

p = findPrime()

print('>>> next(p)')
print(next(p), end='\n')

print('>>> next(p)')
print(next(p), end='\n')

print('>>> next(p)')
print(next(p), end='\n')

# 使用send()
print('>>> p.send(19)')
print(p.send(19) , end='\n')

print('>>> next(p)')
print(next(p), end='\n')


print('>>> next(p)')
print(next(p), end='\n')

# 使用send()
print('>>> p.send(8)')
print(p.send(8) , end='\n')

print('>>> next(p)')
print(next(p), end='\n')


print('>>> next(p)')
print(next(p), end='\n')

# 使用send()
print('>>> p.send(-6)')
print(p.send(-6) , end='\n')

print('>>> p.send(15)')
print(p.send(15) , end='\n')

print('>>> next(p)')
print(next(p), end='\n')

print('>>> next(p)')
print(next(p), end='\n')

# 使用send()
print('>>> p.send(0)')
print(p.send(0) , end='\n')

print('>>> p.send(-8)')
print(p.send(-8) , end='\n')

print('>>> next(p)')
print(next(p), end='\n')

print('>>> next(p)')
print(next(p), end='\n')

print('>>> p.send(\'abc\')')
print(p.send('abc') , end='\n')

print('>>> next(p)')
print(next(p), end='\n')

print('>>> next(p)')
print(next(p), end='\n')

input('press the ENTER key to exit...')
