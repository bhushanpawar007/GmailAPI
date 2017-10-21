'''
Created on Oct 21, 2017

@author: BHUSHAN
'''
from tkinter import *
from bhushan.gmail.ui import authorizeClickHandler 

window=Tk()
window.geometry("800x500")
window.resizable(0,0)
window.title("Welcome to the GMAIL Data Mining")
#making frames to seperate the connect button and welcome msg
#topFrame=Frame(window)
#topFrame.pack()

#bottomFrame=Frame(window)
#bottomFrame.pack(side=BOTTOM)


#welcome message
WelcomeText=Label(window,text="Welcome to the GMAIL Data Mining ..!!")
WelcomeText.config(font=("Courier", 24))
WelcomeText.grid(row=0,column=0)
WelcomeText.grid(padx=50, pady=50)

#connect button to authorize the account
ConnectButton=Button(window,command=authorizeClickHandler.buttonClick(),text="Connect to get insights of your GMAIL Account",fg='green',bg='black')
ConnectButton.config(font=("Courier", 12))
ConnectButton.grid(row=1,column=0)
ConnectButton.grid(padx=20, pady=120)

window.mainloop()

