#! python3

import os, pyperclip, sys, json, picture as pic

#determine if getting from copyPaste or from command line or from input


def checkArguments(pictures):
   if (len(sys.argv) == 1):
      print("no command line arguments")
   elif (len(sys.argv) == 2):
      if(sys.argv[1] == 'p'):
         appendItem(pictures, pic.Picture(pyperclip.paste()))
      else:
         appendItem(pictures, pic.Picture(sys.argv[1]))
   else:
      print("System only takes 1 image at a time, for now")
      sys.exit()
   

def quitProgram(pictures, cur_pointer):
   
    print("Writing to json then closing")
    with open("url_storage.json","w") as storage:
        json_pictures = []
        for x in pictures:
            json_pictures.append(x.__dict__)
        pre_file = {'pointer': {'cur_pointer':cur_pointer}, 'pictures':json_pictures}
        json.dump(pre_file, storage)
        
    print("Exiting Program")
    sys.exit()

def listStorage(storage):
   print("Printing Storage")
   for x in storage:
      print(x.toString())
      
def appendItem(pictures, item):
   print('appending to storage')
   pictures.append(pic.Picture(item))


def viewLatest(pictures,latest):
         try:
            if (latest < len(pictures)):
               picture = pictures[latest]
               print("Views: " + str(picture.views) + " " + picture.picture)
               latest +=1
            else:
               print("End of list of length: " + str(len(pictures)))

            return latest
         except:
            print("Out of images to pop")

            
def popOldest(pictures):
        try:
            picture = pictures.pop(0)
            print("Views: " + str(picture.views) + " " + picture.picture)
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
                    for x in json_file[i]:
                        pictures.append(pic.Picture(x['picture'], x['views']))
                                        
        except Exception as e:
            print("Error reading file: ", end="")
            print(e)

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
            print("Getting oldest of : " + str(len(pictures)))
            popOldest(pictures)
            continue;
        elif (newPicture.lower() == 'v' or newPicture.lower() == 'view'):
            print("Last viewed value is: " + str(cur_pointer) + "/" \
                 +  str(len(pictures)))
            cur_pointer =  viewLatest(pictures,cur_pointer)
        elif (newPicture.lower() =='?' or newPicture.lower() == 'help'):
            print('''Commands:\n
    (Q)uit -- exit program\n
    (L)ist -- list all stored pictures and view count\n
    (P)op  -- Pop the oldest image off and delete it\n
    (V)iew -- Display oldest new iamge and increment view counts\n
    (?)Help - Display this
                    ''')
                    
        else:
            appendItem(pictures, newPicture)
            
   
if __name__ == '__main__':
    main()
