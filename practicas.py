array= []
array_new= [1, 2, 3, 4, 5, 6, 7]
array_new.reverse()
print(array_new)

email= input('Ingrese su email: ')

for i in email:
   
    print( i ,end=' ' )
    array.append(i)

print('\n')
print(array)
array.reverse()
array_new= array
print(array_new)

index= array_new.index('@')

print(index)

longitud= len(array_new)

print(longitud)

del array_new [index+1:]

array1= array_new

print(array1)

email= False

for i in array_new:
    if i =='.':
        email= True



if email :
    print('\n \nEl email es correcto')
else:
    print('\nEl email no es el correcto')

print('\n-------------')

email= input('Ingrese su email: ')

def validacion(email):
    array= []
    for i in email:
        array.append(i)
    
    array.reverse()
    
    index= array.index('@')
    
    del array [index+1:]
    email= False

    for i in array:
        if i =='.':
            email= True

    if email :
        print('\n \nEl email es correcto')
    else:
        print('\nEl email no es el correcto')

validacion(email)
print('\n-------------')

