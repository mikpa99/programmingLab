class ExamException(Exception):
    pass

class CSVFile():
        
    def get_data(self):
        pass

class CSVTimeSeriesFile(CSVFile):

    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        
        my_time_series = []
        can_read = True
        
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        
        except Exception:
            can_read = False
            
        if not can_read:
            raise ExamException('Errore in apertura del file')
    
        for line in my_file:
           
            element = line.split(',')
            if len(element) < 2:
                    continue
                
            
            if element[0] != 'date' and '19' in element[0]:
               
                element[-1] = element[-1].strip()
                
                try:
                    
                    element[-1] = int(element[-1])
                
                except Exception as e:
                    
                    element[-1] = None

                my_time_series.append(element)
        
        my_list_b = my_time_series[:]
        print(my_list_b)
        
       
        same = True
        ordered_and_not_dulicated_list = True
        
        my_list_b.sort()
        
        for i in range(len(my_time_series)):
            if my_time_series[i] != my_list_b[i]:
                same = False
        print (same)
        
        if not same:
        
            raise ExamException('il file non è ordinato')
            
        resultant_list = []
        
        for item in my_list_b:
            if item not in resultant_list:
                resultant_list.append(item)
                
        if len(my_time_series) != len(resultant_list):
            raise ExamException('il file presenta duplicati')
            

        return (my_time_series)

def value_list(series, year):
     
    for item in series:

        try:
            item[0] = item[0].split('-')
        
        except Exception:
            
            continue
    
    list_years = [item for item in series if year in item[0]]

    if list_years == []:
        
        return None
    print(list_years)
    
    month_list =['01','02','03','04','05','06','07','08','09','10','11','12']
    
    if len(list_years) < 12:
        
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
                
    return return_list
    

def detect_similar_monthly_variation(time_series, years):
    
    list_years_1 = value_list(time_series, years[0])
    

    print('{} = {}'.format(years[0],list_years_1))

    list_years_2 = value_list(time_series, years[1])

    if list_years_1 == None or list_years_2 == None:
        
        raise ExamException('Anno inserito non valido!')
    

    print('{} = "{}"'.format(years[1],list_years_2))

    
    new_1 = []
    for i in range(len(list_years_1)-1):
        if list_years_1[i] != None and list_years_1[i+1] != None:
            e = abs(list_years_1[i] - list_years_1[i+1])
            new_1.append(e)
        else:
            new_1.append(None)

    print(new_1)
    

    new_2 = []
    for i in range(len(list_years_2)-1):
        if list_years_2[i] != None and list_years_2[i+1] != None:
            e = abs(list_years_2[i] - list_years_2[i+1])
            new_2.append(e)
        else:  
            new_2.append(None)
  
    print(new_2)

    similar = [-2, -1, 0, 1, 2]
    
    return_list = [] 
    for i in range(len(new_1)):
        if new_1[i] != None and new_2[i] != None and new_1[i]-new_2[i] in similar: 
            return_list.append(True) 
        else: 
            return_list.append(False) 
    
    return (return_list)

    

   

        
        
        

    
            
    
    
    
time_series_file = CSVTimeSeriesFile('data.csv')  
series = time_series_file.get_data()
print(series)
years = ['1950','1951']
list = detect_similar_monthly_variation(series, years)
print ('LA LISTA DEFINITIVA E:"{}"'.format(list))




        
    