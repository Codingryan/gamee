import sys
import time
import random
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
qv = "1+1"
score =0
words = "Welcome to Jabari's world"
thelist = ["green","yellow","blue"]
thecolour = "green"
theoutline = "on_red"
canswer = 0
randomnumber = 0
answer = 0
def AnswerCode(randomnumber):
    if answer == canswer:
        score =+ 1
        PrintBig("correct")
        thedefine + 1 
    else:
        PrintBig("Not correct")
        randomquestion = random.randint(1,12)
    
thedefine = 1

def PrintBig(said):
    cprint(figlet_format(said, font='starwars'),(thecolour), (theoutline), attrs=['bold'], )
     
said = "Welcome to jabari's world"
PrintBig(said)
time.sleep(2)
thecolour = random.choice(thelist)

said =  "what is your name"
PrintBig(said)
time.sleep(1)
thecolour = random.choice(thelist)

Userinput = input("enter here: ")
helloname = "hello "+ Userinput
time.sleep(1)
PrintBig(helloname)
time.sleep(2)
thecolour = random.choice(thelist)

print ("of the three following challenges, which do you find most difficult?")
time.sleep(2)
PrintBig("1- Getting Lost")
time.sleep(2)
thecolour = random.choice(thelist)


PrintBig("2- Losing a toy")
thecolour = random.choice(thelist)

time.sleep(2)
PrintBig("3- Math test")
thecolour = random.choice(thelist)


time.sleep(2)
choice = int(input("Enter coorespodning number here: "))

if choice==1:
    print ("You have chosen 1")
    time.sleep(2)
    print ("...")
    time.sleep(2)
    PrintBig("Let the story begin!")
    thecolour = random.choice(thelist)
    time.sleep(2)
    PrintBig("Paint the picture in your head")
    thecolour = random.choice(thelist)
    
    time.sleep(2)
    
    
if choice==2:
    print ("You have chosen 2!")
    time.sleep(2)
    print ("...")
    time.sleep(2)
    PrintBig("Let the story begin!")
    thecolour = random.choice(thelist)
    
    time.sleep(2)
    PrintBig("Paint the picture in your head")
    thecolour = random.choice(thelist)
    
    time.sleep(2)
    
