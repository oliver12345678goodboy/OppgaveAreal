import os

# Funksjon for å tømme terminalen
def clear():
    os.system('cls')

# Funskjon for å skrive hovedmenyen til skjerm
def skriv_meny():
    print("\nHovedmeny for beregning av areal\n")
    print("1. Beregn areal for kvadrat")
    print("2. Beregn areal for rektangel")
    print("3. Beregn areal for trekant")
    print("4. Beregn areal for parallellogram")
    print("5. Beregn areal for rombe")
    print("6. Beregn areal for trapes")
    print("7. Beregn areal for sirkel")
    print("8. Avslutt")


# Funksjon for å beregne arealet av et kvadrat skrives her. Funsjonen skal ta imot et parameter (s)
# Funksjonen skal returnere arealet
# Utvikler 1 har ansvaret for å lage denne funksjonen

def Kvadrat(s):
    arealkvadrat = s*s
    return arealkvadrat



# Funksjon for å beregne arealet av5 et rektangel skrives her. Funsjonen skal ta imot to parameter (g og h)
# Funksjonen skal returnere arealet
# Utvikler 1 har ansvaret for å lage denne funksjonen

def rektangel(g, h):
    arealrektangel = g*h
    return arealrektangel

# Funksjon for å beregne arealet av en trekant skrives her. Funsjonen skal ta imot to parameter (g og h)
# Funksjonen skal returnere arealet
# Utvikler 1 har ansvaret for å lage denne funksjonen

def trekant(g, h):
    arealtrekant = (g*h)/2
    return arealtrekant

# Funksjon for å beregne arealet av et parallellogram skrives her. Funsjonen skal ta imot to parameter (g og h)
# Funksjonen skal returnere arealet
# Utvikler 1 har ansvaret for å lage denne funksjonen

def parallellogram(g, h):
    arealparallellogram = g * h
    return arealparallellogram


# Funksjon for å beregne arealet av en rombe skrives her. Funsjonen skal ta imot to parameter (g og h)
def arealRombe (h, g):
    areal = g * h
    return areal
# Funksjonen skal returnere arealet
# Utvikler 2 har ansvaret for å lage denne funksjonen


# Funksjon for å beregne arealet av en trapes skrives her. Funsjonen skal ta imot tre parameter (a, b og h)5
def arealTrapes (a, b, h):
    arealTrapes = ((a + b) * h) / 2
    return areal
# Funksjonen skal returnere arealet
# Utvikler 2 har ansvaret for å lage denne funksjonen


# Funksjon for å beregne arealet av en sirkel skrives her. Funsjonen skal ta imot et parameter (r)
def arealSirkel (r):
    areal = 3.14 * r * r
    return areal
# Funksjonen skal returnere arealet
# Utvikler 2 har ansvaret for å lage denne funksjonen

   

# Programmet starter her
ans="Start"
while ans != "8":
    clear()
    skriv_meny()
    
    ans=input("Hva ønsker du å gjøre. Velg tall? ") 
    
    if ans=="1":
        clear()
        print("\nHer bergnes arealet av et kvadrat")
        venter=input("Trykk ENTER for å fortsette!")    
    
    elif ans=="2":
        clear()
        print("\nHer bergnes arealet av et rektangel")
        venter=input("Trykk ENTER for å fortsette!") 
    
    elif ans=="3":
        clear()
        print("\nHer bergnes arealet av en trekant") 
        venter=input("Trykk ENTER for å fortsette!") 
    
    elif ans=="4":
        clear()
        print("\nHer bergnes arealet av et parallellogram")
        venter=input("Trykk ENTER for å fortsette!") 
    
    elif ans=="5":
        clear()

        print("\nHer bergnes arealet av en rombe")
        h = float(input("Skriv inn høyde: "))
        g = float(input("Skriv inn grunnlinje: "))
        areal = arealRombe(h, g)
        print("Arealet av romben er " +  str(areal))

        venter=input("Trykk ENTER for å fortsette!") 
    
    elif ans=="6":
        clear()
        
        print("\nHer bergnes arealet av en trapes")
        a = float(input("Skriv inn lengste siden: "))
        b = float(input("Skriv inn korteste side: "))
        h = float(input("Skriv inn høyden: "))
        areal = arealTrapes(a, b, h)
        print("Arealet av kvadratet er " + str(areal))

        venter=input("Trykk ENTER for å fortsette!")         
    
    elif ans=="7":
        clear()
        print("\nHer bergnes arealet av en sirkel")
        r = float(input("Skriv inn radiusen: "))
        areal = arealSirkel(r)
        print("Arealet av sirkelen er " + str(areal))
        
        venter=input("Trykk ENTER for å fortsette!") 
    
print("\nTakk for at du brukte areal-programmet! Velkommen igjen!\n")          
    
        