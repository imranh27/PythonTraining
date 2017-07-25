
#Page 1941 - Sub Classes


class ManagementStaff(Staff):
    def __init__(self, pName, pPay, pAllowance, pBonus):
        super().__init__('Manager', pName, pPay)
        self.allowance = pAllowance
        self.bonus = pBonus

    def calculatePay(self):
        basicPay = super().calculatePay()
        self.pay = basicPay + self.allowance
        return self.pay

    def calculatePerfBonus(self):
        prompt = 'Enter performance grade for {0:s}'.format(self.name)
        grade = input(prompt)
        if grade == 'A':
            self.bonus = 1000
        else:
            self.bonus = 0
        return self.bonus


