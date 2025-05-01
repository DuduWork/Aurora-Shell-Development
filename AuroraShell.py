import os
import logging

if os.path.exists("./SYSTEM/") == False:
    os.mkdir("./SYSTEM/")

if os.path.exists("./STORAGE/") == False:
    os.mkdir("./STORAGE/")

print("Welcome to Aurora Shell-64")
print("Command Line Library:\n\n┌──────────────────┐\n│ >CMDS   >TYPE    │\n│ >LOAD   >CHDISK  │\n│ >COPLFL >INFO    │\n│ >VER    >EDIT    │\n│ >DIR             │\n│                  │\n│ DISK OPTIONS     │\n│                  │\n│ >DISKWRITE       │\n└──────────────────┘\n® KiddieOS Community | FREE USE OF THE PRODUCT | OPEN SOURCE\n") #18 lenght

try:
    def Interpreter(executing = True, CMDProgram = True):
        try:
            AUTODIR = open("./SYSTEM/AUTODIR.ACP", 'x')
            AUTODIR.write("STORAGE/")
            direct = AUTODIR
            AUTODIR.close()
        except FileExistsError:
            AUTODIR = open("SYSTEM/AUTODIR.ACP", 'r')
            tempmemory = AUTODIR.read()
            print("current Storage Directory is:", tempmemory + ". to change, edit it by the Host File explorer or try finding it by the shell at SYSTEM/>")
            direct = tempmemory
            if os.path.exists(tempmemory) == False:
                print("An Fatal Error has Occured: The Storage Path Set Does not Exists, Resetting The AUTODIR.ACP")
                os.remove("SYSTEM/AUTODIR.ACP")
                input("Press Enter to Quit the Program.")
                return False

        while executing == True:
            currentDirectory = direct
            while CMDProgram == True:
                argumentCarriage = []
                directoryTempStorage = {}
                argumentEnd = 0
                argumentStart = 1
                argumentCarryStart = 0
                argumentCarryStart2 = 0
                Command = input(str(currentDirectory) + ":>")
                arguments = Command.split()
                if not arguments:
                    print("Not A Command.")
                    continue
                arguments[0] = arguments[0].upper()
                #________________________________________________________________________________________
                # Commands (Default)
                #________________________________________________________________________________________

                if arguments[0] == "DIR":
                    if len(arguments) == 2:
                        dirresult = arguments[1]
                        if os.path.exists(dirresult) == False:
                            print("Can not Show Content from a unexistent directory")
                            continue
                        directoryTempStorage = os.listdir(str(dirresult))
                        for content in directoryTempStorage:
                            item_path = os.path.join(dirresult, content)
                            if os.path.isdir(item_path):
                                print("| <DIR> ", content)
                            elif os.path.isfile(item_path):
                                print("| <FILE>", content)
                    elif len(arguments) == 1:
                        directoryTempStorage = os.listdir(currentDirectory + "./")
                        for content in directoryTempStorage:
                            item_path = os.path.join(currentDirectory, content) # Adicionado para obter o caminho completo
                            if os.path.isdir(item_path):
                                print("| <DIR> ", content)
                            elif os.path.isfile(item_path):
                                print("| <FILE>", content)
                elif arguments[0] == "CHDISK" or "CD":
                    try:
                        previousDirectory = currentDirectory
                        currentDirectory = currentDirectory + "\\" + arguments[1]
                        if os.path.exists(currentDirectory) == False:
                            currentDirectory = arguments[1]
                        if os.path.exists(currentDirectory) == False:
                            print("The Path/Directory does not Exists")
                            currentDirectory = previousDirectory
                            continue
                        else:
                            print("| Changed to:", currentDirectory)
                    except IndexError:
                        print("An Error Occured while Trying to Change Directory, you may have put an Space argument, negative argument, or any thing that caused an Index Error")
                elif arguments[0] == "INFO":
                    if len(arguments) > 1:
                        print("Expected no Argument, we Expect only <INFO>")
                    else:
                        print("| Shell Version: 1.0\n| Creator: duduWorks\n| Dev Community: KiddieOS.Community\n| Main Code: Python 3.x\n| Interpreter Version Status: BETA\n| Copy right Status: Free For All\\Open Source")
                if CMDProgram != True:
                    print("An Fatal Error has Occured: Can not Run The Shell If the CMD Interpreter is Not Running.")
                    input("\nPress Enter to Quit the Program.")
                elif arguments[0] == "VER":
                    if len(arguments) == 2:
                        fileresult = currentDirectory + "\\" + arguments[1]
                        if os.path.exists(fileresult) == False:
                            print("File/directory Does not Exists")
                            continue
                        elif os.path.exists(fileresult):
                            fsiz = os.path.getsize(fileresult)
                            fdat = os.path.getmtime(fileresult)
                            print("| F/D Data:\n|- Size:", str(fsiz) + "\nLast Modified:", str(fdat))
                    else:
                        print("Usage: VER <file/file's Directory")
                elif arguments[0] == "TYPE":
                    if len(arguments) == 2:
                        fileresult = currentDirectory + "\\" + arguments[1]
                        print("Checking File.." + "\n\n" + fileresult + "\n")
                        if os.path.exists(fileresult) == False:
                            print("File Does not Exists")
                        if os.path.exists(fileresult):
                            chfile = open(fileresult, 'r')
                            toprint = chfile.read()
                            print(toprint)
                        else:
                            print("usage: TYPE <file/file's Directory>")
                elif arguments[0] == "WRITED":
                    diskname = arguments[1]
                    disksectors = int(arguments[2])
                    diskfile = open(diskname + ".img", 'wb')
                    for sectors in int(disksectors):
                        diskfile.write("0x00" * 512)



    Interpreter()
except Exception as error:
    errorflag = True
    while errorflag == True:
        logging.error("an exception has occured", exc_info=True)
        input()
        errorflag = False