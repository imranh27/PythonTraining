

# Chapter 8 - working with files

def readfile():

    f = open("myfile.txt", "r")

    for line in f:
        print(line, end='')

    f.close()

def writefile():

    f = open('myfile.txt', 'a')

    f.write('\nThis sentence will be appended.')
    f.write('\nPython is fun!')

    f.close()

def readandwritebybuffersize():

    inputFile = open('myfile.txt', 'r')
    outputFile = open('myoutputfile.txt', 'w')

    msg = inputFile.read(10)

    while len(msg):
        outputFile.write(msg)
        msg = inputFile.read(10)

    inputFile.close()
    outputFile.close()




def main():

    f = open('myfile.txt', "r")

    firstline = f.readline()
    secondline = f.readline()

    print(firstline)
    print(secondline)

    f.close()

if __name__ == '__main__':
    main()
    writefile()
    readfile()
    readandwritebybuffersize()

