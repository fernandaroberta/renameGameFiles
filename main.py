import os
import csv


dir = "F:\\其他文6\\"

with open("names.txt") as csv_file:
    files = os.listdir(dir)
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        number = row[0][0:4]
        file = [i for i in files if i.startswith(number)]
        for item in file:
            oldName, ext = os.path.splitext(dir + item)
            newName = dir + row[0]
            try:
                os.rename(oldName + ext, newName + ext)
            except:
                print("Erro " + item)
