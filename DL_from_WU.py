#########################################################################################
# WEATHER UNDERGROUND DATA DOWNLOADER MODULE
# By Brady Goodwin
# April 2016
#
#
# This module contains a function to download and prase data 
#  from the WeatherUnderground webservice
##########################################################################################


#---------------------Import Libraries------------------------#
import urllib2
import json
key = "3f79ec58c4788dbe"  #API key for webservice
#-------------------------------------------------------------#


#------------------------Functions----------------------------#

##############################################################
# DOWNLOADER AND PARSER FUNCTION
# By Brady Goodwin
# April 2016
#
# Downloads WU json file and parses it for pertinent information
#
# Arguments required: Zip Code
##############################################################

def GetZipCodesWeather(zip):
    try:
        url = 'http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/PA/' + zip + '.json'  #URL for webservice. Requires API key and zip
    except: 
        print "error with webservice"
        
    
        #Initiates weather data json for parsing
    TheService = urllib2.urlopen(url)
    json_string = TheService.read()
    parsed_json = json.loads(json_string)  #magic code that makes parsing super easy. Not sure how it works
    
    #The data that we are extracting. Included some extraneous variables for potential future analysis
    city = parsed_json['location']['city']
    state = parsed_json['location']['state']
    latitude = parsed_json['location']['lat']
    longitude = parsed_json['location']['lon']
    precipitation = parsed_json['current_observation']['precip_1hr_metric']    
    weather = parsed_json['current_observation']['weather']
    temp = parsed_json['current_observation']['temperature_string']
    feelslike = parsed_json['current_observation']['feelslike_string']  #Gives what the temp actually "feels like" w/ windchill, etc.
    
    #Code to write json to file. Optional, requires a c:/temp directory
    
    #TheOutPutFile = open("C:/temp/wujson","w")
    #TheOutPutFile.write(json_string)
    #TheOutPutFile.close()        
    
    #The variables that are sent out of the function
    return (city,state,latitude,longitude,precipitation,weather,temp,feelslike)
    #except:
        #print "Error parsing data"
#-------------------------------------------------------------#
    
    
