"""
  author : Akshay Vilekar

  Main File / Driver file for the
  Program. This script sets up gui
  and displays control options to
  user.

"""

## imports 
import Tkinter
import load
import encrypt
import about
import os
import sys



## set up master window
master = Tkinter.Tk()

## set buttons and other things
load_button = Tkinter.Button( master,text = 'load',command 
                              = load.load)
encrypt_button = Tkinter.Button( master,text = 'encrypt',command 
                                 = load.encrypt)

decrypt_button = Tkinter.Button( master,text = 'decrypt',command 
                                 = load.decrypt)


##fullscreen mode
master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(),
                                     master.winfo_screenheight()))


## pack items
load_button.pack()
encrypt_button.pack()


# place items
load_button.place( relx=0.5 , rely=0.1 ,
                     relheight = 0.05 ,relwidth = 0.1)
encrypt_button.place( relx=0.5 , rely=0.2 ,
                       relheight = 0.05 ,relwidth = 0.1)

decrypt_button.place( relx=0.5 , rely=0.3 ,
                       relheight = 0.05 ,relwidth = 0.1)

## mainloop
master.mainloop()
