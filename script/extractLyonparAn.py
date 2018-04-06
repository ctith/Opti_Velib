# csv achived_samples
# timestamp,contract_id,station_number,available_bikes,available_bike_stands
# 1449878403,2,2015,3,28

import csv
import string
import os

# liste des fichiers data csv
file_list = open("file_csv_2018.txt", "r")
file_name = file_list.readlines()

# fichier output
foutput = open("data_lyon_2018.csv","w+")
# foutput.write("timestamp,contract_id,station_number,available_bikes,available_bike_stands\n")

# pour chaque fichier csv, recuperer les donnes de lyon dans data_lyon.csv
for file in file_name:

    file = string.replace(file, ' \n','')
    file = string.replace(file, 'samples_','')
    file = string.replace(file, '.sql','.csv')
    print file

    with open("C:\\Users\\Fitec\\IdeaProjects\\velib\\sql\\csv\\"+file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if(row['contract_id']== "14"):

                str = ""+row['timestamp']+","+row['contract_id']+","+row['station_number']+","+row['available_bikes']+","+row['available_bike_stands']
                foutput.write(str+'\n')