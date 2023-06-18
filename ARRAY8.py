import pygame, os, sys, time

#colours - pear pallete
white = (255,255,235)
pink = (255, 157, 151)

#pd
#pdpath = "c:\users\haln\desktop\coding\pd\bin\"

#text logic states
logAnd = True
logOr = False
logNot = False

#sequencer stuff
seqX = 100
waitTime = 1
seqStep = 0

activeBeat = 0
beats = 8
noteOn = False
beatChanged = True

#timing stuff
timer = pygame.time.Clock()
fps = 60
bpm = 120
activeLength = 0
beatLength = 3600/bpm

#arrays
array1 = [0,0,0,0,0,0,0,1]
array2 = [0,0,1,0,0,0,0,1]
arrayOut = [0,0,0,0,0,0,0,0]

# Initialize pygame
pygame.init()

def mouseProcess():
    global logAnd, logOr, logNot
    #check the mouse position when clicked for collisions with images and text
    
    # array 1 buttons
    if (event.pos[0] > 100 and event.pos[0] < 133) and (event.pos[1] > 200 and event.pos[1]<233):
                array2[0] = (array2[0]+1)%2
                
    if (event.pos[0] > 150 and event.pos[0] < 183) and (event.pos[1] > 200 and event.pos[1]<233):
                array2[1] = (array2[1]+1)%2
    
    if (event.pos[0] > 200 and event.pos[0] < 233) and (event.pos[1] > 200 and event.pos[1]<233):
                array2[2] = (array2[2]+1)%2
                
    if (event.pos[0] > 250 and event.pos[0] < 283) and (event.pos[1] > 200 and event.pos[1]<233):
                array2[3] = (array2[3]+1)%2
                
    if (event.pos[0] > 300 and event.pos[0] < 333) and (event.pos[1] > 200 and event.pos[1]<233):
                array2[4] = (array2[4]+1)%2
                
    if (event.pos[0] > 350 and event.pos[0] < 383) and (event.pos[1] > 200 and event.pos[1]<233):
                array2[5] = (array2[5]+1)%2
                
    if (event.pos[0] > 400 and event.pos[0] < 453) and (event.pos[1] > 200 and event.pos[1]<233):
                array2[6] = (array2[6]+1)%2
                
    if (event.pos[0] > 450 and event.pos[0] < 483) and (event.pos[1] > 200 and event.pos[1]<233):
                array2[7] = (array2[7]+1)%2
                
    # array 2 buttons
    if (event.pos[0] > 100 and event.pos[0] < 133) and (event.pos[1] > 100 and event.pos[1]<133):
                array1[0] = (array1[0]+1)%2
                
    if (event.pos[0] > 150 and event.pos[0] < 183) and (event.pos[1] > 100 and event.pos[1]<133):
                array1[1] = (array1[1]+1)%2
    
    if (event.pos[0] > 200 and event.pos[0] < 233) and (event.pos[1] > 100 and event.pos[1]<133):
                array1[2] = (array1[2]+1)%2
                
    if (event.pos[0] > 250 and event.pos[0] < 283) and (event.pos[1] > 100 and event.pos[1]<133):
                array1[3] = (array1[3]+1)%2
                
    if (event.pos[0] > 300 and event.pos[0] < 333) and (event.pos[1] > 100 and event.pos[1]<133):
                array1[4] = (array1[4]+1)%2
                
    if (event.pos[0] > 350 and event.pos[0] < 383) and (event.pos[1] > 100 and event.pos[1]<133):
                array1[5] = (array1[5]+1)%2
                
    if (event.pos[0] > 400 and event.pos[0] < 453) and (event.pos[1] > 100 and event.pos[1]<133):
                array1[6] = (array1[6]+1)%2
                
    if (event.pos[0] > 450 and event.pos[0] < 483) and (event.pos[1] > 100 and event.pos[1]<133):
                array1[7] = (array1[7]+1)%2
                
    # text buttons
    if (event.pos[0] > 600 and event.pos[0] < 660) and (event.pos[1] > 100 and event.pos[1]<133):
                logAnd= True
                logOr= False
                logNot= False
                print("and " + str(logAnd) )
                print("and " + str(logOr) )
                print("and " + str(logNot))
                arrayOutLogic()
                    
                
    if (event.pos[0] > 600 and event.pos[0] < 660) and (event.pos[1] > 150 and event.pos[1]<183):
                logAnd= False
                logOr= True
                logNot= False
                print("or " + str(logAnd) )
                print("or " + str(logOr) )
                print("or " + str(logNot))
                arrayOutLogic()
                
    if (event.pos[0] > 600 and event.pos[0] < 660) and (event.pos[1] > 200 and event.pos[1]<233):
                logAnd= False
                logOr= False
                logNot= True
                print("not " + str(logAnd) )
                print("not " + str(logOr) )
                print("not " + str(logNot))
                arrayOutLogic()
                
