import time


#deefinitons
def newScreen():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

def loading():
    newScreen()
    print('                                                                                                                    Loading.', '\n', '                                                                                                          +----------------------------+','\n', '                                                                                                          |                            |', '\n', '                                                                                                          +----------------------------+')
    time.sleep(1)
    newScreen()
    print('                                                                                                                     Loading..', '\n', '                                                                                                          +----------------------------+','\n', '                                                                                                          ||||||                       |', '\n', '                                                                                                          +----------------------------+')
    time.sleep(1)
    newScreen()
    print('                                                                                                                     Loading...', '\n', '                                                                                                          +----------------------------+','\n', '                                                                                                          |||||||||||                  |', '\n', '                                                                                                          +----------------------------+')
    time.sleep(1)
    newScreen()
    print('                                                                                                                     Loading.', '\n', '                                                                                                          +----------------------------+','\n', '                                                                                                          ||||||||||||||||             |', '\n', '                                                                                                          +----------------------------+')
    time.sleep(1)
    newScreen()
    print('                                                                                                                     Loading..', '\n', '                                                                                                          +----------------------------+','\n', '                                                                                                          |||||||||||||||||||||        |', '\n', '                                                                                                          +----------------------------+')
    time.sleep(1)
    newScreen()
    print('                                                                                                                     Loading...', '\n', '                                                                                                          +----------------------------+','\n', '                                                                                                          ||||||||||||||||||||||||||   |', '\n', '                                                                                                          +----------------------------+')
    time.sleep(1)
    newScreen()
    print('                                                                                                                     Loading.', '\n', '                                                                                                          +----------------------------+','\n', '                                                                                                          ||||||||||||||||||||||||||||||', '\n', '                                                                                                          +----------------------------+')
    time.sleep(1)


def awatingInput(query, options, first, second, third, fourth):

    global  option1
    global  option2
    global  option3
    global  option4

    option1 =   first
    option2 =   second
    option3 =   third
    option4 =   fourth

    if options == 1:
        newScreen()
        print('            ', query, '\n\n', '               <>', option1)
    if options == 2:
        newScreen()
        print('            ', query, '\n\n', '               <>', option1, '\n', '               <>', option2)
    if options == 3:
        newScreen()
        print('            ', query, '\n\n', '               <>', option1, '\n', '               <>', option2, '               <>', option3)
    if options == 4:
        newScreen()
        print('            ', query, '\n\n', '               <>', option1, '\n', '               <>', option2, '               <>', option3, '               <>', option4)
    global choice
    choice = input('\n\n\n\n\n\n\n\n\n             >> ')

#textboxes
def textbox(sleep, nametag, line1, line2, line3):

    #nametag adjustments
    rawCountNametag = len(nametag)
    CountNametag = int(36) - rawCountNametag
    spaceNametag = CountNametag*str('-') + str('+')

    #line1 adjustments
    rawCountLine1 = len(line1)
    CountLine1 = int(37) - rawCountLine1
    spaceLine1 = CountLine1*str(' ')

    #line2 adjustments
    rawCountLine2 = len(line2)
    CountLine2 = int(37) - rawCountLine2
    spaceLine2 = CountLine2*str(' ')

    #line3 adjustments
    rawCountLine3 = len(line3)
    CountLine3 = int(37) - rawCountLine3
    spaceLine3 = CountLine3*str(' ')

    print('     +--',nametag, spaceNametag)
    print('     |                                        |')
    print('     |', line1, spaceLine1, '|')
    print('     |', line2, spaceLine2, '|')
    print('     |', line3, spaceLine3, '|')
    print('     |                                        |')
    print('     +----------------------------------------+')

    time.sleep(sleep)
    newScreen()

#startup
print( '                                                                                                                    Hinweis: Spiele im Vollbild für die beste Spielerfahrung.')
time.sleep(3.5)
newScreen()
print('                                                                                                                    Stelle dir eine Startmusik vor.')
time.sleep(1.5)

#titlescreen, Art by Korrath
newScreen()
print("                                                                                                      -,,,__                                                 \n                                                                                                       \\    ``~~--,,__                /   /                   \n                                                                                                       /              ``~~--,,_     //--//                   \n                                                                                            _,,,,-----,\\              ,,,,---- >   (c  c)\\                   \n                                                                                        ,;''            `\\\\,,,,----''''   ,,-'''---/   /_ ;___        -,_     \n                                                                                       ( ''---,;====;,----/             (-,,_____/  /'/ `;   '''''----\\ `:.  \n                                                                                       (                 '               `      (oo)/   ;~~~~~~~~~~~~~/--~   \n                                                                                        `;_           ;    \\            ;   \\   `  ' ,,'                     \n                                                                                           ```-----...|     )___________|    )-----'''                       \n                                                                                                       /  /,              `\\   \\\\                            \n                                                                                                     ,'---\\ \\              ,---`,;,                          \n                                                                                                           ```                                               \n\n\n\n\n\n                                                                                                     -<[  Schere  -  Stein  -  Drache  ]>- \n\n\n\n\n\n")
time.sleep(3)
newScreen()
loading()
input('                                                                                                             Press \"ENTER\" to continue \n\n')
newScreen()

#introduction
time.sleep(3.5)
textbox(4, 'Unbekannter', 'Hallo!', '','')
textbox(3, 'Unbekannter', 'Ich bin Professor E.!', '', '')
textbox(2.5, 'Professor E.', 'Ich werde dein Begleiter sein.', '', '')
textbox(1.5, 'Professor E.', 'Aber leider bin ich sehr vergesslich.', '', '')
textbox(2.5, 'Professor E.', 'Aber leider bin ich sehr vergesslich.', 'Wie heißt du nochmal?', '')


#playername
newScreen()
print('             Gebe nun deinen Namen ein.')
playername = input('\n\n\n\n\n\n\n\n\n             >> ')
newScreen()
time.sleep(1)
awatingInput('Falls du deinen Namen ändern willst, öffne das Programm bitte erneut. \n ''            Um fortzufahren, bestätige mit', 1, 'Verstanden', '', '', '')
if choice == option1:
    newScreen()
    time.sleep(2)
    print('            ', playername,'wird nun dein Name sein.\n')
    time.sleep(2.5)
    newScreen()


#story
input()
