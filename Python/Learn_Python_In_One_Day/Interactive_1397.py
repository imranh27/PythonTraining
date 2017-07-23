

import os


def main():

    inputFile = open('every-house-episode.gif', 'rb')
    outputFile = open('copy_every_house_episode.gif', 'wb')

    msg = inputFile.read()

    outputFile.write(msg)

    os.rename('every-house-episode.gif', 'original.gif')




if __name__ == '__main__':
    main()