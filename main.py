# input statements
salary = float(input(1250.0))
numDependents = float(input(2))

# calculate taxes here
stateTax = float(salary * 0.065)
federalTax = float(salary * 0.28)
dependentDeduction = float(numDependents * 0.025)
totalWithholding =  float(stateTax + federalTax + dependentDeduction)
takeHomePay = float(salary - totalWithholding)


# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
print(salary)

