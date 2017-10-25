#print payroll Statement

name = input("Enter Employee name : ")
hours = eval(input("Enter number of hours worked this week : "))
pay_rate = eval(input("Enter hourly pay rate : "))
fed_tax_rate = eval(input("Enter Federal Tax withholding rate : "))
state_tax_rate = eval(input("Enter State Tax withholding rate : "))

gross_pay = hours*pay_rate
fed_tax = (fed_tax_rate/100)*gross_pay
state_tax = (state_tax_rate/100)*gross_pay

print("Employee Name :",name)
print("Hours worked : ",hours)
print("Hourly rate : ",pay_rate)
print("Gross pay : $",gross_pay)
print("Deductions :")
print("    Federal Withholding (",fed_tax_rate,"%) : $",round(fed_tax,2))
print("    State withholding (",state_tax_rate,"%) :    $",round(state_tax,2))
print("    Total Deductions :            $",round(fed_tax + state_tax,2))
print("Net Pay : $",round(gross_pay-fed_tax-state_tax,2))