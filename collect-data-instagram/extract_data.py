import pandas
import json
import csv

df = pandas.read_excel('artis-indonesia.xlsx')

values = df['Nama Artis'].values

print(len(values))

with open("/Users/yosuasepria/Desktop/DevOs/collect-data-instagram/" + "nama-artis-indonesia" + '.csv', 'w') as csvfile:
    fieldnames = ['full_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

for i in values:

    if ((len(str(i)) > 1) and (str(i) != "nan")):

        with open("/Users/yosuasepria/Desktop/DevOs/collect-data-instagram/" + "nama-artis-indonesia" + '.csv', 'a') as csvfile:
            fieldnames = ['full_name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'full_name': str(i)})




   
