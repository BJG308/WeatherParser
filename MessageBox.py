##########################################################################################
# ANSWER BOX MODULE
# By Brady Goodwin
# April 2016
#
#
# Creates the window that displays the final results
##########################################################################################

#---------------------Import Libraries------------------------#
from Tkinter import *
import tkFont
#-------------------------------------------------------------#


#-------------------------Class-------------------------------#

class AnswerBox:

#########################################################################################
# Intiation Function
# By Brady Goodwin
# April 2016
#
#
# Arguments required: None
##########################################################################################   

      def __init__(self,city,state,temp,precip,temp2,precip2):                           # Initiates function and passes in arguments 
            MasterWindow = Tk()                                            # get the window "frame". 
            self.customFont = tkFont.Font(family="Helvetica", size=12)
            Label(MasterWindow, font=self.customFont,  text= ("GREETINGS, I SEE THAT YOU ARE IN " + city + ", " + state + ". \n " +
                                                              "THE TEMPERATURE CURRENTLY FEELS LIKE " + temp2 + " AND THERE HAS BEEN " +
                                                              precip2 + " MILLIMETERS OF PRECIPITATION IN THE PAST HOUR. \n"
                                                              + temp + "\n" +  precip)).pack() # Displays the actual final message


          

