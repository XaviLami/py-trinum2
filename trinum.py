#Trier que les numéros de portable (690) et ne pas faire de doublon, puis re-sortir un fichier csv avec 1 seule colonne 
#new_arr = old_ arr
#Trouver un moyen pour stocker les valeurs prises par itération sans les écrasser. 

#Lecture des numéros du fichier CSV 
import re
import csv
from copy import*
with open('phones.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        #print(row)        
        rowSum = row[0]+"\n"+row[1]
        print(row[0])
       
        matchesUn = re.search("0590[0-9]*",row[0])
        matchesDeux = re.search("0590[0-9]*",row[1])

        if matchesUn  :
                print("Match")
                copyList = copy(row[0])  
        else : 
         print("not match")
print("\n"+copyList)
#Tri des numéros   



