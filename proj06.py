    ###########################################################

    #  Computer Project #6

    #

    #  Algorithm

    #    deals two cards to each person

    #    deals 5 community cards

    #    goes through each poker function

    #    checks to see which player wins with the higher function

    #    outputs the winner and their cards

    #    prompts to play again until there arent enough cards reamining

    ###########################################################
import cards

def less_than(c1,c2):
    '''Return 
           True if c1 is smaller in rank, 
           True if ranks are equal and c1 has a 'smaller' suit
           False otherwise'''
    if c1.rank() < c2.rank():
        return True
    elif c1.rank() == c2.rank() and c1.suit() < c2.suit():
        return True
    return False
    
def min_in_list(L):
    '''Return the index of the mininmum card in L'''
    min_card = L[0]  # first card
    min_index = 0
    for i,c in enumerate(L):
        if less_than(c,min_card):  # found a smaller card, c
            min_card = c
            min_index = i
    return min_index
        
def cannonical(H):
    ''' Selection Sort: find smallest and swap with first in H,
        then find second smallest (smallest of rest) and swap with second in H,
        and so on...'''
    for i,c in enumerate(H):
        # get smallest of rest; +i to account for indexing within slice
        min_index = min_in_list(H[i:]) + i 
        H[i], H[min_index] = H[min_index], c  # swap
    return H

def flush_7(H):
    '''Return a list of 5 cards forming a flush,
       if at least 5 of 7 cards form a flush in H, a list of 7 cards,
       False otherwise.'''
    list1 = [] # create 4 empty lists
    list2 = []
    list3 = []
    list4 = []
    for i in range(0,len(H)): #going through length of list
        if H[i].suit() == 1: #comparing to suit
            list1.append(H[i]) # appending to list
        elif H[i].suit() == 2:
            list2.append(H[i])
        elif H[i].suit() == 3:
            list3.append(H[i])
        elif H[i].suit() == 4:
            list4.append(H[i])
    if len(list1) > 5: # if the list is over 5
        return list1[:-1] #remove last index
    if len(list1) == 5: #list must be 5
        return list1 #contains all cards that have the same suit
    elif len(list2) == 5:
        return list2
    elif len(list3) == 5:
        return list3
    elif len(list4) == 5:
        return list4
    else: # if not
        return False #returns false

def straight_7(H):
    '''Return a list of 5 cards forming a straight,
       if at least 5 of 7 cards form a straight in H, a list of 7 cards, 
       False otherwise.'''
    list1 = [] #creates an empty list
    H1 = cannonical(H) #uses the organized list
    for c in H1: #checks through cards in list
        rank = c.rank() #calculates rank
        list1.append((rank,c)) #appends rank wand card 
    list2 = [] #makes empty list
    x = 0 #initializes variable
    for i in list1: #checks for i in list
        x += 1 #increments x by 1
        if len(list2) == 5: #checks to see if list length is 5
            return list2 #returns list
            break #breaks
        elif (i[0] + 1) == list1[x][0]: #if equal
            list2.append(i[1]) #append index 1 to second list
        else: #if not
            return False #return false
      
def straight_flush_7(H):
    '''Return a list of 5 cards forming a straight flush,
       if at least 5 of 7 cards form a straight flush in H, a list of 7 cards, 
       False otherwise.'''
    list1 = [] #creates an empty list
    H1 = cannonical(H) #uses the organized list
    for c in H1: #checks through cards in list
        rank = c.rank() #calculates rank
        list1.append((rank,c)) #appends rank wand card 
    list2 = [] #makes empty list
    x = 0 #initializes variable
    for i in list1: #checks for i in list
        x += 1 #increments x by 1
        if len(list2) == 5: #checks to see if list length is 5
            return list2 #returns list
            break #breaks
        elif (i[0] + 1) == list1[x][0]: #if equal
            list2.append(i[1]) #append index 1 to second list
        else: #if not
            return False #return false
    else: 
        list2 = flush_7(list1) #call flush function to check for same suit too
        if list2 == False: #if false
            return False #return False
        else:
            return list2 #return built list

