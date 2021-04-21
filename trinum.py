
#Trier que les numéros de portable (690) et ne pas faire de doublon, puis re-sortir un fichier csv avec 1 seule colone 

#Lecture des numéros du fichier CSV 
import re
import csv
with open('phones.csv',newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
print(row.count("0590902549;"))     
#result = re.search('^0590[0-9]*',row)
"""
if result  :
    print("Match")      
else : 
    print("not match")
"""
#Tri des numéros 



    
