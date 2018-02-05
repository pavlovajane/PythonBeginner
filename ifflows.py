name = input("Please, enter your name: ")
age = int(input("How old are you, {0}?".format(name)))

if (age<=30) and (age>=18):
    print("Oh great - know you can go on holiday!")
else:
    if (age<18):
        print("You are too young, please come back in {} year(s)".format(18-age))
    else:
        print("You are too old, sorry!")

