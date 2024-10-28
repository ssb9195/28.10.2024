# 28.10.2024
Piedzīvojums Spoku Mājā
Interaktīva teksta piedzīvojumu spēle, kur spēlētājs izpēta spoku māju, sastopoties ar dažādiem izaicinājumiem un pieņemot lēmumus. Šis projekts ir paredzēts kā uzdevums skolēniem, lai praktizētu while ciklus, if nosacījumus un debugošanas prasmes.

## 📋 Uzdevumi
# 1. Lejupielādē un palaid spēli
Lejupielādē šo projektu un palaid start_game() funkciju, lai iepazītos ar spēles gaitu un identificētu esošās kļūdas un nepilnības.
# 2. Atrisini Kļūdas
Kļūda spēles pārtraukšanā: Spēle turpina darboties pat tad, ja player_alive ir False. Pārliecinies, ka spēle beidzas pareizi, izmantojot end_game() funkciju.
Inventāra funkcionalitāte: Funkcijā basement() ir nepieciešama atslēga, bet spēlē pašlaik nav iespējas to iegūt. Pievieno iespēju spēlētājam atrast atslēgu kādā no istabām.
# 3. Papildini Spēli
Pievieno jaunu funkcionalitāti:
Ļauj spēlētājam jebkurā brīdī ierakstīt “inventārs”, lai apskatītu savus priekšmetus.
Pievieno vairākas istabas vai priekšmetus, kas papildinās spēles interesantumu.
Izveido nejaušu iespēju, ka spoks var parādīties dažādās istabās.
# 4. Izaicinājumi (Papildu punkti)
Karte: Pievieno kartes funkciju, kas parāda, kuras istabas ir pieejamas.
Laika limits: Pievieno laika limitu katrai izvēlei, lai spēle kļūtu intensīvāka.
Dažādi beigu scenāriji: Pievieno vairākus beigu scenārijus, pamatojoties uz spēlētāja savāktajiem priekšmetiem un pieņemtajiem lēmumiem.
## 🔧 Koda Struktūra
python
Copy code
def entrance():  # Spēles sākuma funkcija ar izvēlēm
def foyer():  # Foajē istaba ar izvēlēm
def kitchen():  # Virtuve, kur spēlētājs var atrast nazi
def living_room():  # Dzīvojamā istaba ar nolādētu spoguli
def basement():  # Pagrabs ar iespēju izbēgt, ja spēlētājam ir atslēga
def end_game():  # Spēles beigu funkcija
def start_game():  # Galvenā funkcija, kas sāk spēles while ciklu
## 📌 Kā Iesniegt
Debug un papildini kodu: Novērs visas kļūdas un pievieno jaunas funkcijas, kā norādīts uzdevumos.
Pievieno komentārus: Pievieno komentārus savam kodam, lai skaidrotu izdarītās izmaiņas un papildinājumus.
Augšupielādē repozitorijā: Pievieno savu pabeigto projektu savā GitHub kontā un nosūti saiti, lai iesniegtu uzdevumu.
## 📝 Piezīmes
Debugošana: Sekojiet līdzi, lai spēle pareizi pārtraucas, kad player_alive ir False.
Papildus uzdevumi: Šis projekts ir paredzēts ne tikai kļūdu labošanai, bet arī jaunu ideju un funkcionalitātes pievienošanai.
Veiksmi un radošu darbu pie piedzīvojumu spēles uzlabošanas!

