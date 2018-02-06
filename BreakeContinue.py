ipAddress = input("Please input some IP address in some 'XXX.XXX.XXX' number/full stops format: ")

if len(ipAddress)==0:
    print("You failed to input something")
else:

    numberSegments = 1
    lengthSegment = 0
    arraySegments = []
    strLength = len(ipAddress)
    lastSegment = 0

    for i in range(0, strLength):

        if ipAddress[i] == '.':
            numberSegments += 1
            arraySegments.append(lengthSegment)
            lengthSegment = 0

        if not ipAddress[i] == '.':
            lengthSegment += 1
            if ipAddress.find('.', i, strLength) == -1 and lastSegment == 0:
                # that's mean it the last segment
                arraySegments.append(strLength - i)
                lastSegment = 1

    arrayString = ','.join(str(e) for e in arraySegments)

    print("Your IP address contains segments {0} and segments with length {1}".format(numberSegments, arrayString))
