from random import randrange
import time

#deefinitons
def new_screen():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

def loadingbar():
    f   =   str('▓')
    e   =  str('░')

    #n = A   A   B   B   C   C   D   D   E   E   F   F   G   G   H   H   I   I   J   J
    n0 = e + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e
    n1 = f + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e
    n2 = f + f + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e
    n3 = f + f + f + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e
    n4 = f + f + f + f + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e
    n5 = f + f + f + f + f + e + e + e + e + e + e + e + e + e + e + e + e + e + e + e
    n6 = f + f + f + f + f + f + e + e + e + e + e + e + e + e + e + e + e + e + e + e
    n7 = f + f + f + f + f + f + f + e + e + e + e + e + e + e + e + e + e + e + e + e
    n8 = f + f + f + f + f + f + f + f + e + e + e + e + e + e + e + e + e + e + e + e
    n9 = f + f + f + f + f + f + f + f + f + e + e + e + e + e + e + e + e + e + e + e
    #n  = A   A   B   B   C   C   D   D   E   E   F   F   G   G   H   H   I   I   J   J
    n10 = f + f + f + f + f + f + f + f + f + f + e + e + e + e + e + e + e + e + e + e
    n11 = f + f + f + f + f + f + f + f + f + f + f + e + e + e + e + e + e + e + e + e
    n12 = f + f + f + f + f + f + f + f + f + f + f + f + e + e + e + e + e + e + e + e
    n13 = f + f + f + f + f + f + f + f + f + f + f + f + f + e + e + e + e + e + e + e
    n14 = f + f + f + f + f + f + f + f + f + f + f + f + f + f + e + e + e + e + e + e
    n15 = f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + e + e + e + e + e
    n16 = f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + e + e + e + e
    n17 = f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + e + e + e
    n18 = f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + e + e
    n19 = f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + e
    n20 = f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + f + f

    print('                                       Lade...')
    print('                                      ',n0, '   0%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0,4.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n1, '   5%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n2, '   10%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n3, '   15%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n4, '   20%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n5, '   25%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n6, '   30%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n7, '   35%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n8, '   40%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n9, '   45%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n10, '   50%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n11, '   55%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n12, '   60%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n13, '   65%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n14, '   70%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n15, '   75%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n16, '   80%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n17, '   85%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n18, '   90%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n19, '   95%','\n\n\n\n\n\n\n')
    time.sleep(randrange(2.0))
    new_screen()
    print('                                       Lade...')
    print('                                      ',n20, '   100%','\n\n\n\n\n\n\n')
    time.sleep(randrange(4.0))
    new_screen()

def awating_input(query, options, first, second, third, fourth):

    global  option1
    global  option2
    global  option3
    global  option4

    option1 =   first
    option2 =   second
    option3 =   third
    option4 =   fourth

    if options == 1:
        new_screen()
        print('            ', query, '\n\n', '               <>', option1)
    if options == 2:
        new_screen()
        print('            ', query, '\n\n', '               <>', option1, '\n', '               <>', option2)
    if options == 3:
        new_screen()
        print('            ', query, '\n\n', '               <>', option1, '\n', '               <>', option2, '\n','               <>', option3)
    if options == 4:
        new_screen()
        print('            ', query, '\n\n', '               <>', option1, '\n', '               <>', option2, '\n','               <>', option3, '\n','               <>', option4)
    global choice
    choice = input('\n\n\n\n\n\n\n\n\n             >> ')

#textboxes
def textbox(sleep, nametag, line1, line2, line3):

    #nametag adjustments
    raw_count_nametag = len(nametag)
    count_nametag = int(36) - raw_count_nametag
    space_nametag = count_nametag*str('-') + str('+')

    #line1 adjustments
    raw_count_line1 = len(line1)
    count_line1 = int(37) - raw_count_line1
    space_line1 = count_line1*str(' ')

    #line2 adjustments
    raw_count_line2 = len(line2)
    count_line2 = int(37) - raw_count_line2
    space_line2 = count_line2*str(' ')

    #line3 adjustments
    raw_count_line3 = len(line3)
    count_line3 = int(37) - raw_count_line3
    space_line3 = count_line3*str(' ')

    print('              +--',nametag, space_nametag)
    print('              |                                        |')
    print('              |', line1, space_line1, '|')
    print('              |', line2, space_line2, '|')
    print('              |', line3, space_line3, '|')
    print('              |                                        |')
    print('              +----------------------------------------+')

    time.sleep(sleep)
    new_screen()

#dragonfight
def dragonfight(force_match):
    awating_input('Willst du gegen den Drachen kämpfen?', 2, 'Ja', 'Nein', '', '')
    if choice == option1:
        new_screen()
        time.sleep(2)
        print('                                                                             >>>   Bossfight!   <<<\n\n\n\n\n\n\n\n\n')
        time.sleep(3)
        new_screen()
        awating_input('Wähle!', 3, 'Schere','Stein','Drache','')

        #SCHERE
        if choice == 'Schere':
            new_screen()
            print('Der Drache wählt....')
            time.sleep(2)
            new_screen()

            #FORCE VICTORY
            if force_match == 'v':
                print('Du: Schere     Drache: ???\n\n\n\n\n')
                time.sleep(2)
                new_screen()
                print('Du: Schere     Drache: Drache\n\n>>  Gewonnen!  <<\nSchere sticht Drache ab!\n\n')
                input()

            #FORCE DEFEAT
            elif force_match == 'd':
                print('Du: Schere     Drache: ???\n\n\n\n\n')
                time.sleep(2)
                new_screen()
                print('Du: Schere     Drache: Stein\n\n>>  Verloren!  <<\nStein zerstört Schere!\n\n')
                input()

            #FORCE REGULAR MATCH
            elif force_match == 'r':
                dragon_choice = randrange(3)
                if dragon_choice == 1:
                    print('Du: Schere     Drache: ???\n\n\n\n\n')
                    time.sleep(2)
                    new_screen()
                    print('Du: Schere     Drache: Schere\n\n>>  Unentschieden!  <<\nSchere macht nix gegen Schere!\n\n')
                    input()
                elif dragon_choice == 2:
                    print('Du: Schere     Drache: ???\n\n\n\n\n')
                    time.sleep(2)
                    new_screen()
                    print('Du: Schere     Drache: Stein\n\n>>  Verloren!  <<\nStein zerstört Schere!\n\n')
                    input()
                elif dragon_choice == 3:
                    print('Du: Schere     Drache: ???\n\n\n\n\n')
                    time.sleep(2)
                    new_screen()
                    print('Du: Schere     Drache: Drache\n\n>>  Gewonnen!  <<\nSchere sticht Drache ab!\n\n')
                    input()

        #STEIN
        elif choice == 'Stein':
            new_screen()
            print('Der Drache wählt....')
            time.sleep(2)
            new_screen()

            #FORCE VICTORY
            if force_match == 'v':
                print('Du: Stein     Drache: ???\n\n\n\n\n')
                time.sleep(2)
                new_screen()
                print('Du: Stein     Drache: Schere\n\n>>  Gewonnen!  <<\nStein zerschmettert Schere!\n\n')
                input()

            #FORCE DEFEAT
            elif force_match == 'd':
                print('Du: Stein     Drache: ???\n\n\n\n\n')
                time.sleep(2)
                new_screen()
                print('Du: Stein     Drache: Drache\n\n>>  Verloren!  <<\nDrache schluckt Stein, einfach so!\n\n')
                input()

            #FORCE REGULAR MATCH
            elif force_match == 'r':
                dragon_choice = randrange(3)
                if dragon_choice == 1:
                    print('Du: Stein     Drache: ???\n\n\n\n\n')
                    time.sleep(2)
                    new_screen()
                    print('Du: Stein     Drache: Schere\n\n>>  Gewonnen!  <<\nStein zerschmettert Schere!\n\n')
                    input()
                elif dragon_choice == 2:
                    print('Du: Stein     Drache: ???\n\n\n\n\n')
                    time.sleep(2)
                    new_screen()
                    print('Du: Stein     Drache: Stein\n\n>>  Unentschieden!  <<\nStein fällt auf Stein, passiert aber nichts...\n\n')
                    input()
                elif dragon_choice == 3:
                    print('Du: Stein     Drache: ???\n\n\n\n\n')
                    time.sleep(2)
                    new_screen()
                    print('Du: Stein     Drache: Drache\n\n>>  Verloren!  <<\nDrache schluckt Stein, einfach so!\n\n')
                    input()

        #DRACHE
        if choice == 'Drache':
            new_screen()
            print('Der Drache wählt....')
            time.sleep(2)
            new_screen()
            #FORCE VICTORY / DRAW
            if force_match == 'v':
                print('Du: Drache     Drache: ???\n\n\n\n\n')
                time.sleep(2)
                new_screen()
                print('Du: Drache     Drache: Stein\n\n>>  Gewonnen!  <<\nDein Drache isst den Stein, er hatte wohl Appetit!\n\n')
                input()

            #FORCE DEFEAT
            elif force_match == 'd':
                print('Du: Drache     Drache: ???\n\n\n\n\n')
                time.sleep(2)
                new_screen()
                print('Du: Drache     Drache: Schere\n\n>>  Verloren!  <<\nDie Schere besiegt deinen Drachen!\n\n')
                input()

            #FORCE REGULAR MATCH
            elif force_match == 'r':
                dragon_choice = randrange(3)
                if dragon_choice == 1:
                    print('Du: Drache     Drache: ???\n\n\n\n\n')
                    time.sleep(2)
                    new_screen()
                    print('Du: Drache     Drache: Schere\n\n>>  Verloren!  <<\nDie Schere besiegt deinen Drachen!\n\n')
                    input()
                elif dragon_choice == 2:
                    print('Du: Drache     Drache: ???\n\n\n\n\n')
                    time.sleep(2)
                    new_screen()
                    print('Du: Drache     Drache: Stein\n\n>>  Gewonnen!  <<\nDein Drache isst den Stein, er hatte wohl Appetit!\n\n')
                    input()
                elif dragon_choice == 3:
                    print('Du: Drache     Drache: ???\n\n\n\n\n')
                    time.sleep(2)
                    new_screen()
                    print('Du: Drache     Drache: Drache\n\n>>  Unentschieden!  <<\nDrache gegen Drache, da geht nix!\n\n')
                    input()

    elif choice == 'Nein':
        new_screen()
        input('Dann halt nicht! :P')

def event(text):
    print('                                                                                             ',text)
    time.sleep(3)
    new_screen()

##main



#startup
print('/!\\ Wichtige Hinweise /!\\\n\n[1]   Das Spiel ist für 24"-27" Bildschirme im 16:9 Format konzipiert. \n     Damit auch alles glatt läuft, aktiviere bitte den Vollbildmodus. Drücke dazu \"F11\". \n\n[2]   Die aktuelle Version (Pre-Alpha Halloween 2019 //  v.0.2.0) enthält noch sehr viele Bugs und Tippfehler, \n     bitte hab also Verständnis wenn etwas nicht funktioniert und du das Spiel schließen musst.\n\n\nDas Spiel startet in wenigen Sekunden.')
time.sleep(6.5)
new_screen()
loadingbar()
new_screen()
print('                                                                                                                    Stelle dir eine Startmusik vor.')
time.sleep(1.5)

#titlescreen, Art by Korrath
new_screen()
time.sleep(3)
print("                                                                                                      -,,,__                                                 \n                                                                                                       \\    ``~~--,,__                /   /                   \n                                                                                                       /              ``~~--,,_     //--//                   \n                                                                                            _,,,,-----,\\              ,,,,---- >   (c  c)\\                   \n                                                                                        ,;''            `\\\\,,,,----''''   ,,-'''---/   /_ ;___        -,_     \n                                                                                       ( ''---,;====;,----/             (-,,_____/  /'/ `;   '''''----\\ `:.  \n                                                                                       (                 '               `      (oo)/   ;~~~~~~~~~~~~~/--~   \n                                                                                        `;_           ;    \\            ;   \\   `  ' ,,'                     \n                                                                                           ```-----...|     )___________|    )-----'''                       \n                                                                                                       /  /,              `\\   \\\\                            \n                                                                                                     ,'---\\ \\              ,---`,;,                          \n                                                                                                           ```                                               \n\n\n\n\n\n                                                                                                     -<[  Schere  -  Stein  -  Drache  ]>- \n\n\n\n\n\n")
input('                                                                                                             Press \"ENTER\" to continue \n\n')
new_screen()

#introduction
time.sleep(3.5)
textbox(4, 'Unbekannter', 'Hallo!', '','')
textbox(3, 'Unbekannter', 'Ich bin Professor E.!', '', '')
textbox(2.5, 'Professor E.', 'Ich werde dein Begleiter sein.', '', '')
textbox(1.5, 'Professor E.', 'Aber leider bin ich sehr vergesslich.', '', '')
textbox(2.5, 'Professor E.', 'Aber leider bin ich sehr vergesslich.', 'Wie heißt du nochmal?', '')

#playername
new_screen()
print('             Gebe nun deinen Namen ein.')
playername = input('\n\n\n\n\n\n\n\n\n             >> ')
new_screen()
time.sleep(1)
awating_input('Falls du deinen Namen ändern willst, öffne das Programm bitte erneut. \n ''            Um fortzufahren, tippe das folgendes korrekt ab:', 1, 'Verstanden', '', '', '')
if choice == option1:
    new_screen()
    time.sleep(2)
    print('            ', playername,'wird nun dein Name sein.\n\n\n\n\n\n\n\n')
    time.sleep(2.5)
    new_screen()
    #Satzzeichen-Variablen für textbox()
    playername_pkt = playername + str('.')
    playername_kma = playername + str(',')
    playername_frg = playername + str('?')
    playername_aus = playername + str('!')

if choice != option1:
    new_screen()
    input('                     /!\ \n\nOh, damit haben wir wohl nicht gerechnet.\nAber immerhin hast du dieses nette Easter Egg gefunden.\nWenn du weiterspielen willst, musst du das Programm schließen,\n ansonsten könnten ungewollte Bugs entstehen.')
    new_screen()

print('Story beginnt. Hinweis: Dies ist ein Pre-Alpha Build, erwarte also nicht zuviel :^)')
time.sleep(2)
new_screen()

#Story
textbox(3,'Professor E.','Ahh genau,', playername_pkt,'Ach ich bin schon so vergesslich.')
textbox(3,'Professor E.', 'Also...','','')
textbox(3, 'Professor E.','Etwas schlimmes ist passiert...','','')
textbox(3, 'Professor E.','Etwas schlimmes ist passiert...','Tut mir leid, aber...','')
textbox(2,'Professor E.', 'Dein Vater...','','')
textbox(2,'Professor E.', 'Dein Vater...','wurde...','')
textbox(3,'Professor E.', 'Dein Vater...','wurde...','vom großen blauen Drachen entführt.')
textbox(1,'Professor E.','Er ist in der Drachenhöhle','am Ende der Stadt.','')
textbox(3,'Professor E.','Er ist in der Drachenhöhle','am Ende der Stadt.','Keiner kann ihn retten.')
textbox(2,'Professor E.','Außer...','','')
textbox(2,'Professor E.','Außer...','','Du!')
textbox(3, 'Professor E.', 'Du,', playername_kma, 'du kannst ihn retten!')
awating_input('Bist du bereit deinen Vater zu retten?', 2, 'Ja!','Nein!','','')
if choice == option1:
    time.sleep(1)
    new_screen()
    textbox(2,'Professor E.','Ok!','Auf zur Drachenhöhle!','')
    event('Nach 2 Stunden kommst du zusammen mit dem Professor endlich an.')
if choice == option2:
    time.sleep(1)
    new_screen()
    event('/!\\ Hier wurde wohl noch nicht weitergeschieben... Fang doch nochmal von vorne an.')
    input('Bitte schließe das Programm.')
    input('.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    input('..\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
textbox(3,playername,'Oh...','Das ist wohl die Drachenhöhle, von','der mein Vater immer erzählte...')
new_screen()
event('*Drachenbrüllen*')
new_screen()
textbox(1,'Professor E.','Los!','','')
textbox(2,'Professor E.','Los!','Geh rein bevor es zu spät ist!','')
awating_input('Bist du sicher dass du in die gefährliche Drachenhöhle gehen willst?',2,'Ja...?','Nein!?','','')
if choice == option1:
    new_screen()
    event('Du betrittst nun die Höhle, der Professor dicht hinter dir.')
if choice == option2:
    time.sleep(1)
    new_screen()
    event('/!\\ Hier wurde wohl noch nicht weitergeschieben... Fang doch nochmal von vorne an.')
    input('Bitte schließe das Programm.')
    input('.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    input('..\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
textbox(3,'Professor E.','Der Drache scheint dich gar nicht','töten zu wollen!','')
textbox(3,'Professor E.','Aber er wird dir deinen Vater', 'auch nicht so einfach her','wiedergeben.')
input('ENDE')
