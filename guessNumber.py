import random  
import time                          
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog, messagebox







def play_game():
    number = random.randint(1, 2)
    guessesTaken = 0                     

    myName = simpledialog.askstring("Guessing Game", "Hello and welcome! What is your name?")

    messagebox.showinfo("hello, " + myName + "i am thinking of number between 1 and 2")
    time.sleep(1)
                                                                                   
    while guessesTaken < 3:
        guess = simpledialog.askinteger("take a guess!")
        
        guessesTaken += 1

        if guess < number:
            messagebox.showinfo('too low, again')

        if guess > number:
            messagebox.showifo('too high, go again')

        else:
            break                                                                   

    if guess == number:
        if guessesTaken == 1:
            messagebox.showinfo("u actually got it on the first try, good stuff")
        else:
            messagebox.showinfo("it only took you " + str(guessesTaken) + " times to get it, good job though")                

    else:
        messagebox.showinfo('nope, the number i was thinking of is ' + str(number))                                   


root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()


play_game()

root.mainloop()
