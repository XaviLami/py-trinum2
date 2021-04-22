#Trier que les numéros de portable (690) et ne pas faire de doublon, puis re-sortir un fichier csv avec 1 seule colone 

#Lecture des numéros du fichier CSV 
import re
import csv
with open('phones.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        #print(row)        
        rowSum = row[0]+"\n"+row[1]
        print(rowSum)
        matches = re.search("^0590[0-9]*",rowSum)
        if matches  :
                print("Match")      
        else : 
            print("not match")
#Tri des numéros   



