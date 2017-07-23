
#Chapter 5 Page 598


def main():
    myName = input('Please enter your name: ')
    myAge = input('What about your Age: ')
    output = 'Hello world\nmy name is {0:s}\nand I am {1:s} years old'

    #print('Hello  world, my name is', myName, 'and I am ', myAge, 'years old.')

    print(output.format(myName, myAge))





if __name__ == '__main__':
    main()
