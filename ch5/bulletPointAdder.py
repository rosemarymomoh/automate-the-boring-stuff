#! python3
# bulletPointAdder.py - adds Wikipedia bullet points to the start of each text
# on the clipboard

#steps:
#Paste text from the clipboard
#Separate lines of text
#Modify lines
#join
#Copy the new text to the clipboard

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = "* " + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)
