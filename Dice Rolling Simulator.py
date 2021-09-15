import tkinter
import random

root = tkinter.Tk()
root.geometry('600x600')
root.configure(background='light cyan')
root.title('Roll The Dice')


BlankLine = tkinter.Label(root, text="",bg = "light cyan")
BlankLine.pack()

HeadingLabel = tkinter.Label(root, text="Dice Rolling Simulator",
   fg = "Red",
   bg = "light green",
   font = "Helvetica 16 bold italic")
HeadingLabel.pack()

BlankLine1 = tkinter.Label(root, text="",bg = "light cyan")
BlankLine1.pack()


label = tkinter.Label(root, text='', font=('Helvetica', 260))

def roll_dice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)}',bg = "light yellow")
    label.pack()

button = tkinter.Button(root, text='    Roll Dice   ',font = "Helvetica 8 bold italic" ,foreground='blue',background= 'white' ,command=roll_dice)
button.pack()

BlankLine2 = tkinter.Label(root, text="",bg = "light cyan")
BlankLine2.pack()

root.mainloop()
