    ###########################################################

    #  Computer Project #5

    #

    #  Algorithm

    #    prompt for a file

    #    open a file

    #    read file and build list of list

    #    build a dictionary from list of list

    #    find max and min values

    #    use the functions to help display the data in a table

    ###########################################################

STATES = ['Alaska', 'Alabama', 'Arizona', 'Arkansas', 'California','Colorado', 
          'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
          'Illinois', 'Indiana', 'Iowa','Kansas', 'Kentucky', 'Louisiana', 
          'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 
          'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
          'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 
          'North Carolina', 'North Dakota', 'Ohio','Oklahoma', 'Oregon', 
          'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
          'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 
          'West Virginia','Wisconsin', 'Wyoming'] 
           #list of states that allow output from

def open_file():
    '''prompt for correct file'''
    while True: #when true
        file = input("Enter a file: ") 
        try:
            fp = open(file, "r", encoding = 'utf-8') #opens and reads file
            return fp 
        except FileNotFoundError: #file not found error
            print("Error. Try again.")
            
def read_file(fp):
    '''This function reads the fp and returns a list of lists of the data'''
    data_list = [] #makes an emoty list
    next(fp, None)#skips header
    for line in fp:#line in file
        i = line.split(",")#splits line
        data_list.append(i)#appends to list
    return data_list# returns list
        
def build_dictionary(data_list):
    '''This function builds a dictionary from the previous list'''
    data_dict = {}#empty dictionary
    for lst in data_list:#list in list of lists
        state = lst[0].replace('2/', '').strip() #strip and remove extra words
        crop = lst[1] #index all variables
        year = lst[4]
        year = int(year)
        value = lst[6].strip()
        if "All GE varieties" not in lst[3]: #only want GE values so check 
            continue
        try: #use try except to convert values to int
            value = int(value)
        except ValueError:
            continue
        if crop not in data_dict.keys(): #if not in the keys
            data_dict[crop] = {} #make dict
        if state in STATES: #make sure state is in STATES list
            if state not in data_dict[crop].keys(): #if so then check in dict
                data_dict[crop][state] = [(year, value)] #add as tuple
            else:
                data_dict[crop][state].append((year, value)) #append as tuple
    return data_dict #return dict

def find_min_val(data_dict):
    '''This function finds the min values and returns year, crop, & state'''
    overall_tup_min = [] #make an empty list
    for crop in data_dict.keys(): #for crop in keys
        for state in data_dict[crop].keys(): #for state inside crop dictionary
            x = 100000 #make maximum value to find nums lower
            for tup in data_dict[crop][state]: #search tup
                if tup[1] < x:#check if value is less than x
                    x = tup[1] #if so replace
                    year = tup[0] 
            total = crop, state, year, x 
            min_tup = tuple(total) #creat tup
            x = 100000 #redefine x
            overall_tup_min.append( min_tup )#append tup to a list
    return sorted(overall_tup_min) #sort and return list of tups

def find_max_val(data_dict):
    '''This function finds the max values and returns year, crop, & state'''
    overall_tup_max = [] #make an empty list
    for crop in data_dict.keys():#for crop in keys
        for state in data_dict[crop].keys():#for state inside crop dictionary
            x = 0#make minimum value to find nums higher
            for tup in data_dict[crop][state]: #search tup
                if tup[1] > x:#check if value is more than x
                    x = tup[1] #if so replace
                    year = tup[0]
            total = crop, state, year, x
            max_tup = tuple(total)#creat tup
            x = 0#redefine x
            overall_tup_max.append( max_tup )#append tup to a list
    return sorted(overall_tup_max)#sort and return list of tups
    
def main():
    '''This function calls the other functions and displays the table'''
    fp = open_file() #call open file
    data_list = read_file(fp) #get data_list from read file
    data_dict = build_dictionary(data_list) #get dict from build dictionary
    overall_tup_min = find_min_val(data_dict) #get mins list of tups
    overall_tup_max = find_max_val(data_dict) #get maxs list of tups
    comparison_crop = '' #make empty string
    for tup_min in overall_tup_min: #search tups in list
        for tup_max in overall_tup_max: #search tups in list
            if tup_max[0] == tup_min[0] and tup_max[1] == tup_min[1]:
                #define all indeces
                crop = tup_max[0] 
                state = tup_max[1]
                min_year = tup_min[2]
                min_value = tup_min[3]
                max_year = tup_max[2]
                max_value = tup_max[3]
        #check if crop has been printed by seeing if comparison crop changed
                if comparison_crop != crop:  
                    #print table with formatting
                    print('Crop:', crop) 
                    print("State               Max Yr  Max   Min Yr  Min   ")
                    comparison_crop = crop
                print("{:<20s}{:<8d}{:<6d}{:<8d}{:<6d}".format(state,max_year\
                                            ,max_value,min_year,min_value))

if __name__ == "__main__":
    main()