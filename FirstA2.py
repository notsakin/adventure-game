#Autor: Marcel,Joel,Niklas
#Datum: 2.10.19
#Name: FirstA2.py

import random
import time


print('Unbekannter: \n Hallo!')
time.sleep(3)
print('''Unbekannter:
	Ich bin Professor E.!''')
time.sleep(2)
print('''Professor E.:
	Ich bin dein Begleiter!''')
time.sleep(2)
print('''	Aber leider bin ich sehr vergesslich…''')
time.sleep(2)
print('''Professor E.:
	Wie heißt du nochmal? ''')

x = input("Gib deinen Namen ein: ")

print('''Professor E.:
        Ahhhhh stimmt, ''', x,'''.''')
time.sleep(2)
print('''	Ach ich bin schon so alt und vergesslich.''')
time.sleep(2)
print('''Professor E.:
	Also…         ''')
time.sleep(2)
print('''	Etwas schlimmes ist passiert…   ''')
time.sleep(2)
print('''	Es tut mir sehr leid für dich … ''')
time.sleep(2)
print('''Professor E.:
	Dein… ''')
time.sleep(1)
print('''	Vater…''')
time.sleep(1)
print('''	Wurde…''')
time.sleep(1)
print('''	Von dem großem blauen Drachen entführt…''')
time.sleep(2)
print('''*Du bist schockiert!*''')
time.sleep(2)
print('''Professor E.:
	Er ist in der Drachen Höhle am Ende der Stadt… ''')
time.sleep(2)
print('''	Keiner kann ihn retten…''')
time.sleep(2)
print('''Professor E.:
	Außer… ''')
time.sleep(2)
print('''	Dir!''')
time.sleep(1)
print('''	''', x,''', du kannst ihn retten!''')
time.sleep(1)

rettung = input('''Bist du bereit deinen Vater zu retten?(Ja/Nein)''')

if rettung == ("Ja"):
    print("Lange Story beginnt")


elif rettung == ("Nein"):
    print("Jeder würde seinem Vater retten!")
    time.sleep(1)
    wirklichsicher = input("Bist du dir wirklich sicher?(Ja/Nein)")

    if wirklichsicher == ("Ja"):
        ("Noch in die Arbeit")
    elif wirklichsicher == ("Nein"):
        print("Lange Story beginnt")
