birthdays = {'Alice': 'April 12', 'Bob':'December 31', 'Carol':'March 4'}

while True:
    print('Enter a name: (Blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of '+ name)
    else:
        print('I do not have birthday information for '+name)
        print('What is their Birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database update')

    
