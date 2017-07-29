



def main():

    input_file = open('userScores.txt', 'r')

    for line in input_file:
        row = line.rstrip('\n').split(',')
        person = row[0]
        score = int(row[1])
        message = '{0:s} has achieved a score of {1:d}'.format(person, score)
        print(message)

    input_file.close()




if __name__ == '__main__':
    main()