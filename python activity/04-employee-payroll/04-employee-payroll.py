name = input("Employee name: ")
basic = float(input("Basic pay: "))
overtime_hours = float(input("Overtime hours: "))
overtime_rate = float(input("Overtime rate per hour: "))
incentive = float(input("Incentive: "))

# Allowances and gross salary
hra = basic * 40 / 100
da = basic * 10 / 100
overtime = overtime_hours * overtime_rate
gross = basic + hra + da + overtime + incentive

# Deductions
pf = basic * 12 / 100
if gross <= 25000:
    tax = 0
elif gross <= 50000:
    tax = (gross - 25000) * 10 / 100
else:
    tax = 25000 * 10 / 100 + (gross - 50000) * 20 / 100
total_deductions = pf + tax
net = gross - total_deductions

# Salary statement
print("\n==============================")
print("        SALARY STATEMENT")
print("==============================")
print(f"Employee name   : {name}")
print("------------------------------")
print("EARNINGS")
print(f"Basic pay       : {basic:10.2f}")
print(f"HRA (40%)       : {hra:10.2f}")
print(f"DA (10%)        : {da:10.2f}")
print(f"Overtime        : {overtime:10.2f}")
print(f"Incentive       : {incentive:10.2f}")
print(f"Gross salary    : {gross:10.2f}")
print("------------------------------")
print("DEDUCTIONS")
print(f"Provident fund  : {pf:10.2f}")
print(f"Income tax      : {tax:10.2f}")
print(f"Total deduction : {total_deductions:10.2f}")
print("------------------------------")
print(f"NET SALARY      : {net:10.2f}")
print("==============================")