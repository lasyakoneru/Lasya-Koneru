
    ###########################################################

    #  Computer Project #3

    #

    #  Algorithm

    #    prompt for a file

    #    open a file

    #    find the minimum percent of a line

    #    find the maximum percent of a line

    #    find gdp of specific index and line

    #    loop through file to find lines and call functions

    #    display the data

    ###########################################################

def open_file():
    '''Repeatedly prompt until a valid file name allows the file to be opened.'''
    while True: #when true
        file = input("Enter a file name: ") #user input
        try:
            fp = open(file, "r") #open file
            return fp #return file pointer
        except FileNotFoundError: #if ifile not found
            print("Error. Please try again") #error message
    
def find_min_percent(line):
    '''Find the min percent change in the line; return the value and the index.'''
    min_value = 100000000000 #made to find values below this 
    for x in range(0, 562): #between this number range
        try:
            y = x + 12 #adds 12 to num
            value = line[x:y] #slicing to find val
            value = float(value) #makes float
            if value < min_value: #if val is bellow num set to min val
                #equate to min val to make it the next lowest number
                min_value = value
                index = x + 5 #add 5 to index based off spacing
                x = x + 12 #add 12 to x based off spacing
        except ValueError: #if not a number
            continue #move past it
    return min_value, index #return indexes and minimum number
    
    
def find_max_percent(line):
    '''Find the max percent change in the line; return the value and the index.'''
    max_value = 0 #set max val to low number to find numbers higher than that
    for x in range(0, 562):#between this number range
        try:
            y = x + 12 #adds 12 to num
            value = line[x:y] #slicing to find val
            value = float(value) #makes float
            if value > max_value: #if val is above num set to max val
                #equate to max val to make it the next highest number
                max_value = value 
                index = x + 5 #add 5 to index based off spacing
                x = x + 12 #add 12 to x based off spacing
        except ValueError: #if not a number
            continue #move past it
    return max_value, index #return indexes and maximum number

def find_gdp(line, index):
    '''Use the index fo find the gdp value in the line; return the value'''
    x = index + 12 #add 12 to x based off spacing
    #index to find gdp number in line at given index
    gdp_value = float(line[index:x])
    return gdp_value #return gdp val

        
def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp):
    '''Display values; convert billions to trillions first.'''    
    min_val_gdp = min_val_gdp * 0.001 #convert from billion to trillion
    min_val_gdp = round(min_val_gdp, 2) #round
    max_val_gdp = max_val_gdp * 0.001 #convert from billion to trillion
    max_val_gdp = round(max_val_gdp, 2) #round
    print("Gross Domestic Product") 
    print("min/max     change  year   GDP (trillions)")
    print("min           ", min_val,"  ", min_year,"             ",min_val_gdp)
    print("max           ", max_val,"  ", max_year,"             ",max_val_gdp)

def main():
    fp = open_file() #call open file function
    lines = fp.readlines() #read through lines
    number = 0 #initialize counter
    for line in lines: #go through individual lines
        number += 1 #add 1
        if number == 9: #if 9
            min_val, min_val_index = find_min_percent(line) #call function
            max_val, max_val_index = find_max_percent(line) #call function
            min_year = 1963 + (min_val_index / 12) #calc min year
            min_year = int(min_year) #make int
            max_year = 1963 + (max_val_index / 12) #calc max year
            max_year = int(max_year) #make int
        elif number == 44: #if 44
            min_val_gdp = find_gdp(line, min_val_index) #call function
            max_val_gdp = find_gdp(line, max_val_index) #call function
        else:
            continue 
    #call function
    display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp)
    #return values
    return min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp

# Calls the 'main' function only when you execute within Spyder (or console)
# Do not modify the next two lines.
if __name__ == "__main__":
    main()
