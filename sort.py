import shutil
import os

choose = int(input("Enter your sorting file choice: \n1. Images\n2. Audio/Music\n3. videos\n4. PDF files\nchoose: "))
usource = input("Enter source address: ")
udest = input("Enter destination address: ")
files = os.listdir(usource)
source = usource + "\\"
dest = udest + "\\"

while True:

        #ForImages
        if choose == 1:
            for f in files:
                if os.path.splitext(f)[1] in (".jpg", ".gif", ".png", ".jpeg"".webp", ".tiff", ".psd", ".raw", ".bmp", ".heif", ".indd", ".heic"):
                    shutil.move(source+f, dest)
                    break
        #ForAudio
        elif choose == 2:
            for f in files:
                if os.path.splitext(f)[1] in (".mp3", ".wav"):
                    shutil.move(source+f, dest)
                    break
        #ForVideos
        elif choose == 3:
            for f in files:
                if os.path.splitext(f)[1] in (".3gp", ".webm", ".mpg", ".ogg", ".mp4", ".m4p", ".m4v", ".avi",".wmv",".mov", ".qt",".flv", ".swf",):
                    shutil.move(source+f, dest)
                    break
        #ForPDF
        elif choose == 4:
            for f in files:
                if os.path.splitext(f)[1] in (".pdf"):
                    shutil.move(source+f, dest)
                    break
        break







