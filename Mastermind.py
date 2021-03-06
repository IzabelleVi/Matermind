#Import nodige Modules
from itertools import product
import random
from collections import Counter
import sys

#Mogelijke opties in kleuren

kleuren = ['A', 'B', 'C', 'D', 'E', 'F']

#Status van gestart spel ja/nee
ingame = False

def game_menu():
    #Geeft een klein menu waarin de speler aan kan geven of hij speler 1 of speler 	2 wilt zijn.
    global ingame
    while not ingame:
        print("Welkom, wil je graag speler 1 of speler 2 zijn?")
        spelerskeuze = str(input()).lower()
        if spelerskeuze == '':
            game_menu()
        if spelerskeuze == "speler 1":
            ingame = True
            return (kies_code())

        elif spelerskeuze == "speler 2":
            print("De computer zal een code opstellen, probeer deze te raden.")
            ingame = True
            return (check())
        #Waarschuwing als de speler niet 'speler 1' of 'speler 2' in typt
        else:
            print("Kies tussen speler 1, of speler 2.")
            continue



#Speler is speler 1:
def kies_code():
    #"Via een input kan de speler een code invoeren.
    # Deze moet 4 karakters lang zijn en mag alleen bestaan uit A,B,C,D,E,F.

    while True:
        spelercode = input("Kies een code, 4 karakters lang. Je mag dubbelen gebruiken, kiezen uit A, B, C, D, E, F ").upper()
        computer_algoritme(spelercode)





def computer_algoritme(code):
    "Volgens het algorithme dat word gebruikt in het artikel uit de universiteit van Groningen,"
    "voert de computer een gok uit op basis van de feedback_speler."

    #Lijst met alle mogelijke  opties
    combinatie_list = [''.join(i) for i in product('ABCDEF', repeat=4)]

    #feedback vergelijken aan de overige opties in de lijst, en lengte van de lijst bepalen
    gok = 'ABAB'
    while True:
        feedback = feedback_speler(gok, code)
        combinatie_list = [code for code in combinatie_list if feedback_speler(gok, code) == feedback]
        print(gok)
        print(feedback)
        if len(combinatie_list) == 1:
            print("De code is opgelost, die code die jij bedacht was:" + combinatie_list[0])
            sys.exit(0)

        else:
            gok = combinatie_list[0]
            print (combinatie_list)


#Feedback op de laatste gok van de computer

def feedback_speler(gok, code):
    correct = sum((Counter(code) & Counter(gok)).values())
    feedback1 = sum(x == i for x, i in zip(code, gok))
    return feedback1, correct - feedback1


#Speler is speler 2:
#Computer genereert een random code
def maak_code():
    "Maak een code met 4 letters kiezend uit A,B,C,D,E,F door middel van random"
    "code = "

    computercode = []
    for i in range(4):
        computercode.append(kleuren[random.randint(0, 5)])
    return computercode

#Speler dient een gok in op de code van de computer.
def speler_gok():
    "Vraag input en geef deze een naam, bijv “gok”. Als deze iets anders is dan een 4 karakter lange combinatie van A,B,C,D,E,F geef een foutmelding en vraag een nieuwe input."
    print("Gok een code van 4 karakters lang")
    global spelergok
    spelergok = input("")

    for onderdeel in spelergok:

        if len(spelergok) > 4:
            print("De code moet 4 karakters lang zijn.")
            spelergok = ''

        elif onderdeel not in kleuren:
            print("Je kun alleen kiezen uit A, B, C, D, E, F.")
            spelergok = ''

    return spelergok

#De computer vergelijkt de gok van de speler met de code van de computer
def check():
    "In deze functie vergelijkt de computer de gok met de de gegenereerde code. 	Als deze overeenkomen, feliciteert de computer de speler."
    "break"
    "Als deze niet overeenkomt met de code word feedback_computer aangeroepen."
    if speler_gok() == maak_code():
        print("Gefeliciteerd, je hebt de code goed geraden!")
        sys.exit(0)
    else:
        feedback_computer()

#De computer geeft feedback op de gok van de speler, en laat ze opnieuw gokken.
def feedback_computer():
    "De computer geeft hier feedback op de gokken van de speler, ik ga hiervoor	de techniek gebruiken die ook in het artikel van de universiteit van Groningen 	werd gebruikt."
    "Wanneer een getal wel goed is maar op de verkeerde plek returned hij een [0], wanneer er een getal goed staat en de juiste is returned hij een [X]"
    spelergok = speler_gok()
    code = maak_code()
    correct = sum((Counter(code) & Counter(spelergok)).values())
    feedback2 = sum(x == i for x, i in zip(code, spelergok))
    print( (feedback2, correct - feedback2))
    check()




game_menu()
