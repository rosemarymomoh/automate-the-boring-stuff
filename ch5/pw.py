#! python3

#pw.py - an insecure password locker program

PASSWORDS = {'email': ' F7rerere9wwq3ngpw91',
             'blog': 'VMfitru14923f56ness32',
             'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # the first command line arg is the name of the account you're looking to retrieve its password

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
else:
    print('There\'s no account named ' + account)
