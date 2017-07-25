
#Page 2072 - Inheritance demo

import Staff
import BasicStaff
import ManagementStaff

peter = BasicStaff.BasicStaff('Peter', 0)
john = ManagementStaff.ManagementStaff('John', 0, 1000, 0)

print(peter)
print(john)

print('Print Peters Pay =', peter.calculatePay())
print('Print Johns Pay =', john.calculatePay())
print('Print Johns Performance Bonus = ', john.calculatePerfBonus())
