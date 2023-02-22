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
            raise ExamException('errore in apertura del file')
    
        for line in my_file:
            try:
                element = line.split(',')
            except Exception as e:
                print('il valore non è una stringa {}, lo converto a stringa'.format(e))
                try:
                    str(line)
                    element = line.split(',')
                    
                except Exception:
                    print ('questa "line" non è utilizzabile')
                    continue
                
            
            if element[0] != 'date':
                element[-1] = element[-1].strip()
                try:
                    element[-1] = int(element[-1])
                except Exception as e:
                    print('errore in conversione di {}, con questa dicitura {}'.format(element[-1], e))
                    element[-1] = 0

                my_time_series.append(element)
                
        return (my_time_series)

def value_list(series, year):
     
    for item in series:

        try:
            item[0] = item[0].split('-')
        
        except Exception:
            
            continue
    
    list = [item[1] for item in series if year in item[0]]
    
    return list
    

def detect_similar_monthly_variation(time_series, years):
    
    list_years_1 = value_list(time_series, years[0])

    print('{} = {}'.format(years[0],list_years_1))

    list_years_2 = value_list(time_series, years[-1])
    

    print('{} = "{}"'.format(years[1],list_years_2))

    try:
        new_1 = [abs(list_years_1[i] - list_years_1[i+1]) for i in range(len(list_years_1)-1)]
    except Exception as e:
        print('ho quest errore "{}"'.format(e))

    print('new_1 è : {}'.format(new_1))

    new_2 = [abs(list_years_2[i] - list_years_2[i+1]) for i in range(len(list_years_2)-1)]

    print('new_2 è : {}'.format(new_2))

    similar = [-2, -1, 0, 1, 2]
    
    return_list = [True if new_1[i]-new_2[i] in similar else False for i in range(len(new_1))] 
    
    return (return_list)

    

   

        
        
        

    
            
    
    
    
time_series_file = CSVTimeSeriesFile('data.csv')  
series = time_series_file.get_data()
print(series)
years = ['1950','1951']
list = detect_similar_monthly_variation(series, years)
print ('LA LISTA DEFINITIVA E:"{}"'.format(list))




        
    