def array1Graphics():
    if array1[0] == 0:
        screen.blit(bigBubble0,(100,100))
    else:
        screen.blit(bigBubble1,(100,100))
        
    if array1[1] == 0:
        screen.blit(bigBubble0,(150,100))
    else:
        screen.blit(bigBubble1,(150,100))
        
    if array1[2] == 0:
        screen.blit(bigBubble0,(200,100))
    else:
        screen.blit(bigBubble1,(200,100))
        
    if array1[3] == 0:
        screen.blit(bigBubble0,(250,100))
    else:
        screen.blit(bigBubble1,(250,100))

    if array1[4] == 0:
        screen.blit(bigBubble0,(300,100))
    else:
        screen.blit(bigBubble1,(300,100))
        
    if array1[5] == 0:
        screen.blit(bigBubble0,(350,100))
    else:
        screen.blit(bigBubble1,(350,100))
        
    if array1[6] == 0:
        screen.blit(bigBubble0,(400,100))
    else:
        screen.blit(bigBubble1,(400,100))
        
    if array1[7] == 0:
        screen.blit(bigBubble0,(450,100))
    else:
        screen.blit(bigBubble1,(450,100))
        
def array2Graphics():
    if array2[0] == 0:
        screen.blit(bigBubble0,(100,200))
    else:
        screen.blit(bigBubble1,(100,200))
        
    if array2[1] == 0:
        screen.blit(bigBubble0,(150,200))
    else:
        screen.blit(bigBubble1,(150,200))
        
    if array2[2] == 0:
        screen.blit(bigBubble0,(200,200))
    else:
        screen.blit(bigBubble1,(200,200))
        
    if array2[3] == 0:
        screen.blit(bigBubble0,(250,200))
    else:
        screen.blit(bigBubble1,(250,200))

    if array2[4] == 0:
        screen.blit(bigBubble0,(300,200))
    else:
        screen.blit(bigBubble1,(300,200))
        
    if array2[5] == 0:
        screen.blit(bigBubble0,(350,200))
    else:
        screen.blit(bigBubble1,(350,200))
        
    if array2[6] == 0:
        screen.blit(bigBubble0,(400,200))
    else:
        screen.blit(bigBubble1,(400,200))
        
    if array2[7] == 0:
        screen.blit(bigBubble0,(450,200))
    else:
        screen.blit(bigBubble1,(450,200))

def drawArrow():
    if logAnd == True:
        screen.blit(bigArrow,(660,95))
    if logOr == True:
            screen.blit(bigArrow,(660,145))
    if logNot == True:
        screen.blit(bigArrow,(660,195))

def arrayOutGraphics():
    if arrayOut[0] == 0:
        screen.blit(bigOutOff,(100,300))
    else:
        screen.blit(bigOutOn,(100,300))
        
    if arrayOut[1] == 0:
        screen.blit(bigOutOff,(150,300))
    else:
        screen.blit(bigOutOn,(150,300))
        
    if arrayOut[2] == 0:
        screen.blit(bigOutOff,(200,300))
    else:
        screen.blit(bigOutOn,(200,300))
        
    if arrayOut[3] == 0:
        screen.blit(bigOutOff,(250,300))
    else:
        screen.blit(bigOutOn,(250,300))

    if arrayOut[4] == 0:
        screen.blit(bigOutOff,(300,300))
    else:
        screen.blit(bigOutOn,(300,300))
        
    if arrayOut[5] == 0:
        screen.blit(bigOutOff,(350,300))
    else:
        screen.blit(bigOutOn,(350,300))
        
    if arrayOut[6] == 0:
        screen.blit(bigOutOff,(400,300))
    else:
        screen.blit(bigOutOn,(400,300))
        
    if arrayOut[7] == 0:
        screen.blit(bigOutOff,(450,300))
    else:
        screen.blit(bigOutOn,(450,300))