def four_7(H):
    '''Return a list of 4 cards with the same rank,
       if 4 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.'''
    list1 = cannonical(H) #gets organized list
    lst1 = [] #creates 13 empty lists for all ranks
    lst2 = []
    lst3 = []
    lst4 = []
    lst5 = []
    lst6 = []
    lst7 = []
    lst8 = []
    lst9 = []
    lst10 = []
    lst11 = []
    lst12 = []
    lst13 = []
    for i in range(0,len(list1)): #goes through length of organized list
        if list1[i].rank() == 1: #goes through each rank to find matching ones 
            lst1.append(list1[i]) #then appends to list
        elif list1[i].rank() == 2:
            lst2.append(list1[i])
        elif list1[i].rank() == 3:
            lst3.append(list1[i])
        elif list1[i].rank() == 4:
            lst4.append(list1[i])
        elif list1[i].rank() == 5:
            lst5.append(list1[i])
        elif list1[i].rank() == 6:
            lst6.append(list1[i])
        elif list1[i].rank() == 7:
            lst7.append(list1[i])
        elif list1[i].rank() == 8:
            lst8.append(list1[i])
        elif list1[i].rank() == 9:
            lst9.append(list1[i])
        elif list1[i].rank() == 10:
            lst10.append(list1[i])
        elif list1[i].rank() == 11:
            lst11.append(list1[i])
        elif list1[i].rank() == 12:
            lst12.append(list1[i])
        elif list1[i].rank() == 13:
            lst13.append(list1[i])
    if len(lst1) == 4: #checks to see which list has 4 matching ranks in it
        return lst1 #returns that list
    elif len(lst2) == 4:
        return lst2
    elif len(lst3) == 4:
        return lst3
    elif len(lst4) == 4:
        return lst4
    elif len(lst5) == 4:
        return lst5
    elif len(lst6) == 4:
        return lst6
    elif len(lst7) == 4:
        return lst7
    elif len(lst8) == 4:
        return lst8
    elif len(lst9) == 4:
        return lst9
    elif len(lst10) == 4:
        return lst10
    elif len(lst11) == 4:
        return lst11
    elif len(lst12) == 4:
        return lst12
    elif len(lst13) == 4:
        return lst13
    else:
        return False #otherwise if none returns false

