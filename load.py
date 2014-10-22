"""
   author : Akshay Vilekar
 
   Load the dialog box and choose file


"""

## imports

import tkFileDialog
import tkMessageBox
import tkSimpleDialog
import os

# global variable filename
infilename = ''

## change filename from empty to other
def updatefilename(filename):
    global infilename
    infilename = filename
    
def encrypt():
     global infilename
     if infilename != '' :
         password = tkSimpleDialog.askstring('pass',"Enter password"
                                             ,show="*")
         ## release the canons
         cmd = "openssl aes-256-cbc -in " + str(infilename) + " -out " +str(infilename) + ".enc " + " -k " + str(password)
         o = os.system(cmd)
         print o
     else:
           tkMessageBox.showerror('error',"Please select a file")


def load():

    ## Open file box and select file(file object)
    input_file  =  tkFileDialog.askopenfilename()

    ## set the input filename in encrypt.py to this value
    global infilename
    infilename = updatefilename(str(input_file))

   
########################################################
