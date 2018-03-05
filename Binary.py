number = int(input("Please, enter the number between 0 and 65535: "))
remainder = number
result = ""
while remainder>=1:
    division = remainder//2
    remainder_division = remainder%2
    result = result + format(remainder_division)
    remainder = division
# result = result + format(remainder)
if result=="":
    print(0)
else:
    print(result[::-1])