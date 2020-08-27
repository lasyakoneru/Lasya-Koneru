

 ###########################################################

    #  Computer Project #4

    #

    #  Algorithm

    #    prompt for a file

    #    open a file

    #    read file

    #    find average salary

    #    find median income

    #    find salary range

    #    find cumulative percentage

    #    loop and display data

    ###########################################################
import pylab

def do_plot(x_vals,y_vals,year):
    '''Plot x_vals vs. y_vals where each is a list of numbers of the same length.'''
    pylab.xlabel('Income')
    pylab.ylabel('Cumulative Percent')
    pylab.title("Cumulative Percent for Income in "+str(year))
    pylab.plot(x_vals,y_vals)
    pylab.show()
    
def open_file():
    '''opens the file and returns the year and fp'''
    
    while True:
        year_str = input("Enter a year where 1990 <= year <= 2015: ")
        file = 'year' + year_str + '.txt' # constructs file name
        try:
            fp = open(file, 'r')#opens file
            return fp, year_str
        except FileNotFoundError: # if file not found
            if year_str == '1999':
                print('Error in file name: year' + year_str + '.txt  \
                      Please try again.')
            else:
                print("Error in year. Please try again.")

        
def read_file(fp):
    '''reads the file and constructs a list of the data'''
    L1 = []
    fp.readline()#skips lines
    fp.readline()
    reader = fp.readlines()
    for line in reader: #every individual line in the file
        line = line.split()        
        l = []
        line_0 = line[0].replace(',','') #removes commas
        line_0 = float(line_0)
        try:
            line_2 = line[2].replace(',','')
            line_2 = float(line_2)
            l.append(line_2) #adds to the small list of the line
        except ValueError:
            l.append(None)  
        line_5 = float(line[5])  
        line_6 = line[6].replace(',','')
        line_6 = float(line_6)
        line_7 = line[7].replace(',','')
        line_7 = float(line_7)
        line_3 = line[3].replace(',','')  
        line_3 = int(line_3)
        line_4 = line[4].replace(',','')
        line_4 = int(line_4)
        l.append(line_0)           
        l.append(line_3) 
        l.append(line_4)
        l.append(line_5)
        l.append(line_6)
        l.append(line_7)
        L1.append(l) # adds small list to the big list of all the lines
    return L1 # returns big list
        
def find_average(data_lst):
    '''returns the average salary'''
    numerator = 0 #initialization
    for lst in data_lst: #looks through one list at a time
        numerator += lst[5] # adds all numbers in column
    denominator = data_lst[-1][3] #finds number from last row in column
    average = numerator/denominator 
    return average
    
def find_median(data_lst):
    ''' returns the median income'''
    x = 0
    y = 100
    for lst in data_lst:
        if x < abs(lst[4]) <= 50: #using abs and finding if less than 50
            x = abs(lst[4])
            avg1 = lst[6]
        elif y > abs(lst[4]) >= 50:#using abs and finding if greater than 50
            y = abs(lst[4])
            avg2 = lst[6]
    if (50 - x) > (y - 50): #finding which one is smaller
        avg = avg2#setting to avg
    else:
        avg = avg1
    return avg
    

        
def get_range(data_lst, percent):
    '''returns the salary range as a tuple,the cumulative percentage value, 
        and the average income'''
    percent = float(percent)
    ans = []
    for lst in data_lst:#goes through each list in major list
        if lst[4] >= percent: #checks if greater
            lst2 = []
            col0 = lst[1] #finds column
            lst2.append(col0) #appends to list
            col2 = lst[0]
            lst2.append(col2)
            ans.append(tuple(lst2)) #converts to tuple and appends to list
            col5 = lst[4]
            ans.append(col5)
            col7 = lst[6]
            ans.append(col7)
            break
    return tuple(ans) #converts to a tuple

def get_percent(data_lst,salary):
    '''returns the cumulative percentage in the income range and the 
    income range'''
    salary = float(salary)
    tup = () 
    salary_tup = ()
    for lst in data_lst:#goes through each list in major list
        col0 = lst[1]#finds column
        col2 = lst[0]
        if salary >= col0 and salary <= col2: #chceks if values are in range
            salary_tup = (col0, col2) #creates tuple
            col5 = lst[4]
            tup = (salary_tup, col5) #creates large tuple
    return tup
    

def main():
    fp, year_str = open_file()#opens file
    data_lst = read_file(fp)#reads file
    avg = find_average(data_lst) #finds average
    median = find_median(data_lst) #finds median
    print('Year  Mean           Median         ')
    median = '{:,.2f}'.format(median) #formatting to 2 decimal places
    median = str(median)
    avg = '{:,.2f}'.format(avg)
    avg = str(avg)
    print(year_str+' $'+avg+'          $'+ median) #concatination
    response = input("Do you want to plot values (yes/no)? ")
    if response.lower() == 'yes': # if yes
        x_vals = []
        y_vals = []
        for i in range(40): #through 40 
            income = float(data_lst[i][0])
            cumulative_percent = float(data_lst[i][5])
            x_vals.append(income) # append to list
            y_vals.append(cumulative_percent) # append to list
        do_plot(x_vals,y_vals, year_str) #plot
    
    choice = input("Enter a choice to get (r)ange, (p)ercent,\
                   or nothing to stop: ")
    
    while choice:
        choice = choice.lower() #lowercase
        if choice == '':
            break 
        elif choice == 'r':
            try:
                percent = float(input("Enter a percent: "))
                if (percent >= 0) and (percent <= 100): #if valid print
                    range_num = get_range(data_lst,percent)#call function
                    print("{:>6.2f}% of incomes are below ${:<13,.2f}.".\
                          format(percent,range_num[0][0]))
                else:
                    print('Error in percent. Please try again') #error message
            except ValueError:
                print('Error in percent. Please try again')#error message
        elif choice.lower() == 'p':
            try:
                income = float(input("Enter an income: "))
                if income >= 0:#if valid print
                    percent_num = get_percent(data_lst,income)#call function
                    print("An income of ${:<13,.2f} is in the top {:>6.2f}% \
                          of incomes.".format(income,percent_num[1]))    
                else:
                    print('Error: income must be positive')#error message
            except ValueError:
                print('Error: income must be positive')#error message
        elif choice == '':
            break
        else:
            print('Error in selection.')#error message
        choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing\
                       to stop: ")

if __name__ == "__main__":
    main()