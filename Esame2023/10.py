series = [['1950-02', 126], ['1950-03', 141], ['1950-04', 135], ['1950-05', 125]]
year ='1950'

for item in series:

        try:
            item[0] = item[0].split('-')
        
        except Exception:
            
            continue
    
list_years = [item for item in series if year in item[0]]
print(list_years)

month_list =['01','02','03','04','05','06','07','08','09','10','11','12']

if len(list_years) != 12:
    
    for value in month_list:
        
        missing = 0
        for i in range(len(list_years)):
            
            if value not in list_years[i][0]:
                missing += 1
                
        if missing == len(list_years):
            element = [[year, value], None]
            list_years.append(element)

list_years.sort()
print(' ')
print(list_years)
                
return_list = [item[1] for item in list_years]

print(' ')
print(return_list)
            
#if list == []:
    
    #return None
    

   


