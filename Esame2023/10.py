my_file = open('data.csv', 'r')

my_time_series = [line for line in my_file if not 'date' in line]
print(my_time_series)

for item in my_time_series:
    if not '19' in item:
        continue

