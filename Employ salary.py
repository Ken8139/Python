employ=[
    ("jojo","manager",10101010.000),
    ("abek","asistant manager",1110101.000),
    ("aden","HR",100000.000),
    ("harish","asistant",101010.000)
]
highest_salary_value=0
employ_with_highest_salary_value=None
for employ in employ:
    employ_name, Dipartment, monthly_salary=employ
    salary_value=12*monthly_salary
    print(f"Employ name:{employ_name},the monthly salary is: {salary_value}")
    if salary_value>highest_salary_value:
         highest_salary_value=salary_value
         employ_with_highest_salary_value=salary_value
print(f"Highest salary value is:{highest_salary_value}")
print(f"employ with highest salary value is: {employ_with_highest_salary_value}")
