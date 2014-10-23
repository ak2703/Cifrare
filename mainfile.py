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

## set up images 
back_image = Tkinter.PhotoImage(file = './img/back.png')
load_image = Tkinter.PhotoImage(file = './img/load.png'  )
enc_image  = Tkinter.PhotoImage(file = './img/enc.png'   )
dec_image  = Tkinter.PhotoImage(file = './img/dec.png'   )


## set background label
back_label = Tkinter.Label(master , image = back_image)


## set buttons 
load_button = Tkinter.Button( master,image = load_image,command 
                              = load.load)
encrypt_button = Tkinter.Button( master,image = enc_image,command 
                                 = load.encrypt)

decrypt_button = Tkinter.Button( master,image = dec_image,command 
                                 = load.decrypt)


##fullscreen mode
master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(),
                                     master.winfo_screenheight()))


## pack items
load_button.pack()
encrypt_button.pack()
decrypt_button.pack()
back_label.pack()


# place items
back_label.place(x=0,y=0,relheight=1,relwidth = 1)

load_button.place( relx=0.5 , rely=0.2 ,
                     height = 50 ,width = 200)
encrypt_button.place( relx=0.5 , rely=0.4 ,
                       height = 50 ,width = 200)

decrypt_button.place( relx=0.5 , rely=0.6 ,
                       height = 50 ,width = 200)


## mainloop
master.mainloop()

