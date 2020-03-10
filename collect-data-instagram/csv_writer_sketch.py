import csv

daftar_nama = [
    "jokowi","prabowo","sandiaga"
]

with open('eggs.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for nama in daftar_nama:
        writer.writerow([nama])