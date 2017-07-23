


def main():
    brand = 'Apple'
    price = 1299
    exchangeRate = 1.2345
    #message = 'The price of this is %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR' %(brand, 1299, exchangeRate)

    message = 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR'.format(brand,price,exchangeRate)

    print(message)





if __name__ == '__main__':
    main()
