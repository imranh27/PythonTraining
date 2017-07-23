# while loops
'''
this is a comment
'''

def breakwhile_continue():

    j = 0

    for i in range(5):
        j = j + 2

        print('\n i = {0:d}, j = {1:d}'.format(i, j))
        if j == 6:
            continue
        print('I will be skipped over if j = 6')



def breakwhile():

    j = 0

    for i in range(5):
        j = j + 2

        print('i = {0:d}, j = {1:d}'.format(i, j))

        if j == 6:
            break


def main():
    counter = 5

    while counter > 0:
        print('Counter = {0:d}'.format(counter))
        counter = counter - 1


if __name__ == '__main__':
    main()
    breakwhile()
    breakwhile_continue()
