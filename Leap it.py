import tkinter as tk 
root = tk.Tk() 
root.geometry("500x400")
root.configure(background='light yellow')
root.title(" Leap Year ") 

name_var=tk.IntVar()

def Take_input(): 
    INPUT = name_var.get()
##    INPUT= int(INPUT)
    print(INPUT)
    if(INPUT == 0):
        lbl = tk.Label(root, text=" \n      PLZ. Enter Valid Year        \n", fg="green", bg="light green").place(x=150,y=250)

    elif(INPUT % 4 and INPUT % 100 and INPUT % 400) == 0:
        lbl = tk.Label(root, text=" \n      Year is Leap....        \n", fg="green", bg="light green").place(x=150,y=250)

    else:
        lbl = tk.Label(root, text=" \n      Year is NOT Leap....        \n", fg="red", bg="light green").place(x=150,y=250)
   
l1 =tk.Label(text="     LEAP YEAR OR NOT   ", font=("bold",20),fg="red",bg = "light yellow")
l1.place(x=60,y=60)

l = tk.Label(text = "Enter the Year" ,width=15,font=("bold",10),bg = "light yellow").place(x =60, y= 130)


inputtxt = tk.Entry(root,textvariable = name_var , 
                bg = "light yellow").place(x=220,y=130)



Display = tk.Button(root, height = 1, 
                 width = 20,background = "white",text ="Show", 
                 command = lambda:Take_input()).place(x=150,y=180)
 

  
root.mainloop() 
