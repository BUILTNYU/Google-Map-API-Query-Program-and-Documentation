from random import *
import json
import urllib
import urllib.request
import codecs
import time
import signal

'''
import random
print(random.randint(0,9))
'''

prefixURL = "https://maps.googleapis.com/maps/api/distancematrix/json?"

def handler(signum, frame):
    print ("do nothing")

def read_file(inputFile,m):
    try:
        inFile = open(inputFile,m)
    except:
        print("There's something wrong with printing the file "+inputFile)
        exit(1)
    return inFile

def processAddress(start_location_method,start_location_cor_or_address,location):
    if(start_location_cor_or_address=="cor"):
        location = location.replace(" ","+")
    else:
        location = location.replace(" ","+")
    stringBuilder = ""
    if(start_location_method!="manual"):
        input_file = input("Please enter the absolute/relative path of the file that contains the address/coordinates\n")
        fileIn = read_file(input_file,"r")
        stringBuilder = ""
        for line in fileIn:
            line = line.strip("\n")
            stringBuilder+=line+"|"
        stringBuilder = stringBuilder[:-1]
        location = stringBuilder
        location = location.replace(" ","+")
        #print(location)
    return location
            
def google_map_distance_matrix_api(information,APIkey):
    reader = codecs.getreader("utf-8")
    global prefixURL
    finalURL = prefixURL
    for key,value in information.items():
        if(value!="null"):
            finalURL+=value
    finalURL+=APIkey
    print(finalURL)
    answer = json.load(reader(urllib.request.urlopen(finalURL)))
    print(answer)
    return answer
    

def outputFile (output_fileName,randomNumber,information,key):
    output=read_file(output_fileName,"w")
    if(randomNumber==0):
        answer = google_map_distance_matrix_api(information,key)
        output.write(",")
        for i in range(len(answer["destination_addresses"])):
            clean_dest = answer["destination_addresses"][i].replace(",","/")+","
            output.write(clean_dest)
        output.write("\n")
        for i in range(len(answer["origin_addresses"])):
            clean_origin = (answer["origin_addresses"][i]).replace(",","/")
            output.write(clean_origin)
            output.write(",")
            for j in range(len(answer["rows"][i]["elements"])):
                output.write(str(answer["rows"][i]["elements"][j]["duration_in_traffic"]["value"]))
                output.write(",")
            output.write("\n")
    else:
        origins = information["origins"][8:-1]
        print("i'm origins:"+origins)
        #origins = "origins="+processAddress(start_location_method,start_location_cor_or_address,origins_location)+"&"
        destinations = information["destinations"][13:-1]
        print("i'm destinations:"+destinations)
        origins = origins.split("|")
        destinations = destinations.split("|")
        if(randomNumber>(len(destinations)) or randomNumber>len(origins)):
            print("error, random number is larger than destinations/origins number, program exits")
            exit(1)
        origins_new = []
        destinations_new = []
        for i in range(randomNumber):
            origins_new.append(origins.pop(randint(0,len(origins)-1)))
            destinations_new.append(destinations.pop(randint(0,len(destinations)-1)))
        origins = "origins="
        destinations = "destinations="
        for i in origins_new:
            origins+=i+"|"
        for i in destinations_new:
            destinations+=i+"|"
        origins = origins[:-1]+"&"
        destinations = destinations[:-1]+"&"
        information["origins"] = origins
        information["destinations"] = destinations
        answer = google_map_distance_matrix_api(information,key)
        output.write(",")
        for i in range(len(answer["destination_addresses"])):
            clean_dest = answer["destination_addresses"][i].replace(",","/")+","
            output.write(clean_dest)
        output.write("\n")
        for i in range(len(answer["origin_addresses"])):
            clean_origin = (answer["origin_addresses"][i]).replace(",","/")
            output.write(clean_origin)
            output.write(",")
            for j in range(len(answer["rows"][i]["elements"])):
                output.write(str(answer["rows"][i]["elements"][j]["duration_in_traffic"]["value"]))
                output.write(",")
            output.write("\n")
        
        
            
            
        
        
        
        

        
        
    


