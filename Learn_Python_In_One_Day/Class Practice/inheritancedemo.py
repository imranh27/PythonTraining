
#Page 2072 - Inheritance demo

import Staff

peter = Staff.BasicStaff('Peter', 0)
john = Staff.ManagementStaff('John', 0, 1000, 0)

print(peter)
print(john)

print('Print Peters Pay =', peter.calculatePay())
print('Print Johns Pay =', john.calculatePay())
print('Print Johns Performance Bonus = ', john.calculatePerfBonus())

totalPay = john + peter

print('\nTotal Pay for Both Staff = ', totalPay)