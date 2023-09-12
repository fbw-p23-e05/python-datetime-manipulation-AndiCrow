from datetime import datetime, timedelta
current_datetime = datetime.now()

#Task 1

now_datetime = current_datetime - timedelta(days=15)

result = now_datetime.strftime ('%Y-%m-%d')

print(result)

#Task 2

now_datetime = current_datetime + timedelta(days=7)

result = now_datetime.strftime ('%Y-%m-%d')

print(result)

#Task 3

start = datetime(year=2020, month=1, day=1)

payday = start + timedelta(days=25)

result3 = payday.strftime('%d %B, %Y')

print(f'Hello Friedrich, your rent of 300 € is due on {result3}.')