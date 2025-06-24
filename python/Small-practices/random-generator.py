import random 

print("Hi!, welcome to this mini 'random' number generator, if you would like a number please tell us so")
correct = False
while not correct:
    respuesta = (input("Do you want another number?(y/n)"))
    numero_alasar = random.randint(1,1000)
    if respuesta == 'y':
        print(numero_alasar)
    elif respuesta == 'n':
        print("Ok, see you later")
        correct = True
    else:
        print("Please input a correct answer(y/n)")

