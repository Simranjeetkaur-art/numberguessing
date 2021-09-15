from tkinter import *
root = Tk()
root.geometry('500x400')
root.resizable(0,0)
root.configure(background='light blue')
root.title("Website Blocker")
Label(root, text ='WEBSITE BLOCKER' , font ='arial 20 bold',bg = "light blue").place(x= 115 , y = 20)

host_path ='C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'
Label(root, text ='Enter Website :' , font ='arial 13 bold',bg = "light blue").place(x=25 ,y=106)
Websites = Text(root,font = 'arial 10',height='1.5', width = '40', wrap = WORD, padx=5, pady=5)
Websites.place(x= 170,y = 100)
def Blocker():
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                Label(root, text = 'Already Blocked!!!' , font = 'arial 15 bold',fg = "red",bg = "light blue").place(x=160,y=170)
                pass
            else:
                host_file.write(ip_address + " " + website + '\n')
                Label(root, text = "Blocked!!!", font = 'arial 15 bold',fg = "green",bg = "light blue").place(x=160,y =170)


block = Button(root, text = 'Block',font = 'arial 12 bold',pady = 5,command = Blocker ,width = 15, bg = 'royal blue1', activebackground = 'sky blue')
block.place(x = 150, y = 230)
root.mainloop()
