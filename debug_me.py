# Piedzīvojums Spoku Mājā
import random

# Inicializē mainīgos
inventory = []
player_alive = True

# Funkcija, kas parāda inventāru
def show_inventory():
    if inventory:
        print("Tavs inventārs: ",",".join(inventory))

# Definē funkciju, kas sāk spēli un vada ciklu, kamēr spēlētājs ir dzīvs
def start_game():
    while player_alive:
        entrance()

def entrance():
    print("Tu atrodies spoku mājas ieejā. Vai vēlies iet 'iekšā' vai bēgt 'prom'?")
    choice = ""
    while choice not in ["iekšā", "prom"]:
        choice = input(">>> ").lower()
        if choice == "iekšā":
            foyer()
        elif choice == "prom":
            print("Tu izbēdzi droši. Spēle beigusies!")
            end_game()
        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")

def foyer():
    print("Tu ieej foajē. Ir tumšs, bet redzi durvis uz 'virtuvi' un 'dzīvojamo istabu'.")
    choice = ""
    while choice not in ["virtuve", "dzīvojamā istaba"]:
        choice = input(">>> ").lower()
        if choice == "virtuve":
            kitchen()
        elif choice == "dzīvojamā istaba":
            living_room()
        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")

def kitchen():
    print("Tu esi virtuvē. Tā ir biedējoša, un tu atrod rūsinātu nazi un kerambits. Vai tu 'ņem nazis', 'ņem kerambits' vai atstāj 'aizvērtu'?")
    choice = ""
    while choice not in ["ņem nazis", "ņem kerambits", "aizvērtu"]:
        choice = input(">>> ").lower()
        if choice == "ņem nazis":
            nus()       
        if choice == "ņem kerambits":
            inventory.append("kerambits")
            print("Tu paņēmi kerambitu.")
        print("Pēkšņi parādās spoks! Vai tu vēlies 'cīnīties' vai 'bēgt'?")
        action = input(">>> ").lower()
        if action == "cīnīties":
            if "kerambits" in inventory:
                print("Tu uzvarēji spoku ar kerambitu! Tu atgriezies foajē.")
                foyer()
            else:
                print("Tev nav ar ko aizstāvēties. Spēle beigusies.")
                end_game()
        elif action == "bēgt":
            print("Tu aizbēdzi atpakaļ uz foajē.")
            foyer()
        else:
            print("Nepareiza izvēle.")

def living_room():
    print("Dzīvojamā istaba ir putekļaina un tajā ir dīvains spogulis, arī ir lielgabals. Vai tu vēlies 'skatīties' spogulī, 'ņem lielgabalu' vai iet 'atpakaļ'?")
    choice = ""
    while choice not in ["skatīties", "ņem lielgabalu", "atpakaļ"]:
        choice = input(">>> ").lower()
        if choice == "skatīties":
            print("Spogulis ir nolādēts! Tu pārvērties par spoku. Spēle beigusies.")
            end_game()
        if choice == "ņem lielgabalu":
            inventory.append("lielgabals")
            print("Tu paņēmi lielgabalu.")
        print("Spogulis ir nolādēts! Tu pārvērties par spoku. Vai tu vēlies 'nošaujiet sevi' vai 'neko nedarīt'?")
        action = input(">>> ").lower()
        if action == "nošaujiet sevi":
            if "lielgabals" in inventory:
                print("Tu nošāva sevi! Spēle beigusies.")
                end_game()
        if action == "neko nedarīt":
            if "lielgabals" in inventory:
                print("Tu pārvērties par spoku. Spēle beigusies.")
                end_game()
        elif choice == "atpakaļ":
            foyer()
        else:
            print("Nepareiza izvēle.")

def basement():
    print("Tu atrodi durvis uz pagrabu. Tās ir aizslēgtas. Ja tev būtu atslēga, tu varētu tās 'atvērt'.")
    choice = ""
    while choice != "atvērt":
        choice = input(">>> ").lower()
        if choice == "atvērt":
            if "atslēga" in inventory:
                print("Tu atvēri durvis un izbēgi no spoku mājas! Tu uzvari!")
                end_game()
            else:
                print("Durvis ir aizslēgtas. Tev nepieciešama atslēga.")
                basement()
        else:
            print("Nepareiza izvēle.")
            foyer()

def nus():
    inventory.append("nazis")
    print("Tu paņēmi nazi.")
    print("Pēkšņi parādās spoks! Vai tu vēlies 'cīnīties' vai 'bēgt'?")
    action = input(">>> ").lower()
    if action == "cīnīties":
            if "nazis" in inventory:
                print("Tu uzvarēji spoku ar nazi! No spoka izkrita atslēga. Vai tu vēlies 'ņem atslēgu' vai 'atgriezies foajē'?")
            else:
                print("Tev nav ar ko aizstāvēties. Spēle beigusies.")
                end_game
                choice = ""
                while choice not in ["ņem atslēgu", "atgriezies foajē"]:
                    choice = input(">>>").lower()
                    if choice == "ņem atslēgu":
                     gnus

def gnus():
    inventory.append("atslēga")
    print("Tu paņēmi atslēgu.")
    print("Priekšā ir ieeja. Vai vēlies 'iet ieejā' vai 'atgriezies foajē'?")
    choice = ""
    while choice not in ["iet ieejā", "atgriezies foajē"]:
       choice = input(">>> ").lower()
       if choice == "iet ieejā":
        basement()
       elif choice == "atgriezies foajē":
        foyer()

def end_game():
    global player_alive
    player_alive = False
    print("Paldies, ka spēlēji Piedzīvojums Spoku Mājā!")

# Sāk spēli
print("Sveicināts Piedzīvojums Spoku Mājā!")
start_game()
