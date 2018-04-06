# csv achived_samples
# timestamp,contract_id,station_number,available_bikes,available_bike_stands
# 1449878403,2,2015,3,28

import csv
import string
import os

# liste des fichiers data csv
list_file = os.listdir("C:\\Users\\Fitec\\IdeaProjects\\velib\\sql\\csv")
print list_file

# fichier output
foutput = open("data_lyon_extract.csv","w+")
foutput.write("timestamp,contract_id,station_number,available_bikes,available_bike_stands\n")

# pour chaque fichier csv, recuperer les donnes de lyon dans data_lyon.csv
for file in list_file:

    file = string.replace(file, ' \n','')
    print file

    with open("C:\\Users\\Fitec\\IdeaProjects\\velib\\sql\\csv\\"+file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if(row['contract_id']== "14"):

                str = ""+row['timestamp']+","+row['contract_id']+","+row['station_number']+","+row['available_bikes']+","+row['available_bike_stands']
                foutput.write(str+'\n')