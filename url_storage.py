#! python3

import os, shelve, pyperclip, sys

#determine if getting from copyPaste or from command line or from input


def checkArguments(pictures):
   if (len(sys.argv) == 1):
      print("no command line arguments")
   elif (len(sys.argv) == 2):
      appendItem(pictures, sys.argv[1])
   else:
      print("System only takes 1 image at a time, for now")
      sys.exit()
   

def quitProgram():
   print("Exiting Program")
   sys.exit()

def listStorage(storage):
   print("Printing Storage")
   for x in storage:
      print(x)
      
def appendItem(pictures, item):
   print('appending to storage')
   pictures.append(newPicture)
   
def popOldest(storage):
        try:
            print(pictures.pop(0))
        except:
            print("Out of images to pop")
   
def main():
    
    pictures = []
    newPicture = ''
    
    os.chdir("C:\\Users\\Sylos\\Documents\\Projects\\PythonScripts\\url_storage")
    
    with shelve.open('url_storage') as storage:
        if len(storage) == 0:
            #deal with having an empty storage file
            storage['pictures'] = pictures   
            print("Storage is empty")
        pictures = storage['pictures']

    checkArguments(pictures)
   
    while True:
        print("enter command or image")
        newPicture = input()

        if (newPicture.lower() == 'q' or newPicture.lower() == 'quit'):
            quitProgram()
        elif (newPicture.lower() == 'l' or newPicture.lower() == 'list'):
            listStorage(pictures)
            continue;
        elif (newPicture.lower() == 'p' or newPicture.lower() == 'pop'):
            print("Getting oldest of : ", end="")
            popOldest(pictures)
            continue;
        else:
            appendToPictures(pictures, newPicture)
            
        
    with shelve.open('url_storage') as storage:
        storage['pictures'] = pictures   


if __name__ == '__main__':
    main()
