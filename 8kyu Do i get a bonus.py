def bonus_time(salary,bonus):
    return f"${salary}0" if bonus else f"${salary}"

print(bonus_time(2000,True))
print(bonus_time(2000,False))
