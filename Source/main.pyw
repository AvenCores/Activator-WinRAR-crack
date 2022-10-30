import sys
from tkinter import Tk,Canvas,PhotoImage,Button,messagebox,Label,CENTER
from requests import get
from os import system

root = Tk()
root.title('Activator WinRAR')
root.geometry('400x300')
root.resizable(width=False, height=False)

f=open(r'banner.png', "wb")
ufr = get("https://i.imgur.com/Pea4LkY.png")
f.write(ufr.content)
f.close()

canvas = Canvas(root, height=400, width=400)
canvas.pack()
bannerimg = PhotoImage(file='banner.png')
renderImg = canvas.create_image(200,80, image=bannerimg)

def goinstallkey():
    lines = ["RAR registration data", "hzfsoft", "Unlimited Company License", "UID=41075b9d18d904e98ab0", "64122122508ab0841c1fa203a621981d6b720ee513acd972c83952", "10d6d4dd47a2b11bd04560fce6cb5ffde62890079861be57638717", "7131ced835ed65cc743d9777f2ea71a8e32c7e593cf66794343565", "b41bcf56929486b8bcdac33d50ecf7739960cf892eda0660311493", "c8b5d1e6c7b497fbb3d3b8621ec3a8ddf317387f56b54e028b3ab0", "b6eac0ccab0822a014f9827a0e48c989c4b72b59383d59b3602da1", "1857cb59fbb2b953885e1eb272671a6d071f9b8de7be2863583398"]
    with open(r"rarreg.key", "w") as file:
        for  line in lines:
            file.write(line + '\n')
    system("del /Q C:\Program Files\WinRAR\rarreg.key")  
    system("move /Y rarreg.key C:\Program Files\WinRAR")
    messagebox.showinfo(title="Установлено!", message='Кряк был успешно установлен! Перезапустите WinRAR.')

def goremovekey():
    system("del /Q C:\Program Files\WinRAR\rarreg.key")
    messagebox.showinfo(title="Удалено!", message='Кряк был успешно удален! Перезапустите WinRAR.')

installkey = Button(text='Установить кряк WinRAR', bg="green", fg="white", command=goinstallkey)
installkey.place(x=120, y=200)

delkey = Button(text='Удалить кряк WinRAR', bg="red", fg="white", command=goremovekey)
delkey.place(x=120, y=240)

poetry = 't.me/hzfnews'
label3 = Label(text=poetry, justify=CENTER)
label3.place(x=5, y=280)

root.mainloop()
system("del /Q banner.png")