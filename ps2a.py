# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 16:17:59 2021

@author: chung
"""

annual_salary = float(input("Annual Salary: "))
portion_saved = float(input("Portion of Salary Saved: "))
monthly_salary = annual_salary/12
total_cost = float(input("Cost of Dream House: "))


portion_down_payment = 0.25 * total_cost
current_savings = 0
r= 0.04
months = 0
semi_annual_raise = float(input("Semi annual raise: "))

while current_savings < portion_down_payment:
    current_savings += monthly_salary * portion_saved
    current_savings = current_savings * (1 + r/12)
    if months % 6 == 0 and months != 0 :
        monthly_salary = monthly_salary * (1 + semi_annual_raise)
    months += 1

years = months / 12
print(months)
print(years)