#! python3

import os, shelve, pyperclip, sys

pictures = []

newPicture = ''

#determine if getting from copyPaste or from command line or from input
#if (len(sys.argv) == 1):
 #   print("no command line arguments") 
#elif (len(sys.argv) > 2):
    #print("Error, system only takes 1 image at a time")


os.chdir("C:\\Users\\Sylos\\Documents\\Projects\\PythonScripts\\url_storage")
with shelve.open('url_storage') as storage:
    if len(storage) == 0:
        #deal with having an empty storage file
        print("Storage is empty")
    pictures = storage['pictures']

while True:
    print("enter command or image")
    newPicture = input()

    if (newPicture.lower() == 'q' or newPicture.lower() == 'quit'):
        print("Quitting")
        break;

    if (newPicture.lower() == 'l' or newPicture.lower() == 'list'):
            print("Printing all stored URLS")
            for x in pictures:
                print(x)
            continue;

    if (newPicture.lower() == 'p' or newPicture.lower() == 'pop'):
        print("Getting oldest of : ", end="")
        print(len(pictures))
        try:
            print(pictures.pop(0))
        except:
            print("Out of images to pop")
        continue;
                
    print('appending picture')
    pictures.append(newPicture)
    
with shelve.open('url_storage') as storage:
    storage['pictures'] = pictures
  
    

    