def three_7(H):
    '''Return a list of 3 cards with the same rank,
       if 3 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''
    list1 = cannonical(H) #gets organized list
    lst1 = [] #creates 13 empty lists for all ranks
    lst2 = []
    lst3 = []
    lst4 = []
    lst5 = []
    lst6 = []
    lst7 = []
    lst8 = []
    lst9 = []
    lst10 = []
    lst11 = []
    lst12 = []
    lst13 = []
    for i in range(0,len(list1)): #goes through length of organized list
        if list1[i].rank() == 1: #goes through each rank to find matching ones 
            lst1.append(list1[i]) #then appends to list
        elif list1[i].rank() == 2:
            lst2.append(list1[i])
        elif list1[i].rank() == 3:
            lst3.append(list1[i])
        elif list1[i].rank() == 4:
            lst4.append(list1[i])
        elif list1[i].rank() == 5:
            lst5.append(list1[i])
        elif list1[i].rank() == 6:
            lst6.append(list1[i])
        elif list1[i].rank() == 7:
            lst7.append(list1[i])
        elif list1[i].rank() == 8:
            lst8.append(list1[i])
        elif list1[i].rank() == 9:
            lst9.append(list1[i])
        elif list1[i].rank() == 10:
            lst10.append(list1[i])
        elif list1[i].rank() == 11:
            lst11.append(list1[i])
        elif list1[i].rank() == 12:
            lst12.append(list1[i])
        elif list1[i].rank() == 13:
            lst13.append(list1[i])
    if len(lst1) == 3: #checks to see which list has 3 matching ranks in it
        return lst1 #returns that list
    elif len(lst2) == 3:
        return lst2
    elif len(lst3) == 3:
        return lst3
    elif len(lst4) == 3:
        return lst4
    elif len(lst5) == 3:
        return lst5
    elif len(lst6) == 3:
        return lst6
    elif len(lst7) == 3:
        return lst7
    elif len(lst8) == 3:
        return lst8
    elif len(lst9) == 3:
        return lst9
    elif len(lst10) == 3:
        return lst10
    elif len(lst11) == 3:
        return lst11
    elif len(lst12) == 3:
        return lst12
    elif len(lst13) == 3:
        return lst13
    else:
        return False #otherwise if none returns false
        
def two_pair_7(H):
    '''Return a list of 4 cards that form 2 pairs,
       if there exist two pairs in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H) and three_7(H) are both False.'''
    list1 = cannonical(H) #gets organized list
    lst1 = [] #creates 13 empty lists for all ranks
    lst2 = []
    lst3 = []
    lst4 = []
    lst5 = []
    lst6 = []
    lst7 = []
    lst8 = []
    lst9 = []
    lst10 = []
    lst11 = []
    lst12 = []
    lst13 = []
    total_list = []
    if four_7(H) == True or three_7(H) == True:
        return False
    else:
        for i in range(0,len(list1)): #goes through length of organized list
            if list1[i].rank() == 1: #goes through each rank to find matching ones 
                lst1.append(list1[i]) #then appends to list
            elif list1[i].rank() == 2:
                lst2.append(list1[i])
            elif list1[i].rank() == 3:
                lst3.append(list1[i])
            elif list1[i].rank() == 4:
                lst4.append(list1[i])
            elif list1[i].rank() == 5:
                lst5.append(list1[i])
            elif list1[i].rank() == 6:
                lst6.append(list1[i])
            elif list1[i].rank() == 7:
                lst7.append(list1[i])
            elif list1[i].rank() == 8:
                lst8.append(list1[i])
            elif list1[i].rank() == 9:
                lst9.append(list1[i])
            elif list1[i].rank() == 10:
                lst10.append(list1[i])
            elif list1[i].rank() == 11:
                lst11.append(list1[i])
            elif list1[i].rank() == 12:
                lst12.append(list1[i])
            elif list1[i].rank() == 13:
                lst13.append(list1[i])
        if len(lst1) == 2:#checks to see which list has 2 matching ranks in it
            total_list.append(lst1) #rappends to the overall list
        if len(lst2) == 2:
            total_list.append(lst2)
        if len(lst3) == 2: 
            total_list.append(lst3)
        if len(lst4) == 2:
            total_list.append(lst4)
        if len(lst5) == 2:
            total_list.append(lst5)
        if len(lst6) == 2:
            total_list.append(lst6)
        if len(lst7) == 2:
            total_list.append(lst7)
        if len(lst8) == 2:
            total_list.append(lst8)
        if len(lst9) == 2:
            total_list.append(lst9)
        if len(lst10) == 2:
            total_list.append(lst10)
        if len(lst11) == 2:
            total_list.append(lst11)
        if len(lst12) == 2:
            total_list.append(lst12)
        if len(lst13) == 2:
            total_list.append(lst13)
        if len(total_list) != 2:
            return False #otherwise if none returns false
        else:
            #gets rid of the list of lists and makes one list
            total_list = [val for sublist in total_list for val in sublist]
            return total_list #returns list
    

def one_pair_7(H):
    '''Return a list of 2 cards that form a pair,
       if there exists exactly one pair in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H), three_7(H) and two_pair(H) are False.'''
    list1 = cannonical(H) #gets organized list
    lst1 = [] #creates 13 empty lists for all ranks
    lst2 = []
    lst3 = []
    lst4 = []
    lst5 = []
    lst6 = []
    lst7 = []
    lst8 = []
    lst9 = []
    lst10 = []
    lst11 = []
    lst12 = []
    lst13 = []
    for i in range(0,len(list1)): #goes through length of organized list
        if list1[i].rank() == 1: #goes through each rank to find matching ones 
            lst1.append(list1[i]) #then appends to list
        elif list1[i].rank() == 2:
            lst2.append(list1[i])
        elif list1[i].rank() == 3:
            lst3.append(list1[i])
        elif list1[i].rank() == 4:
            lst4.append(list1[i])
        elif list1[i].rank() == 5:
            lst5.append(list1[i])
        elif list1[i].rank() == 6:
            lst6.append(list1[i])
        elif list1[i].rank() == 7:
            lst7.append(list1[i])
        elif list1[i].rank() == 8:
            lst8.append(list1[i])
        elif list1[i].rank() == 9:
            lst9.append(list1[i])
        elif list1[i].rank() == 10:
            lst10.append(list1[i])
        elif list1[i].rank() == 11:
            lst11.append(list1[i])
        elif list1[i].rank() == 12:
            lst12.append(list1[i])
        elif list1[i].rank() == 13:
            lst13.append(list1[i])
    if len(lst1) == 2:#checks to see which list has 3 matching ranks in it
        return lst1 #returns that list
    elif len(lst2) == 2:
        return lst2
    elif len(lst3) == 2:
        return lst3
    elif len(lst4) == 2:
        return lst4
    elif len(lst5) == 2:
        return lst5
    elif len(lst6) == 2:
        return lst6
    elif len(lst7) == 2:
        return lst7
    elif len(lst8) == 2:
        return lst8
    elif len(lst9) == 2:
        return lst9
    elif len(lst10) == 2:
        return lst10
    elif len(lst11) == 2:
        return lst11
    elif len(lst12) == 2:
        return lst12
    elif len(lst13) == 2:
        return lst13
    else:
        return False #otherwise if not returns False

def full_house_7(H):
    '''Return a list of 5 cards forming a full house,
       if 5 of the 7 cards form a full house in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''   
    H  = cannonical(H) #organizes list
    list1 = three_7(H) #checks for three
    list2 = one_pair_7(H) #checks for one pair
    if list1 != False: #if not false
        if list2 != False: #if not false
            return (list2+list1) #concatenate list
    else:
        return False #otherwise if not return False

