
#Page 1437 Chapter 9 - Object Oriented Programming


class Staff:
    def __init__(self, pPosition, pName, pPay):
        self.position = pPosition
        self.name = pName
        self.pay = pPay
        print('Creating Staff Object')

    def __str__(self):
        return "Position = {0:s}, Name = {1:s}, Pay = {2:d}".format(self.position, self.name, self.pay)

    def calculatePay(self):
        prompt = '\nEnter number of hours worked for {0:s}'.format(self.name)
        hours = input(prompt)

        prompt = 'Enter hourly rate for {0:s}'.format(self.name)
        hourlyRate = input(prompt)

        self.pay = int(hours) * int(hourlyRate)

        return self.pay


