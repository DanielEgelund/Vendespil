import random
import time


grid_vertical = "+----"
grid_horizontal = "|    "

size = 10
char_list = ["A", "B", "C", "D", "E", 
             "F", "G", "H", "I", "J"] * size
grid_numb_list = ["0","1", "2", "3", "4", 
                  "5", "6", "7", "8", "9"] * size
#laver to lister som senere kombineres for at give navnet på positioner
#F.eks. "A2" eller "C6"
positions_liste = []

number_list = []
for i in range(0, 50):
    number_list.append(str(i).zfill(2))
    number_list.append(str(i).zfill(2))

random.shuffle(number_list)
#Laver en liste hvor tallene 0-49 hver indgår 2 gange med tilfældige placeringer

char_pos = 0
for i in range(100):
    positions_liste.append(char_list[char_pos] + grid_numb_list[i])
    if i in (9, 19, 29, 39, 49, 59, 69, 79, 89):
        char_pos += 1

pos_dict = dict(zip(positions_liste, number_list))
#laver et dictionary hvor hver item består af en key(placeringen) og en value(tilfældigt tal 0-49)

#print(pos_dict)

user1_score = 0
user2_score = 0

turn = 1
if turn % 2 == 0:
    print()
#styrer spillers tur

end = time.time() + 120
#sætter en timer på 120 sek
while time.time() < end:


    for i in range(size + 1):
        if i < size:
            print(grid_vertical * size, end = "+ \n")
            print(f"| {positions_liste[i]} " +
            f"| {positions_liste[i + 10]} " +
            f"| {positions_liste[i + 20]} " +
            f"| {positions_liste[i + 30]} " +
            f"| {positions_liste[i + 40]} " +
            f"| {positions_liste[i + 50]} " +
            f"| {positions_liste[i + 60]} " +
            f"| {positions_liste[i + 70]} " +
            f"| {positions_liste[i + 80]} " +
            f"| {positions_liste[i + 90]} " +
            f"|")
#printer grid og placeringer til console
        else:
            print(grid_vertical * (size), end = "+ \n")

    user_in1 = input("Indtast første kort: ")
    user_in2 = input("Indtast andet kort: ")

    index = positions_liste.index(user_in1)
    
    if pos_dict[user_in1] == pos_dict[user_in2]:
        index1 = positions_liste.index(user_in1)
        index2 = positions_liste.index(user_in2)
#Hvis turn var et lige tal var det spiller2 det gættede og omvendt ved ulige tal
        positions_liste[index1] = pos_dict[user_in1]
        positions_liste[index2] = pos_dict[user_in2]
        print(positions_liste[index1], positions_liste[index2])

        if turn % 2 == 0:
            user2_score += 1
        else:
            user1_score += 1

#Brugeren gætter i virkeligheden på 2 keys i vores pos_dict. Hvis valuen af de 2 keys er ens...
#er det ikke længere keyen(placeringen) der vises men i stedet valuen(tal 0-49)

    else:
        print(f"Du fandt {pos_dict[user_in1]} og {pos_dict[user_in2]}. Prøv igen")

    turn += 1
else:
    print("spillet er forbi")
    print(f"Spiller 1 fik {user1_score} point og Spiller 2 fik {user2_score} point")
