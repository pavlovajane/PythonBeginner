# greeting = "Hello"
# name = input("Please enter your name: ")
# print(greeting + ", " + name + "!")
# anotherSplitString = """This string has been split
# over
# several lines"""
# print(anotherSplitString)
#
# print('''The pet owner said "No, no, e's' uh...he's resting"''')

age = 24
print("My age is "+ str(age)+ " years")
print("My age is {0} years".format(age))
print("My age is %d %s, %d %s" % (age, 'years', 6, 'months'))

print('%(language)s has %(number)04d quote types.' % {'language': "Python", "number": 2})

for i in range(1,12):
    print("No. %2d is squared %4d nad cubed is %4d" % (i, i**2, i**3))

print("Pi is approximately {0:12.50f}".format(22/7))