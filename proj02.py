###########################################################

    #  Computer Project #2

    #

    #  Algorithm

    #    prompt for purchase price and dollars paid

    #    iuser inputs data

    #    while loop

    #       counts number of coins that goes into the amount

    #       output how many coins in stock

    #       goes again and again until user hits q

    #       exits loop

    ###########################################################

# purchase price and payment will be kept in cents
quarters = 10 #initializing all the coins to 10 in the stock
dimes = 10
nickels = 10
pennies = 10


print("Welcome to change-making program.")
print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))
purchase_price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
while purchase_price != 'q': #when not quit

    purchase_price = float(purchase_price) #making float
   
    if purchase_price < 0: #if purchase price less than 0
        print('Error: purchase price must be non-negative.') #no negative number message
#        purchase_price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
   
    else:
        dollars_paid = input('Input dollars paid (int):') #ask for input
        dollars_paid = float(dollars_paid) #float
       
        if dollars_paid < purchase_price: #if dollars paid less than purchase price
            print('\nError: insufficient payment.')
            dollars_paid = input('Input dollars paid (int): ') #ask again
            dollars_paid = float(dollars_paid)
       
        change = dollars_paid - purchase_price #caclualte change
        change = int(round(change * 100)) #convert to cents
        if change == 0:
            print('\nNo change.') #error message
           
        else:
            q = change // 25 #floor division 
            if q > quarters:  #if  q greater
                q = quarters
                quarters = 0 
                change = change - (q * 25) #calculate change
                if quarters < 0:
                    print('\nError: ran out of coins.') # no coins
                    break
            elif q <= quarters: # q less than or equal to quarters
                change = change - (q * 25) #calculate change
                quarters -= q #subtracts quarters from q
                if quarters < 0:
                    print('\nError: ran out of coins.') #error message
                    break
               
            d = change // 10#floor division 
            if d > dimes:#if  d greater
                d = dimes
                dimes  = 0
                change = change - (d * 10) #calculate change
                if dimes < 0:
                    print('\nError: ran out of coins.')#error message
                    break
            elif d <= dimes:# d less than or equal to dimes
                change = change - (d * 10) #calculate change
                dimes -= d#subtracts quarters from d
                if dimes < 0:
                    print('\nError: ran out of coins.')#error message
                    break
                   
            n = change // 5#floor division 
            if n > nickels:#if  n greater
                n = nickels
                nickels = 0
                change = change - (n * 5) #calculate change
                print('\nError: ran out of coins.')#error message
                break
            elif n <= nickels:# n less than or equal to nickels
                change = change - (n * 5) #calculate change
                nickels -= n#subtracts quarters from n
                if nickels < 0:
                    print('\nError: ran out of coins.')#error message
                    break
                
            p = change
            if p > pennies:#if  p greater
                p = pennies
                pennies = 0
                change = change - p #calculate change
                if pennies < 0:
                    print('\nError: ran out of coins.')#error message
                    break
            elif p <= pennies:# p less than or equal to pennies
                change = change - p #calculate change
                pennies -= p#subtracts quarters from p
                if pennies < 0:
                    print('\nError: ran out of coins.')#error message
                    break
                           
   
            print('\nCollect change below: ') #prints the amount of q, d, n, p
            if int(q) != 0:
                print('Quarters: ' + str(int(q)))
            if int(d) != 0:
                print('Dimes: ' + str(int(d)))
            if int(n) != 0:
                print('Nickels: ' + str(int(n)))
            if int(p) != 0:
                print('Pennies: ' + str(int(p)))
               
               
    quarters = int(quarters) #makes integers
    nickels = int(nickels)
    dimes = int(dimes)
    pennies = int(pennies)
   
    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))
   


    purchase_price = input("Enter the purchase price (xx.xx) or 'q' to quit: ") #asks again
    
                
           

   
           