def sequencer():
    global seqX
    global beatLength
    global activeLength
    global seqStep
    global arrayOut
    global beatChanged
    global activeBeat
    global noteOn

    screen.blit(bigSeq,(seqX,350))
    
    if activeLength < beatLength:
            activeLength += 1
    else:
        activeLength = 0
        seqX += 50
        
        #seqStep += 1
        if seqStep < 8 - 1:
                
                seqStep += 1
                beatChanged = True
                
                
        else:
                
                seqStep = 0
                beatChanged = True
                
               
    
    if seqX > 450:
        seqX = 100
    if seqStep > 7:
        seqStep = 0
        
    
            
def playNote():
    print("Note")
    message = "bang"
    os.system("echo " + message +"|" + "c:\\users\\haln\\desktop\\coding\\pd\\bin\\" + "pdsend 7000 127.0.0.1 udp")
        
    
    

def arrayOutLogic():
    if logAnd == True:
        for i in range(len(arrayOut)):
            if array1[i] == 1 and array2[i] == 1:
                arrayOut[i] = 1
            else: arrayOut[i] = 0
    
    if logOr == True:
        for i in range(len(arrayOut)):
            if array1[i] == 1 or array2[i] == 1:
                arrayOut[i] = 1
            else: arrayOut[i] = 0
    
    if logNot == True:
        for i in range(len(arrayOut)):
            if array1[i] == 0 and array2[i] == 0:
                arrayOut[i] = 1
            else: arrayOut[i] = 0
    
# Set the height and width of the screen
size = [700, 400]
screen = pygame.display.set_mode(size)


#window caption & icon & font
pygame.display.set_caption("Array8")
pygame_icon = pygame.image.load('images/b1.png')
pygame.display.set_icon(pygame_icon)
font1 = pygame.font.Font('fonts/pixel_4x4.ttf', 24)

andL = font1.render('and', True, white)
orL = font1.render('or', True, white)
notL = font1.render('not', True, white)
timer.tick(fps)
#load images
bubble0 = pygame.image.load('images/b0.png').convert_alpha()
bigBubble0 = pygame.transform.scale(bubble0, (32,32))

bubble1 = pygame.image.load('images/b1.png').convert_alpha()
bigBubble1 = pygame.transform.scale(bubble1, (32,32))

bubbleOn = pygame.image.load('images/b2.png').convert_alpha()
bigBubbleOn = pygame.transform.scale(bubbleOn, (32,32))

bubbleOff = pygame.image.load('images/b3.png').convert_alpha()
bigBubbleOff = pygame.transform.scale(bubbleOff, (32,32))

arrow = pygame.image.load('images/arrow.png').convert_alpha()
bigArrow = pygame.transform.scale(arrow, (32,32))

outOn = pygame.image.load('images/b2.png').convert_alpha()
bigOutOn = pygame.transform.scale(outOn, (32,32))

outOff = pygame.image.load('images/b3.png').convert_alpha()
bigOutOff = pygame.transform.scale(outOff, (32,32))

seq = pygame.image.load('images/seq.png').convert_alpha()
bigSeq = pygame.transform.scale(seq, (32,32))


# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

while not done:
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    
    
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseProcess()

    # Clear the screen and set the screen background
    screen.fill((39,39,54))
    
    title = font1.render('Array8', True, (255,255,235))
    screen.blit(title,(20,20))
    # text buttons
    screen.blit(andL,(600,100))
    screen.blit(orL,(600,150))
    screen.blit(notL,(600,200))
    
    
    timer.tick(fps)
    #Run Graphics Processes
    array1Graphics()
    array2Graphics()
    drawArrow()
    arrayOutGraphics()
    arrayOutLogic()
    #threading.Thread(target = sequencer).start()
    sequencer()
    
    if arrayOut[seqStep] == 1 and beatChanged == True:
        playNote()
        beatChanged = False
        
    
    pygame.draw.line(screen, (255,255,235), [575, 20], [575, 380], 2)
    
    pygame.display.flip()
    
# Be IDLE friendly
pygame.quit()