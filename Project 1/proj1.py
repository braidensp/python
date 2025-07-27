salary = int(input("Enter your salary: "))
hours = 40
weeks = 52

print("Your annual salary is: ", salary)

hourly_wage = salary / hours / weeks
print("Your hourly wage is: ", hourly_wage)

bonus_rate = int(input("Enter your bonus rate (as a percentage): "))
bonus = (bonus_rate / 100) * salary
print("Your bonus is: ", bonus)

total_compensation = salary + bonus
print("Your total compensation including bonus is: ", total_compensation)
print("Your total compensation per hour is: ", total_compensation / (hours * weeks))
print("Thank you for using the salary calculator!")