if choice==3:
    print ("You have chosen 3")
    time.sleep(2)
    print ("...")
    time.sleep(2)
    PrintBig("Let the test begin!")
    time.sleep(2)
    randomquestion = random.randint(1,12)
    if randomquestion == 1:
        canswer = 160
        qv = "80+80="
        thedefine + 1
    if randomquestion == 2:
        canswer = 62
        qv = "2x31="
        thedefine + 1
    if randomquestion == 3:
        canswer = 56
        qv = "8x7="
        thedefine + 1
    if randomquestion == 4:
        canswer = 0
        qv = "47x0="
        thedefine + 1
    if randomquestion == 5:
        canswer = 144
        qv = "12x12="
        thedefine + 1
    if randomquestion == 6:
        canswer = 64
        qv = "8x8="
        thedefine + 1
    if randomquestion == 7:
        canswer = 44
        qv = "11x4="
        thedefine + 1
    if randomquestion == 8:
        canswer = 60
        qv = "20x3="
        thedefine + 1
    if randomquestion == 9:
        canswer = 81
        qv = "9x9="
        thedefine + 1
    if randomquestion == 10:
        canswer = 121
        qv = "11x11="
        thedefine + 1
    if randomquestion == 11:
        canswer = 68
        qv = "17x4="
        thedefine + 1
    if randomquestion == 12:
        canswer = 49
        qv = "7x7="
        thedefine + 1
    PrintBig(qv)
    time.sleep(2)
    answer = int(input ("answer= "))
    AnswerCode(randomnumber)
    randomquestion = random.randint(1,12)
    if randomquestion == 1:
        canswer = 160
        qv = "80+80="
        thedefine + 1
    if randomquestion == 2:
        canswer = 62
        qv = "2x31="
        thedefine + 1
    if randomquestion == 3:
        canswer = 56
        qv = "8x7="
        thedefine + 1
    if randomquestion == 4:
        canswer = 0
        qv = "47x0="
        thedefine + 1
    if randomquestion == 5:
        canswer = 144
        qv = "12x12="
        thedefine + 1
    if randomquestion == 6:
        canswer = 64
        qv = "8x8="
        thedefine + 1
    if randomquestion == 7:
        canswer = 44
        qv = "11x4="
        thedefine + 1
    if randomquestion == 8:
        canswer = 60
        qv = "20x3="
        thedefine + 1
    if randomquestion == 9:
        canswer = 81
        qv = "9x9="
        thedefine + 1
    if randomquestion == 10:
        canswer = 121
        qv = "11x11="
        thedefine + 1
    if randomquestion == 11:
        canswer = 68
        qv = "17x4="
        thedefine + 1
    if randomquestion == 12:
        canswer = 49
        qv = "7x7="
        thedefine + 1
    PrintBig(qv)
    time.sleep(2)
    answer = int(input ("answer= "))
    AnswerCode(randomquestion)
    randomquestion = random.randint(1,12)
    if randomquestion == 1:
        canswer = 160
        qv = "80+80="
        thedefine + 1
    if randomquestion == 2:
        canswer = 62
        qv = "2x31="
        thedefine + 1
    if randomquestion == 3:
        canswer = 56
        qv = "8x7="
        thedefine + 1
    if randomquestion == 4:
        canswer = 0
        qv = "47x0="
        thedefine + 1
    if randomquestion == 5:
        canswer = 144
        qv = "12x12="
        thedefine + 1
    if randomquestion == 6:
        canswer = 64
        qv = "8x8="
        thedefine + 1
    if randomquestion == 7:
        canswer = 44
        qv = "11x4="
        thedefine + 1
    if randomquestion == 8:
        canswer = 60
        qv = "20x3="
        thedefine + 1
    if randomquestion == 9:
        canswer = 81
        qv = "9x9="
        thedefine + 1
    if randomquestion == 10:
        canswer = 121
        qv = "11x11="
        thedefine + 1
    if randomquestion == 11:
        canswer = 68
        qv = "17x4="
        thedefine + 1
    if randomquestion == 12:
        canswer = 49
        qv = "7x7="
        thedefine + 1
    PrintBig(qv)
    time.sleep(2)
    answer = int(input ("answer= "))
    AnswerCode(randomquestion)
    randomquestion = random.randint(1,12)
    if randomquestion == 1:
        canswer = 160
        qv = "80+80="
        thedefine + 1
    if randomquestion == 2:
        canswer = 62
        qv = "2x31="
        thedefine + 1
    if randomquestion == 3:
        canswer = 56
        qv = "8x7="
        thedefine + 1
    if randomquestion == 4:
        canswer = 0
        qv = "47x0="
        thedefine + 1
    if randomquestion == 5:
        canswer = 144
        qv = "12x12="
        thedefine + 1
    if randomquestion == 6:
        canswer = 64
        qv = "8x8="
        thedefine + 1
    if randomquestion == 7:
        canswer = 44
        qv = "11x4="
        thedefine + 1
    if randomquestion == 8:
        canswer = 60
        qv = "20x3="
        thedefine + 1
    if randomquestion == 9:
        canswer = 81
        qv = "9x9="
        thedefine + 1
    if randomquestion == 10:
        canswer = 121
        qv = "11x11="
        thedefine + 1
    if randomquestion == 11:
        canswer = 68
        qv = "17x4="
        thedefine + 1
    if randomquestion == 12:
        canswer = 49
        qv = "7x7="
        thedefine + 1
    PrintBig(qv)
    time.sleep(2)
    answer = int(input ("answer= "))
    AnswerCode(randomquestion)
    randomquestion = random.randint(1,12)
    if randomquestion == 1:
        canswer = 160
        qv = "80+80="
        thedefine + 1
    if randomquestion == 2:
        canswer = 62
        qv = "2x31="
        thedefine + 1
    if randomquestion == 3:
        canswer = 56
        qv = "8x7="
        thedefine + 1
    if randomquestion == 4:
        canswer = 0
        qv = "47x0="
        thedefine + 1
    if randomquestion == 5:
        canswer = 144
        qv = "12x12="
        thedefine + 1
    if randomquestion == 6:
        canswer = 64
        qv = "8x8="
        thedefine + 1
    if randomquestion == 7:
        canswer = 44
        qv = "11x4="
        thedefine + 1
    if randomquestion == 8:
        canswer = 60
        qv = "20x3="
        thedefine + 1
    if randomquestion == 9:
        canswer = 81
        qv = "9x9="
        thedefine + 1
    if randomquestion == 10:
        canswer = 121
        qv = "11x11="
        thedefine + 1
    if randomquestion == 11:
        canswer = 68
        qv = "17x4="
        thedefine + 1
    if randomquestion == 12:
        canswer = 49
        qv = "7x7="
        thedefine + 1
    PrintBig(qv)
    time.sleep(2)
    answer = int(input ("answer= "))
    AnswerCode(randomquestion)
    randomquestion = random.randint(1,12)
    if randomquestion == 1:
        canswer = 160
        qv = "80+80="
        thedefine + 1
    if randomquestion == 2:
        canswer = 62
        qv = "2x31="
        thedefine + 1
    if randomquestion == 3:
        canswer = 56
        qv = "8x7="
        thedefine + 1
    if randomquestion == 4:
        canswer = 0
        qv = "47x0="
        thedefine + 1
    if randomquestion == 5:
        canswer = 144
        qv = "12x12="
        thedefine + 1
    if randomquestion == 6:
        canswer = 64
        qv = "8x8="
        thedefine + 1
    if randomquestion == 7:
        canswer = 44
        qv = "11x4="
        thedefine + 1
    if randomquestion == 8:
        canswer = 60
        qv = "20x3="
        thedefine + 1
    if randomquestion == 9:
        canswer = 81
        qv = "9x9="
        thedefine + 1
    if randomquestion == 10:
        canswer = 121
        qv = "11x11="
        thedefine + 1
    if randomquestion == 11:
        canswer = 68
        qv = "17x4="
        thedefine + 1
    if randomquestion == 12:
        canswer = 49
        qv = "7x7="
        thedefine + 1
    PrintBig(qv)
    time.sleep(2)
    answer = int(input ("answer= "))
    AnswerCode(randomquestion)
    randomquestion = random.randint(1,12)
    if randomquestion == 1:
        canswer = 160
        qv = "80+80="
        thedefine + 1
    if randomquestion == 2:
        canswer = 62
        qv = "2x31="
        thedefine + 1
    if randomquestion == 3:
        canswer = 56
        qv = "8x7="
        thedefine + 1
    if randomquestion == 4:
        canswer = 0
        qv = "47x0="
        thedefine + 1
    if randomquestion == 5:
        canswer = 144
        qv = "12x12="
        thedefine + 1
    if randomquestion == 6:
        canswer = 64
        qv = "8x8="
        thedefine + 1
    if randomquestion == 7:
        canswer = 44
        qv = "11x4="
        thedefine + 1
    if randomquestion == 8:
        canswer = 60
        qv = "20x3="
        thedefine + 1
    if randomquestion == 9:
        canswer = 81
        qv = "9x9="
        thedefine + 1
    if randomquestion == 10:
        canswer = 121
        qv = "11x11="
        thedefine + 1
    if randomquestion == 11:
        canswer = 68
        qv = "17x4="
        thedefine + 1
    if randomquestion == 12:
        canswer = 49
        qv = "7x7="
        thedefine + 1
    PrintBig(qv)
    time.sleep(2)
    answer = int(input ("answer= "))