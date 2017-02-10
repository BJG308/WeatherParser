#########################################################################################
# GRAPHICAL USER INTERFACE MODULE
# By Brady Goodwin
# April 2016
#
#
# Creates the GUI for the program
# Harvests zipcode from user 
# Displays final result
##########################################################################################


#--------------------Import Libraries-----------------------#
from Tkinter import *
import tkFont
import DL_from_WU
import Decide_Clothing
import OtherBoxesGUI
import MessageBox
MasterWindow = Tk() #creates MasterWindow, where everything will live
#-----------------------------------------------------------#


#-----------------------Functions---------------------------#

##############################################################
# Help Button Function
# By Brady Goodwin
# April 2016
#
# Opens Help Window when Help Button Pushed
#
# Arguments required: none
##############################################################
def HelpButton():
    OtherBoxesGUI.MessageBox()


##############################################################
# Cancel Button Function
# By Brady Goodwin
# April 2016
#
# Closes Main Window when pressed
#
# Arguments required: none
##############################################################
def CancelFunction():
    MasterWindow.destroy()
    
##############################################################
# Show Weather Pressed Function 1
# By Brady Goodwin
# April 2016
#
# Collects data when pressed
# Prepares data for GiveFinalBox function
#
# Arguments required: none
##############################################################
def ShowMeWeatherPressed():
    ZipCode =TheTextEntry.get()                                               # Gathers input from Text Entry Box
    (city,state,                                    
    latitude,longitude,
    precipitation,weather,
    temp,feelslike) = DL_from_WU.GetZipCodesWeather(ZipCode) 
    tempcommand,precipcommand = Decide_Clothing.ClothingParser(feelslike, 
                                                              precipitation)  # Get variables from WU webservice
    city,state = city.upper(),state.upper()                                   # Converts city/ state string to uppercase for shouting effect
    return (city,state,tempcommand,precipcommand,precipitation,feelslike)                             # Return variables


##############################################################
# Show Weather Pressed Function 2
# By Brady Goodwin
# April 2016
#
# Gathers final variables from Show Weather Pressed Function 1
# Passes variables into external window that is displayed to user
#
# Arguments required: none
##############################################################
def GiveFinalBox():
    (city,state,tempcommand,precipcommand,precipitation,feelslike) = ShowMeWeatherPressed()         # Collect variables from Show Weather Pressed Function 1
    MessageBox.AnswerBox(city,state,tempcommand, precipcommand,
                         feelslike,precipitation)              # Pass arguments into message box for display to user
   
#-----------------------------------------------------------#    
    

#-----------------------Fonts-------------------------------#
HeaderFont=tkFont.Font(family="Helvetica", weight=tkFont.BOLD, size=14,)
ItalicFont=tkFont.Font(family= "Helvetica", slant=tkFont.ITALIC, size=8, weight=tkFont.BOLD)
BoldFont=tkFont.Font(family= "Helvetica", weight=tkFont.BOLD, size=9)
ButtonFont=tkFont.Font(family= "Helvetica", size=9)
#-----------------------------------------------------------#  


#----------------------WIDGETS------------------------------#

                  # Header Label #
TheHeader = Label(MasterWindow,text=("Welcome!"
                                     ), font=HeaderFont )               
TheHeader.pack()  

                 # Unit Entry Label #
TheLabel = Label(MasterWindow,text="ENTER YOUR ZIPCODE BELOW",font = BoldFont) 
TheLabel.place(relx=.12, rely=.24) 

                  #Text Entry Box #
TheTextEntry = Entry(MasterWindow)
TheTextEntry.place(relx=.23, rely=.39) 

                  # Action Button #
EnterZipcodeButton=Button(MasterWindow, text= "Tell Me What To Wear",font=ButtonFont,command=GiveFinalBox)
EnterZipcodeButton.place(relx=.22, rely=.57)

                  # Cancel Button #
CancelButton=Button(MasterWindow, text="Cancel", command= CancelFunction, font=ButtonFont)
CancelButton.place(relx=.6, rely=.79)

                   # Help Button #
HelpButton=Button(MasterWindow, text= "Help!", font=ButtonFont, command= HelpButton)
HelpButton.place(relx=.22, rely=.79) 

#-----------------------------------------------------------#  


#-----------------Format Main Waindow-----------------------#
MasterWindow.wm_minsize(220, 130)
MasterWindow.wm_maxsize(1000, 1000)
MasterWindow.mainloop() # Loop main window until the user closes the dialog

#-----------------------------------------------------------# 