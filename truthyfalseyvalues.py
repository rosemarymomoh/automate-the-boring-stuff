import sys
##name = ''
##while not name:
##    print('Enter your name:')
##    name = input()
##print('How many guests will you have?')
##num_of_guests = int(input())
##if num_of_guests:
##    print('Be sure to have enough room for all your guests.')
##    print('Done')
##    

##i=0
##for i in range(5):
##    print('Jimmy Five Times ('+ str(i)+ ')')

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
    
