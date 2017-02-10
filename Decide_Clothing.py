##########################################################################################
# CLOTHING DECIDER MODULE
# By Brady Goodwin
# April 2016
#
#
# This module contains a function that consists of a series of if/ then statements
#  to make clothing recommendations based on temperature and precipitation values
##########################################################################################

#---------------------Import Libraries------------------------#
import DL_from_WU
#-------------------------------------------------------------#


#------------------------Functions----------------------------#
##############################################################
# CLOTHING DECISION FUNCTION
# By Brady Goodwin
# April 2016
#
# Creates a string telling user what to wear for the day 
#  based on precipitation and temperature in their zipcode.
#
# Arguments required: Feels Like Temperature, Precipitation
##############################################################
def ClothingParser(feelslike,precipitation):

    #Makes the temperature variable a useable float. Is given in unicode string, so some conversions must be done.
    newtemp = feelslike.split() #splits string into list based on whitespaces
    newertemp = newtemp[0]      #select first list item, temperature
    stringtemp = str(newertemp) #convert from unicode to regular string
    newestemp= float(stringtemp)#convert to float
    
    #Same as above, for precipitation
    stringprecip = str(precipitation)
    newestprecip = float(precipitation)
    
    
    #Error check
    tempcommand = "There is an error with the ClothingParser temp function"
    
    #Assigns a string to tempcommand variable based on temperature. This string will be presented to user.
    if newestemp <= -50:
        tempcommand = "IT'S RIDICULOUSLY INSANELY COLD DO NOT UNDER ANY CIRCUMSTANCES LEAVE YOUR IGLOO"
    elif newestemp <= -25:
        tempcommand = "IT'S SERIOUSLY SUPER COLD STAY INSIDE AT ALL COSTS BUT IF YOU HAVE TO GO OUTSIDE WEAR 100 LAYERS OF LONGJOHNS AND YOUR WARMEST COAT"
    elif newestemp <= 0: 
        tempcommand = "IT'S TOO COLD FOR HUMAN BEINGS BUT IF YOU PUT ON LONGJOHNS, THICK WOOL PANTS, SUPER WARM BOOTS, SEVERAL WARM LAYERS OF SHIRTS AND A WINTER COAT YOU MIGHT LIVE"
    elif newestemp <= 20:
        tempcommand = "IT'S TOO COLD FOR REASONABLE PEOPLE BUT IF YOU LIVE IN ALASKA OR MONTANA OR SOMETHING YOU PROBABLY THINK THIS IS FINE. WEAR VERY WARM CLOTHES, LIKE A WARM JACKET AND WOOL SOCKS"
    elif newestemp <= 40:
        tempcommand = "IT'S PRETTY CHILLY OUT THERE. WEAR A WARM COAT, LONG PANTS, AND SHOES WITH WOOL SOCKS"
    elif newestemp <= 60:
        tempcommand = "THIS IS PRETTY NICE TEMPERATE WEATHER. YOU'RE GONNA WANT TO WEAR SOME FLANNEL AND LONG PANTS, AND SOCKS WITH YOUR SANDALS"
    elif newestemp <= 80:
        tempcommand = "IT'S DOWNRIGHT NICE OUTSIDE. SHORTS OR TROUSERS WILL WORK, AND YOU CAN WEAR A LIGHT BUTTON UP OR A TEE."
    elif newestemp <= 100:
        tempcommand = "STARTING TO GET A LITTLE WARM. WEAR SHORTS, A PANAMA HAT, AND SANDALS SANS SOCKS. UNDER NO CIRCUMSTANCES WILL YOU WEAR A SHIRT"
    elif newestemp <= 120:
        tempcommand = "GO IMMEDIATLY TO A LAKE OR A RIVER AND JUMP IN IT. DO NOT LEAVE THIS BODY OF WATER UNTIL THE CRUEL SUN HAS HID ITSELF IN THE SHADOW OF THE NIGHT"
    elif newestemp <= 140:
        tempcommand = "You are dead"
    
    
    #Error check
    precipcommand = "There is an error with the ClothingParser precipitation function"
   
    #Assigns a string to precipcommand variable based on precipitation in past hour. This string will be presented to user.
    #Breaks correspond to standard definitions of no rain, light rain, medium rain, and heavy rain.
    if newestprecip <= 2.53:
        precipcommand = " "
    elif newestprecip <= 2.53:
        precipcommand = ". THERE MIGHT BE LIGHT RAIN BUT YOU CAN TOUGH IT OUT"
    elif newestprecip <= 2.54:
        precipcommand =". IT'S RAINY, BRING YOUR GALOSHES AND UMBRELLA"
    elif newestprecip <= 7.62:
        precipcommand =". IT'S ABSOLUTELY POURING, BRING YOUR CANOE"
    
        
    #Variables extracted from function
    return (tempcommand,precipcommand)

#-------------------------------------------------------------#




