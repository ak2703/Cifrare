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
    
def encrypt():
     global infilename
     
     ## open the temporary file and deal with it
     filep  = open('filename.temp','r')
     infilename =filep.read()
     filep.close()
     os.system('rm filename.temp')
     #####

     if infilename != '' or infilename != None :
         password = tkSimpleDialog.askstring('pass',"Enter password"
                                            ,show="*")
         ## release the canons
         cmd = "openssl aes-256-cbc -in " + str(infilename) + " -out " +str(infilename) + ".enc " + " -k " + str(password)
         o = os.system(cmd)
         
     else:
           tkMessageBox.showerror('error',"Please select a file")

###################################################################

def decrypt():
    pass



##################################################################
def load():

    ## Open file box and select file(file object)
    input_file  =  tkFileDialog.askopenfilename()

    ## set the input filename in encrypt.py to this value
    global infilename
    filep = open('filename.temp','w')
    filep.write(str(input_file))
    filep.close()
   
########################################################
