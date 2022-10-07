from tkinter.font import BOLD
from turtle import bgcolor
from PIL import Image,ImageTk
import random
import tkinter

root = tkinter.Tk()
root.geometry('345x345')
root.title('Roll the Dice')
root['bg']="azure4"

count=1
number_of_dice=0
# declaring string variable
# for storing Number of Dise user want to roll
No_dice=tkinter.StringVar()
def submit():
  global number_of_dice
  name_label.configure(text="!!!!NOW PRESS ROLL THE DICE BUTTON BELOW!!!!")
  no_of_dice=No_dice.get()    #get the input 
  # print(type(no_of_dice),no_of_dice)
  number_of_dice=int(no_of_dice)    # type conversion string to int
  if number_of_dice>6:
    start_button.configure(text="### PRESS ME ###",command=root.destroy,bg="black",fg="white",width=25) # if number of dice are more than 6 then Exit
    sub_btn.configure(text="### Wrong Input ###",command=root.destroy,width=30)
    name_label.configure(text='### WRONG INPUT ###',width=30)
  else:
    sub_btn.configure(text="!!! PRESS ROLL THE DICE BUTTON !!!",command=name_entry.destroy,width=30)
    pass
  # print(type(number),number)
  No_dice.set("")
  
def Button_click():
    name_entry.destroy()
    submit()


def roll_dice():    #this function generate random dice image and then resize it.
  global count,number_of_dice
  # print(type(number_of_dice),number_of_dice)
  if number_of_dice==0:
    HeadingLabel.configure(text="### PLEASE ENTER NO OF DICE YOU WANT TO ROLL ###",font=('calibre',9, 'bold'),width=45)
    start_button.configure(text='THANK YOU',command=root.destroy,width=20,bg="black",fg="white",font='BOLD')

  elif count<number_of_dice:
    HeadingLabel.configure(text="NO ON {} DICE!".format(count))
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((140, 140)))
    # update image
    ImageLabel.configure(image=DiceImage)
    # keep a reference
    ImageLabel.image = DiceImage
    count=count+1
  else:
    HeadingLabel.configure(text="NO ON {} DICE!".format(count))
    start_button.configure(text='THANK YOU',command=root.destroy,width=20,bg="black",fg="white",font='BOLD')# For exiting the window



name_label = tkinter.Label(root, text = 'How many dice do you want to roll? [1-6] ',
font=('calibre',10, 'bold'),
fg='red',
bg='black')
name_label.pack()
name_entry = tkinter.Entry(root,textvariable = No_dice, font=('calibre',10,'normal'))
name_entry.pack()
sub_btn=tkinter.Button(root,text='Submit', command=Button_click,bg='black',fg='white')
sub_btn.pack()



BlankLine = tkinter.Label(root, text="",bg="azure4")
BlankLine.pack()              # blankspace in the starting

HeadingLabel = tkinter.Label(root, text="## ROLL THE DICE ##",
  fg = "blue",
  bg = "AntiqueWhite3",
  font = "Bold",
  width=20)
HeadingLabel.pack()           # Heading

dice = ['1.png', '2.png', '3.png','4.png', '5.png', '6.png'] # simulating the dice with random numbers between 0 to 6 and generating image

DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((140, 140)))
ImageLabel = tkinter.Label(root, image=DiceImage,bg="azure4")
ImageLabel.image = DiceImage
ImageLabel.pack(expand=True)
start_button = tkinter.Button(root, text='Roll the Dice', bg="black",fg="white",command=roll_dice,width=13,font='Bold')
# pack a widget in the parent widget
start_button.pack(expand=True)

root.mainloop()
