#! python3

import os, shelve, pyperclip, sys, json

#determine if getting from copyPaste or from command line or from input


def checkArguments(pictures):
   if (len(sys.argv) == 1):
      print("no command line arguments")
   elif (len(sys.argv) == 2):
      appendItem(pictures, sys.argv[1])
   else:
      print("System only takes 1 image at a time, for now")
      sys.exit()
   

def quitProgram(pictures, cur_pointer):
   
    print("Writing to json then closing")
    with open("url_storage.json","w") as storage:
        pre_file = {'pointer': {'cur_pointer':cur_pointer}, 'pictures':pictures}
        json.dump(pre_file, storage)
        
    print("Exiting Program")
    sys.exit()

def listStorage(storage):
   print("Printing Storage")
   for x in storage:
      print(x)
      
def appendItem(pictures, item):
   print('appending to storage')
   pictures.append(item)
   
def popOldest(pictures):
        try:
            print(pictures.pop(0))
        except:
            print("Out of images to pop")
            

def main():
    
    pictures = []
    json_file = []
    newPicture = ''
    cur_pointer = 0
    pref_file= {}
    os.chdir("C:\\Users\\Sylos\\Documents\\Projects\\PythonScripts\\url_storage")

    
    if not os.path.isfile("url_storage.json"):
        print("Error, file not found")
        with open("url_storage.json", 'w') as write_file:
            print("Creating file")
            pre_file = {'pointers': {"cur_pointer":0}, 'pictures':pictures}
            json.dump(pre_file, write_file)

    with open("url_storage.json", "r") as read_file:
        json_file = json.load(read_file)
        try:
            for i in json_file:
                if(i == 'pointers'):
                    cur_pointer = json_file[i]['cur_pointer']
                elif(i == 'pictures'):
                    pictures = json_file[i]
        except Exception as e:
            print("Error reading file: ", end="")
            print(e)
             
             
##    with shelve.open('url_storage') as storage:
##        if len(storage) == 0:
##            #deal with having an empty storage file
##            storage['pictures'] = pictures   
##            print("Storage is empty")
##        pictures = storage['pictures']

    checkArguments(pictures)
   
    while True:
        print("enter command or image")
        newPicture = input()

        if (newPicture.lower() == 'q' or newPicture.lower() == 'quit'):
            quitProgram(pictures, cur_pointer)
        elif (newPicture.lower() == 'l' or newPicture.lower() == 'list'):
            listStorage(pictures)
            continue;
        elif (newPicture.lower() == 'p' or newPicture.lower() == 'pop'):
            print("Getting oldest of : ", end="")
            popOldest(pictures)
            continue;
        else:
            appendItem(pictures, newPicture)
            
    
        
##    with shelve.open('url_storage') as storage:
##        storage['pictures'] = pictures   


if __name__ == '__main__':
    main()
