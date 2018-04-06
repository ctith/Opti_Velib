import string

fname = open("C:\\Users\\Fitec\\Desktop\\bikeData\\samples_2018_04_05.sql", "r")
lignes = fname.readlines()

# creation fichier output
out_debut = string.replace('samples_2018_04_05.sql','samples_','')
out_final = string.replace(out_debut,'.sql','')
foutput = open(out_final+".csv","w+")

foutput.write("timestamp,contract_id,station_number,available_bikes,available_bike_stands\n")

for line in lignes :
    line = string.replace(line, 'PRAGMA foreign_keys=OFF;\n','')
    line = string.replace(line, 'BEGIN TRANSACTION;\n','')
    line = string.replace(line, 'CREATE TABLE archived_samples (\n','')
    line = string.replace(line, 'CREATE TABLE "archived_samples" (\n','')
    line = string.replace(line, 'timestamp INTEGER NOT NULL,\n','')
    line = string.replace(line, 'contract_id INTEGER NOT NULL,\n','')
    line = string.replace(line, 'station_number INTEGR NOT NULL,\n','')
    line = string.replace(line, 'available_bikes INTEGER NOT NULL,\n','')
    line = string.replace(line, 'available_bike_stands INTEGER NOT NULL,\n','')
    line = string.replace(line, 'PRIMARY KEY (timestamp, contract_id, station_number)\n','')
    line = string.replace(line, ') WITHOUT ROWID;\n','')
    line = string.replace(line, 'INSERT INTO "archived_samples" VALUES(', '')
    line = string.replace(line,');\n', '')
    line = string.replace(line,'COMMIT;\n', '')
    line = string.replace(line,'\s', '')
    if (line != ''):
        if (line != '\t'):
            if(line !='')
            foutput.write(line+'\n')

fname.close()
foutput.close()