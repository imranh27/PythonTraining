


def dividetwonumbers(number1, number2):

    returnVal = number1 / number2

    return returnVal



def main():
    try:
        userInput1 = int(input('Please enter a number: '))
        userInput2 = int(input('Please enter another number: '))

        answer = dividetwonumbers(userInput1, userInput2)

        print('The answer is {0:f}'.format(answer))

        myFile = open('missing.txt', 'r')

    except ValueError:
        print('Error: you did not enter a number')
    except ZeroDivisionError:
        print('Error: Cannot divide by zero')
    except Exception as e:
        print('Unknown error: ', e)

if __name__ == '__main__':
    main()
