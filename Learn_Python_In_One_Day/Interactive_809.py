

def mainDict():
    age = {'Peter': 5, 'John': 7}

#iterate through Dictionary
    for i in age:
        print(i)

#key and value
    for i in age:
        print("Name = {0:s}, Age = {1:d}".format(i, age[i]))

#key and value alternate
    for i,j in age.items():
        print('Name = {0:s}, Age = {1:d}'.format(i, j))



def main():
    pets = ['cats', 'dogs', 'rabbits', 'hamsters']

#contents of list
    for myPets in pets:
        print(myPets)

#enumerate
    for index, myPets in enumerate(pets):
        print(index, myPets)


if __name__ == '__main__':
    main()
    mainDict()