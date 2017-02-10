##########################################################################################
# HELP CLASS MODULE
# By Brady Goodwin
# April 2016
#
#
# This module contains the HelpClass. HelpClass creates a window for the help dialog.
# This simple dialog gives the user a brief description of how to use the program. 
##########################################################################################

#---------------------Import Libraries------------------------#
from Tkinter import *
import tkFont
#-------------------------------------------------------------#



#-------------------------Class-------------------------------#

class MessageBox:

#########################################################################################
# Intiation Function
# By Brady Goodwin
# April 2016
#
#
# Initializes the class, and creates the help dialog window.
#
# Arguments required: None
##########################################################################################    
    def __init__(self): # called when the object is created
        self.customFont = tkFont.Font(family="Helvetica", size=12)    
        MasterWindow = Tk() # get the window "frame". 
        Label(MasterWindow, font=self.customFont,text="To use, simply input your zip code where it says 'ENTER YOUR ZIPCODE'").pack() 
             
 
#COULDNT GET THE FOLLOWING WORKING PROPERLY WILL REVISIT                
#########################################################################################
# Help Button Function
# By Brady Goodwin
# April 2016
#
#
# Displays help window
#
# Arguments required: None
##########################################################################################    
      #def HelpButton(self):
        #Label(MasterWindow, font=self.customFont,text="To use, simply input your zip code where it says 'ENTER YOUR ZIPCODE, PUNY HUMAN'").pack()
    
    
