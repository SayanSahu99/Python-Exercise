print('Program To Check The Validity Of a Password \n')
condition = [False, False, False, False]

small_letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
caps = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
small_letters = small_letters.split()
caps = caps.split()
numbers = '0 1 2 3 4 5 6 7 8 9'
numbers = numbers.split()
char = ['$', '#', '@']
valid_password = []

passwords = input('Enter comma seperated passwords ')
passwords = passwords.split(',')
count = 0

for password in passwords:
    count += 1
    for character in password:
        if character in small_letters:
            condition[0] = True

        if character in caps:
            condition[1] = True

        if character in numbers:
            condition[2] = True

        if character in char:
            condition[3] = True

    if False in condition:
        condition = [False, False, False, False]
        continue
    elif len(password) >= 6 and len(password) <= 12:
        valid_password.append(password)
        condition = [False, False, False, False]

for i in range(len(valid_password)):
    if i == len(valid_password) - 1:
        print(valid_password[i])
    else:
        print(valid_password[i], end = ',')
