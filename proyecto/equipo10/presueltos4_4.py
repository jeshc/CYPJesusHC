PRIMO = []
PRIMO.append(2) 
K = 2
NUM = 3
while K <= 30:
    DIVI = 3
    BAND = True
    while (DIVI <(NUM/2)) and BAND == True:
        if NUM % DIVI ==0:
            BAND = False
            DIVI+= 2
        else:
            DIVI+= 2
    else:
        if BAND == True:
            PRIMO.append(NUM)
            K+= 1
            NUM+=2
        else:
            NUM+=2
else:
    print(PRIMO)
    print("Fin del programa")


