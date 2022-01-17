# Write your code here :-)
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    else:
        print('Hello Joe, What is the Password? (Hint: it is a fish.)')
        password = input()
        if password == 'swordfish':
            break
        else:
            print('Access Denied')
print('Access Granted')
