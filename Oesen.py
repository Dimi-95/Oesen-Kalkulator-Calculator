from math import pi 

while True: #repeats the program anew if the user doesn't input the right value
    einZwei = str.upper(input("Wenn Zwei Ösen gemacht werden sollen, gebe 'zwei' ein, wenn nicht dann gebe'eine' ein "))
#-------------------------------------------------------------------------------------------------
    if einZwei == "ZWEI":
        while True: #repeats anew if the user doesn't input a nummber
            try:
                d_leitung = float(input("Gebe den Durchmesser der Leitung ein "))
                break
            except:
                print("Das ist keine Nummer")
        while True:
            try:
                d_schraube = float(input("Gebe den Durchmesser der Schraube ein "))
                break
            except:
                print("Das ist keine Nummer")
        while True:
            try:
                l_leitung = float(input("Gebe die Länge der Leitung ein "))
                break
            except:
                print("Das ist keine Nummer")
        
        res = d_leitung + d_schraube * pi + d_schraube + 1 * 2 + l_leitung + d_schraube * 2 #formula to calculate two OESEN
        print("Die Leitung soll: " + str(res) + "mm lang sein")
        print("")
#-------------------------------------------------------------------------------------------------
    elif einZwei == "EINE":#repeats anew if the user doesn't input a nummber
        while True:
            try:
                d_leitung = float(input("Gebe den Durchmesser der Leitung ein "))
                break
            except:
                print("Das ist keine Nummer")
        while True:
            try:
                d_schraube = float(input("Gebe den Durchmesser der Schraube ein "))
                break
            except:
                print("Das ist keine Nummer")
        while True:
            try:
                l_leitung = float(input("Gebe die Länge der Leitung ein "))
                break
            except:
                print("Das ist keine Nummer")
                
        res = d_leitung + d_schraube * pi + d_schraube + 1 * 2 + l_leitung + d_schraube #formula to calculate one OESEN
        print("Die Leitung soll: " + str(res) + "mm lang sein")
        print("")
    else:
        print("Es wurde nicht richtig eingegeben, bitte versuche es nochmal")
        
    
