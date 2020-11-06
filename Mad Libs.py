#Mad Libs

from pathlib import Path
import os

os.chdir = Path('C:/Users/thikr/OneDrive/Documentos/Lernen/Python/Projects/Mad Libs/')
text = open('text.txt').read()

textList = list(text.split(" "))


for i in range(len(textList)):
    if textList[i][-1].isalpha():
        if textList[i] == 'ADJECTIVE':
           print('Enter an adjective:')
           textList[i] = input()
        elif textList[i] == 'VERB':
           print('Enter a verb:')
           textList[i] = input()
        elif textList[i] == 'NOUN':
           print('Enter a noun:')
           textList[i] = input()
    else:
        if textList[i][:-1] == 'ADJECTIVE':
           print('Enter an adjective:')
           textList[i] = input() + textList[i][-1]
        elif textList[i][:-1] == 'VERB':
           print('Enter a verb:')
           textList[i] = input() + textList[i][-1]
        elif textList[i][:-1] == 'NOUN':
           print('Enter a noun:')
           textList[i] = input() + textList[i][-1]


newText = " ".join(textList)

newTextFile = open('newText.txt', 'w')
newTextFile.write(str(newText))

newTextFile.close()

print(newText)


