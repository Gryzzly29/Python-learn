# myfile = open("fruits.txt")
# content = myfile.read()
# myfile.close

# with open('/fruits.txt') as myfile:
#     content = myfile.read()

# print(content)


with open("vegetables.txt", "w") as myfile:
    myfile.write("Tomato\nCucumber\nOnion") 