def main():
    print('''
    for this program to run, you might need to use pip(3) to install the following libraries
    json
    urllib
    codecs
    time
    signal
    random
    ''')
    print("For the following parameters, some of them are optional, type null when you would like to exclude the parameter in the query")
    #taking in origins and destinations
    print("If you choose manual mode:")
    print("For coordinates, Please separate latitude and longitude by comma and different coordinates by '|'")
    print("For address, Please separate information inside address by '+', between address by '|'")
    print("For example, '257 Gold Street Brooklyn ny 11201|2 Gold Street Manhattan nyc ny' or coordinates'43.6,76.5|43.7,87.9'")
    start_location_method = input("For origins (required): Please indicate whether you would like to use file that contains all location's name or manually enter address(file/manual)\n")
    start_location_cor_or_address = input("For origins (required): Please indicate whether you would like to use coordinates or address(cor/address)\n")
    origins_location = ""
    if(start_location_method=="file"):
        origins_location = "null"
    else:
        origins_location = input("For origins(required): Please input your location\n")
    origins = "origins="+processAddress(start_location_method,start_location_cor_or_address,origins_location)+"&"
    #print (origins)
    
    end_location_method = input("For Destination (required): Please indicate whether you would like to use file that contains all location's name or manually enter address(file/manual)\n")
    end_location_cor_or_address = input("For Destination (required): Please indicate whether you would like to use coordinates or address(cor/address)\n")
    destinations_location = ""
    if(start_location_method=="file"):
        destinations_location = "null"
    else:
        destinations_location = input("For Destination (required), Please input your location\n")
    destinations = "destinations="+processAddress(end_location_method,end_location_cor_or_address,destinations_location)+"&"
    print (destinations)
    print("There are two kinds of units available in for the Google maps system: imperial(feet and miles) or metric(meter and kilometer)")
    units = input("What kind of units would you like to use? (imperial/metric)\n")
    units = "units="+units+"&"
    departure_time = input("Please enter your departure time in second since 1970 (unix time) or you can enter 'now' to indicate you want real time information (An integer/now)\n")
    departure_time_int = True
    try:
        int(departure_time)
    except:
        if(departure_time!="now"):
            print("The input of the departure time is invalid")
            exit(1)
    departure_time = "departure_time="+departure_time+"&"
    mode = input("Please enter the traffic mode that you would like to use to get from origins to destination(driving/walking/bicycling/transit)\n")
    transit_mode = "null"
    if(mode=="transit"):
        print("Please enter 'rail' if you want to use one of tram/subway/train")
        transit_mode = input("Please enter the public transit mode you would like to choose(bus/subway/train/tram/rail)\n")
        transit_mode = "transit_mode="+transit_mode+"&"
    else:
        transit_mode = "null"
    mode = "mode="+mode+"&"
        
    key = input("Please enter your google map api key to continue:\n")
    key = "key="+key
    information = {"origins":origins,"destinations":destinations,"units":units,"departure_time":departure_time,"mode":mode,"transit_mode":transit_mode}
    print("Please contact with Xuebo Lai if you request another language (ex. French)")
    print("Please also contact with Xuebo Lai if you request another to get the distance instead of travel time")
    random = input("Do you want to randomly pick up n address from origins and destinations to generate matrix?(yes/no)\n")
    numberOfRandom = 0
    if(random=="yes"):
        numberOfRandom = int(input("How many random trial would you like?\n"))
    output_fileName = input("Please name the output file")+".csv"
    outputFile(output_fileName,numberOfRandom,information,key)
    
    
    #def outputFile (output_fileName,randomNumber):

    
    
            






if(__name__=="__main__"):
    main()

    
    
    

    
    
    
