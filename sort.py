import os
def makefolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
pick = input("Enter path from where to pick")
drop = input("Enter path where to drop")
select = int(input("Enter types of file 1. for image \n 2. for video \n 3.for audio \n 4. for pdf or doc \n 5. ""for everything to arrange"))
try:
    if select == 1:
        makefolder('Images')
        os.
    elif select == 2:
        pass
    elif select == 3:
        pass
    elif select == 4:
        pass
    elif select == 5:
        pass
except ValueError:
    print("you must enter a number not alphabets: ")
files =os.listdir(pick)

makefolder('Video')
makefolder('Audio')
makefolder('docs')
