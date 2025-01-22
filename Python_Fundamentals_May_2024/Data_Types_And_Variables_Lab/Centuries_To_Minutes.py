centuries = int(input())
year = centuries * 100
day = int(year * 365.2422)
hour = day * 24
minute = hour * 60

print(f"{centuries} centuries = {year} years = {day} days = {hour} hours = {minute} minutes")