def main():
    '''This function calls the other functions and displays the game'''
    D = cards.Deck() #calls the deck
    D.shuffle() #shuffles deck
       
    while True: #when true
        community_list = [] #create empty list
        hand_1_list = [] #create empty list
        hand_2_list = [] #create empty list
        for i in range(5): #retreiving five cards for community list
            community_list.append(D.deal())
        for i in range(2): #retreiving two cards for hands
            hand_1_list.append(D.deal())
        for i in range(2):   #retreiving two cards for hands 
            hand_2_list.append(D.deal())
       
        print("-"*40) #display
        print("Let's play poker!\n") #display
        print("Community cards:",community_list) #display
        print("Player 1:",hand_1_list) #display
        print("Player 2:",hand_2_list) #display
        print()
        hand1 = hand_1_list + community_list #combining hand and community
        hand2 = hand_2_list + community_list #combining hand and community
        if straight_flush_7(hand1): #calling straight flush in hand 1
            if straight_flush_7(hand2): #calling straight flush in hand 2
                #there is a tie
                print('TIE with a straight flush:', straight_flush_7(hand1))
            else:
                #player one wins
                print('Player 1 wins with a straight flush:', \
                      straight_flush_7(hand1))
        elif four_7(hand1): #calling four in hand 1
            if four_7(hand2):#calling four in hand 2
                 #there is a tie
                print('TIE with a four:', four_7(hand1))
            else:
                 #player one wins
                print('Player 1 wins with four of a kind:', four_7(hand1))
        elif full_house_7(hand1): #calling full house in hand 1
            if full_house_7(hand2): #calling full house in hand 2
                 #there is a tie
                print('TIE with a full house:', full_house_7(hand1))
            else:
                 #player one wins
                print('Player 1 wins with a full house:', full_house_7(hand1))
        elif flush_7(hand1): #calling flush in hand 1
            if flush_7(hand2): #calling flush in hand 2
                 #there is a tie
                print('TIE with a flush:', flush_7(hand1))
            else:
                 #player one wins
                print('Player 1 wins with a flush:', flush_7(hand1))
        elif straight_7(hand1): #calling straight in hand 1
            if straight_7(hand2): #calling straight in hand 2
                 #there is a tie
                print('Tie with a straight:', straight_7(hand1))
            else:
                 #player one wins
                print('Player 1 wins with a straight:', straight_7(hand1))
        elif three_7(hand1): #calling three in hand 1
            if three_7(hand2):#calling three in hand 2
                 #there is a tie
                print('TIE with a three:', three_7(hand1))
            else:
                 #player one wins
                print('Player 1 wins with a three:', three_7(hand1))
        elif two_pair_7(hand1): #calling two pair in hand 1
            if two_pair_7(hand2): #calling two pair in hand 2
                 #there is a tie
                print('TIE with two pairs:', two_pair_7(hand1))
            else:
                 #player one wins
                print('Player 1 wins with a two pair:', two_pair_7(hand1))
        elif one_pair_7(hand1): #calling one pair in hand 1
            if one_pair_7(hand2): #calling one pair in hand 2
                 #there is a tie
                print('TIE with a one pair:', one_pair_7(hand1))
            else:
                 #player one wins
                print('Player 1 wins with a one pair:', one_pair_7(hand1))
        if len(D) < 9: #checking if there are less than 9 cards left in deck
            print('Deck has too few cards so game is done.')
            break #if so then break
        y = input("Do you wish to play another hand?(Y or N) ").lower() #prompt
        if y == 'n': #if they click n
            break #break

if __name__ == "__main__":
    main()