import random
from tkinter import *
from tkinter import messagebox

text = "abcdefghijklmnopqrstuvwxyz0123456789"
window = Tk()
window.title('Captcha App')
window.geometry('1200x700')
window.config(bg ="red")
captcha = StringVar()
user_input = StringVar()

def set_captcha():
	s = random.choices(text, k=6)
	captcha.set(''.join(s))

def check():
	if captcha.get()==user_input.get():
		messagebox.showinfo("Success","Correct")
	else:
		messagebox.showerror("Error","Incorrect")
	set_captcha()
	
Label(window,textvariable = captcha,bg="darkcyan",font = "Arial 30 bold").pack()

Entry(window,textvariable =user_input, font = "Arial 25 bold").pack()

Button(window, command = check, text = "Check", font = "Arial 25 bold").pack()




window.mainloop()
