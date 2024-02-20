def money (deposit, tax, years, monthly_income):
    money = deposit
    for year in range(years): 
        money+= 12 * monthly_income
        money+= money / 100 * tax
    return money 
print (str(int(money(50000, 20, 12, 1500))))