
#Page 2281

def printInstructions(instruction):
    return print(instruction)


def getUserScore(userName):
    try:
    inputFile = open('userScores.txt', 'r')

    for line in inputFile:
        content = line.rstrip('\n').split(',')
        person = content[0]
        score = int(content[1])

        if userName == person:
            print("The score for {0:s} is {1:d}".format(person, score))
            inputFile.close()
            return '-1'

    except IOError:
    print('The file was not found, so we will create it')
    inputFile = open('userScores.txt', 'w')
    inputFile.close()
    return '-1'

    else:
    inputFile.close()
    return '-1'


def main():
    printInstructions()


if __name__ == '__main__':
    main()