print('What is your name?') #ask for their name
name = input()
print('It is good to meet you, ' + my_name)
print('The length of your name is:')
print(len(my_name))
print('What is your age?') #ask for their age
my_age = input()
print('You will be ' + str(int(my_age)+ 1) + ' in a year. ')



name = input()
if name == 'Alice':
    print('Hi, Alice.')
    print ('How old are you?')
    age = input()
    age = int(age)
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you, Alice ia not an undead, immortal vampire.')
