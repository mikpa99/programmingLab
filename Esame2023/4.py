class ExamException(Exception):
    pass

my_list = [['1949-01', 112.0],['1949-02', 118.0],['1949-03', 132.0],['1949-04', 129.0],['1949-05', 121.0],['1949-06', 135.0],['1949-07', 148.0],['1949-08', 148.0],['1949-09', 136.0],['1949-10', 119.0],['1949-11', 104.0],['1949-12', 118.0],['1950-01', 115.0],['1950-02', 126.0],['1950-03', 141.0]
,['1950-04', 135.0]
,['1950-05', 125.0]
,['1950-06', 149.0]
,['1950-07', 170.0]
,['1950-08', 170.0]
,['1950-09', 158.0]
,['1950-10', 133.0]
,['1950-11', 114.0]
,['1950-12', 140.0]
,['1951-01', 145.0]
,['1951-02', 150.0]
,['1951-03', 178.0]
,['1951-04', 163.0]
,['1951-05', 172.0]
,['1951-06', 178.0]
,['1951-07', 199.0]
,['1951-08', 199.0]
,['1951-09', 184.0]
,['1951-10', 162.0]
,['1951-11', 146.0]
,['1951-12', 166.0]
,['1952-01', 171.0]
,['1952-02', 180.0]
,['1952-03', 193.0]
,['1952-04', 181.0]
,['1952-05', 183.0]]

#def detect_similar_monthly_variation(my_list, years):

value_1 = '1949'
#value_2 = years[1]
list_years_1 = []
list_years_2 = []

for item in my_list:
    item[0] = item[0].split('-')
    if value_1 in item[0]:
        list_years_1.append(item[1])


#for item in my_list:
    #if not value_1 in my_list:
        #raise ExamException('anno indicato non presente nella lista')

def value_list(series, year):
    
    for item in series:
        item[0] = item[0].split('-')
        print(series)
        #list = [item for item in series if year in item[0]]
    #return list
    
    


year = '1949'
dates = value_list(my_list, year)
print(dates)

