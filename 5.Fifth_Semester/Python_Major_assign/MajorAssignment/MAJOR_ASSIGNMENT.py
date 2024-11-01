
#Q1 & Q2: Function to calculate basic salary and overtime salary, and total salary ::::::::::::::::::::::::::::
 #Basic salary case 
def b_s(hourly_rate, hours_worked_per_week):
    return (hourly_rate * hours_worked_per_week) * 4  # Calculate monthly salary

# Overtime case
def o_s(hourly_rate, hours_worked_per_week):
    if hours_worked_per_week > 40:
        overtime_hr = hours_worked_per_week - 40
        return overtime_hr * hourly_rate * 1.5  # Calculate overtime pay
    return 0  # No overtime pay if hours are 40 or less

# Total salary calculation
def t_S(hourly_rate, hours_worked_per_week):
    return b_s(hourly_rate, hours_worked_per_week) + o_s(hourly_rate, hours_worked_per_week)




# Q2 Function to calculate the tax amount based on basic salary ::::::::::::::::::::::::::::::::
def tax_amount(total_salary):
    """Calculate the tax amount based on the salary."""

    if total_salary < 60000:
        return total_salary * 0.10
    elif 60000 <= total_salary <= 85000:
        return total_salary * 0.15
    else:
        return total_salary * 0.20
    

# Q3: Function to calculate the gross salary including allowances and after deducting tax::::::::::::::::::::::::::::
def g_s(hourly_rate, hours_worked_per_week):
    b = b_s(hourly_rate, hours_worked_per_week) 
    t =t_S(hourly_rate, hours_worked_per_week)
    allowances = 0.20 * b
    tax = tax_amount(b)
    return t + allowances - tax


# Q4: Function to determine the salary bracket based on gross salary::::::::::::::::::::::::::::::::::::::::::
def sal_bracket(g):
    if g < 50000:
        return "Low income"
    elif 50000 <= g <= 80000:
        return "Middle income"
    else:
        return "High income"
    

    # Q5: Function to generate a report for multiple employees:::::::::::::::::::
def emp_report():
    n = int(input("Enter number of employees: "))
    print("Employee Report")
    print("-" * 50)
    for _ in range(n):
        name = input("Enter employee name: ")
        hourly_rate = float(input("Enter hourly rate: "))
        hours_worked_per_week = float(input("Enter hours worked per week: "))
        
        b = b_s(hourly_rate, hours_worked_per_week)
        g = g_s(hourly_rate, hours_worked_per_week)
        tax = tax_amount(b)
        bracket = sal_bracket(g)
        
        print(f"Name: {name}")
        print(f"Basic Salary: Rs. {b}")
        print(f"Gross Salary: Rs. {g}")
        print(f"Tax Amount: Rs. {tax}")
        print(f"Salary Bracket: {bracket}")
        print("-" * 50)

# Call the function to generate the report
emp_report()




