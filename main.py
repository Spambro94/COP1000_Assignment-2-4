# input statements
salary = float(input(1250.0))
numDependents = float(input(2))
stateTax = float(input(0.065))
federalTax = float(input(0.28))
dependentsDeduction = float(input(0.025))
totalWithheld = float(input(stateTax + federalTax + dependentsDeduction))
takeHomePay = float(input(salary - totalWithheld))



# calculate taxes here
stateTax = salary * .065
federalTax = salary * .28
dependentsDeduction = numDependents * .025
totalWithheld = stateTax + federalTax + dependentsDeduction
takeHomePay = salary - totalWithheld

# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))