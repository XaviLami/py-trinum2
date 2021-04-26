#Trier que les numéros de portable (690) et ne pas faire de doublon, puis re-sortir un fichier csv avec 1 seule colonne 
#new_arr = old_ arr (a voir )
#Trouver un moyen pour stocker les valeurs prises par itération sans les écrasser. 
#Faire un tableau a l'exterieure de la boucle et inserer les valeurs a la voler ou Pandas
#Utiliser la fonction 'write' du module csv pour créer mon nouveau csv 

#Lecture des numéros du fichier CSV 

import re
import csv
from copy import*
with open('phones.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    copyList = []
    for row in reader:
        #print(row)        
        rowSum = row[0]+"\n"+row[1]
        #print(row[0])
       
        matchesUn = re.search("0690[0-9]*",row[0])

        
        if matchesUn  :
               # print("Match")  
                copyList.append(row[0])
print(copyList)  



#Tri des numéros   



