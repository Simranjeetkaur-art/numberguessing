
import tkinter  as tk
import re
  
# creates a Tk() object 
master = tk.Tk()


# set the background colour of GUI window 
master.configure(background='light blue')

# set the title of GUI window
master.title("Slicer") 
master.resizable(0,0)

# sets the geometry of main  
# root window 
master.geometry("500x700")


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
name_var=tk.StringVar()

def check(email):
     email = name_var.get()
    # pass the regular expression 
    # and the string in search() method
     
     if(re.search(regex,email)):
         lblLine1 = tk.Label(master, text = "******************************************************************************",font=("bold",15),fg="black",bg="light blue").place(x=0,y=260)
         label_2 =tk.Label(master,text="     Here is your Sliced Result!!!     ",bg ="light cyan",font=("bold",20))
         label_2.place(x=30,y=300)

         
         label_3 =tk.Label(master,text="  Email Address  :", bg ="light blue",font=("bold"))
         label_3.place(x=30,y=380)
         label_4 =tk.Label(master,text=email,  bg ="light blue",font=("bold"))
         label_4.place(x=280,y=380)
         
         user_name = email[:email.index("@")]
         label_5 =tk.Label(master,text="   USER NAME   :", bg ="light blue",font=("bold"))
         label_5.place(x=30,y=420)
         label_6 =tk.Label(master,text=user_name, fg="green", bg ="light blue",font=("bold"))
         label_6.place(x=300,y=420)
         
##         server_name = email[email.index("@")+1:email.index(".")]
##         label_7 =tk.Label(master,text="   SERVER      :", bg ="light blue",font=("bold"))
##         label_7.place(x=30,y=450)
##         label_8 =tk.Label(master,text=server_name, fg="green", bg ="light blue",font=("bold"))
##         label_8.place(x=300,y=450)
         
         server_name = email[email.index("@")+1:]
         label_9 =tk.Label(master,text="   DOMAIN    :", bg ="light blue",font=("bold"))
         label_9.place(x=30,y=480)
         label_10 =tk.Label(master,text=server_name, fg="green", bg ="light blue",font=("bold"))
         label_10.place(x=300,y=480)
          
     else:
         lblLine1 = tk.Label(master, text = "******************************************************************************",font=("bold",15),fg="black",bg="light blue").place(x=0,y=260)
         label_21 =tk.Label(master,text="     Invalid Format!!!     ",fg ="red", bg ="light cyan",font=("bold",20))
         label_21.place(x=100,y=400)   
        
        
    
lblLine2 = tk.Label(master, text = "******************************************************************************",font=("bold",15),fg="black",bg="light blue").place(x=0,y=2)
label_0 =tk.Label(master,text="       E-MAIL SLICER    ",bg ="light cyan", width=20,font=("bold",20))
label_0.place(x=90,y=60)

label_1 =tk.Label(master,text="Enter your Email Address",bg ="light cyan", width=20,font=("bold",10))
label_1.place(x=70,y=132)

name_entry = tk.Entry(master,textvariable = name_var, font=('bold',10))
name_entry.place(x=250,y=132)

sub_btn= tk.Button(master,text = 'Submit',width=20,height=2,background="white",command = lambda:check(name_var)).place(x=180,y=200)



master.mainloop()
