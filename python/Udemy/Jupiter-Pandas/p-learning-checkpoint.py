import time
import os
import pandas

csv_path = "C:/progra/WORKSPACE/PYPYPYTHON/temps_today.csv"
count = 0

while count < 10:
    if os.path.exists(csv_path):
        data = pandas.read_csv(csv_path)   
        print(data.mean())
    else:
        print("File does not exist.")
    count += 1
    time.sleep(.1)
print("breaking loop after 10 tries")