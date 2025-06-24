import time
import os

while True:
    if os.path.exists("D:/PYPYPYTHON/fruits.txt"):
        with open("D:/PYPYPYTHON/fruits.txt") as file:
            print(file.read())
    else:
         print("File does not exist.")
    time.sleep(1) 