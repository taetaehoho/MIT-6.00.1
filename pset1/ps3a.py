# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 17:14:48 2021

@author: chung
"""

semi_annual_raise = 0.07
r = 0.04
total_cost = 10**6
down_payment = 0.25 * total_cost
months = 36
annual_salary = float(input("Annual Salary: "))

def total_save(portion_saved):
    total_saved = 0
    monthly_salary = annual_salary/12
    for i in range(1, months + 1):
        if i % 6 == 0:
            monthly_salary = monthly_salary * (1 + semi_annual_raise)
        total_saved += portion_saved * monthly_salary
        total_saved = total_saved * (1+r/12)
    return total_saved

high = 10000
low = 0
steps = 0
portion_saved = (high+low)/20000

while abs(total_save(portion_saved) - down_payment) > 100:
    if total_save(portion_saved) < down_payment:
        low = round(portion_saved * 10000)
    else:
        high = round(portion_saved * 10000)
    if steps > 100:
        print("Not possible")
        break
    portion_saved = (round(high+low))/20000
    steps += 1

print(f"Best savings rate: {portion_saved}")
print(f"Steps in bisection search: {steps}")
    

