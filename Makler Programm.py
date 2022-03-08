from typing import Concatenate
import Room
checkInput = False

print ("Makler Programm Ver. 1.17.3")
while(checkInput == False):
    roomcount = input ("Wie viele Räume wollen sie anlegen?")
    if(roomcount):
        checkInput = True
    else:
        print("Bitte geben sie etwas ein")
durchlauf = int(0)
multiplikator = int
rooms = []
while (durchlauf < int(roomcount)):
    checkInput = False
    bezeichnung = input ("Wie heisst der Raum?")
    while(checkInput == False):
        teilraume = input ("Wie viele Teilräume hat der Raum? Bitte bedenken sie, dass eine abgeschrägte Decke als Teilraum gilt.")
        if(teilraume):
            checkInput = True
        else:
            print("Bitte geben sie etwas ein")
    teilraum = int(0)
    while (teilraum < int(teilraume)):
        checkInput = False
        while(checkInput == False):
            decke = input ("Wie hoch ist die Decke?")
            if(decke):
                checkInput = True
            else:
                print("Bitte geben sie etwas ein")
        if (int(decke) < 1):
            multiplikator = 0
        elif (int(decke) >= 1 and int(decke) < 2):
            multiplikator = 0.5
        elif (int(decke) >= 2):
            multiplikator = 1
        else:
            print ("Bitte geben sie eine gültige Eingabe")
        if (int(decke) >= 1):
            check = False
            while (check == False):
                frage = input ("Hat der Teilraum 4 Wände? [y/n]")
                if (frage == "y"):
                    wand1 = input ("Bitte geben sie die länge der ersten Wand ein")
                    wand2 = input ("Bitte geben sie die länge einer Wand ein die nicht parallel zur ersten liegt")
                    flaeche = int(wand1) * int(wand2)
                    check = True
                elif (frage == "n"):
                    wand = input ("Bitte geben sie die länge einer Wand ein")
                    tiefe = input ("Bitte geben sie die Distanz zwischen der Wand und der dritten Ecke ein")
                    flaeche = 0,5 * int(wand) * int(tiefe)
                    check = True
                else:
                    print ("Bitte tätigen sie eine gültige Eingabe!")
            gesamtflaeche = flaeche * multiplikator
            raum = Room.room
            raum.bezeichnung = bezeichnung
            raum.flaeche = raum.flaeche + gesamtflaeche
        else:
            print ("Da die Decke niedriger als 1m ist, wird dieser Teilraum nicht als Fläche mitgezählt")
            flaeche = 0
        teilraum = teilraum + 1
    rooms.append(raum)
    print(raum.bezeichnung + " " + str(raum.flaeche) + "m²")
    wohnungFlaeche = wohnungFlaeche + gesamtflaeche
    durchlauf = durchlauf + 1
i = 0
while (i < len(rooms)):
    ausgabe = rooms[i].bezeichnung + " " + str(rooms[i].flaeche) + "m²"
    print (ausgabe)
    i = i + 1
print("Gesamtfläche der Wohnung: " + wohnungFlaeche + "m²")