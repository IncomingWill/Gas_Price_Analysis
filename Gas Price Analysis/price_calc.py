# Title: Gas Price Analysis Program
# Program created by William Schaeffer
# CPS 313
# P. 465, Exercise 14, Gas Price Analysis Program
# 02.08.22

import re

#Function to welcome the user

def welcome_function():

    print(f'Welcome to the Gas Price Analysis Program!')
    print(f'This program will analyze gas prices from a document.')
    print(f'It will then output the list of prices from highest to lowest to a new document named l_to_h_gas.txt.')
    print(f'It will then output the list of prices from lowest to highest to a new document named h_to_l_gas.txt.')
    print(f'The program will create new files by these names, and it will overwrite them if they already exist.\n')

#Function to create the list of gas prices, and to convert strings to int and float values

def form_gas_price_list(list):
                                                        # i = major list element
    for i in range(len(list)):                          # create range, index of last element is len(list)
        list[i] = re.split(":", list[i])                # split apart date and gas price, [i][0] is date, [i][1] is gas price
        if list[i]:                                     # for each major list element
            list[i][0] = re.split("-", list[i][0])      # split single date element into three element nested list ['mm', 'dd', 'yyyy']
                                                        # [i][0] is date, [i][1] is gas price
            list[i][0][0] = int(list[i][0][0])          # convert month from string to int [i][0][0] is month
            list[i][0][1] = int(list[i][0][1])          # convert day from string to int [i][0][1] is day
            list[i][0][2] = int(list[i][0][2])          # convert year from string to int [i][0][2] is year
            
            list[i][1] = float(list[i][1])              # convert price string to float [i][1] is gas price

    return list                                         # return change_list to pass to other functions
    #print(f'{list}')                                   # commented print of change_list for test verification

# Function to perform and print average price per year and average price per month calculations
    # This function will also display the lowest and highest average for the current year

def avg_min_max_price(list, year):
    
    year_list = []                                      # initialize list to hold prices for current year, and yearly average
    year_average = 0.0
    month = 1                                           # initialize month at 1 (January)
    
    for i in range(len(list)):
        if(list[i][0][2] == year):
            year_list.append(list[i][1])
    
    maximumValue = max(year_list)                       # find maximum gas price in current year's list
    minimumValue = min(year_list)                       # find min
    max_i = (year_list.index(maximumValue))             # find index for maximum and minimum values from current year's list
    min_i = (year_list.index(minimumValue))
                                                        # print with month_swap function formatting
    print(f'The minimum average price for {year} was during the week of ', end='')
    print(f'{month_swap(list[min_i][0][0])}, {list[min_i][0][1]} and is ${list[min_i][1]:,.2f}')
    
    print(f'The maximum average price for {year} was during the week of ', end='')
    print(f'{month_swap(list[max_i][0][0])}, {list[max_i][0][1]} and is ${list[max_i][1]:,.2f}')

    year_average = avg_price_calculator(year_list)      # calculate average for the current year

    #print(f'{year} year price list: {year_list}')      # for testing purposes
    
    print(f'Weekly Average Gas Price for the year of {year}: ${year_average:,.2f}')
    
    for m in range(1, 13, 1):                           # step through each month of the year
        month_price_calculator(list, month, year)
        month += 1

#Function to calculate the monthly average by dividing the total from the list by lengh of list

def month_price_calculator(list, month, year):

    month_list = []                                     # initialize list to hold prices for current month, and current month average
    month_average = 0.0

    for i in range(len(list)):
        if(list[i][0][2] == year and list[i][0][0] == month):
            month_list.append(list[i][1])               # month list created from gas_list by verifying year AND month
    if not month_list:                                  # if the list is empty(False), return None -- for years with missing months
        return None
    else:                                               # calculate average with each month's values
        month_average = avg_price_calculator(month_list)

    #print(f'{month_swap(month)} price list: {month_list}') #for testing purposes
    
    print(f'{month_swap(month)} Average: ${month_average:,.2f}')

# Function to calculate average price by dividing the total by length of given list

def avg_price_calculator(list):
    
    total = 0.0                                         # create accumulator
    
    for value in list:                                  # calculate total
        total += value

    average = total / len(list)                         # average equals total divided by number of elements in list
    return average

# Function to sort list from lowest to highest gas price and output to file

def lowest_to_highest(list, outfile):

    list.sort(key = lambda x: x[1])                     # key is to sort second element, by default reverse = false

    #print(list)                                        #for testing purposes
    
    for i in range(len(list)):
        outfile.write(f'{month_swap(list[i][0][0])}, {list[i][0][1]} {list[i][0][2]}: ${list[i][1]:,.2f}\n')

# Function to sort list from highest to lowest gas price and output to file

def highest_to_lowest(list, outfile):

    list.sort(key = lambda x: x[1], reverse=True)       # key is to sort second element

    #print(list)                                        #for testing purposes


    for i in range(len(list)):
        outfile.write(f'{month_swap(list[i][0][0])}, {list[i][0][1]} {list[i][0][2]}: ${list[i][1]:,.2f}\n')

# Function to swap out month integer with month string name

def month_swap(m):
   
    if (m == 1):
        m = 'January'
    elif (m == 2):
        m = 'February'
    elif (m == 3):
        m = 'March'
    elif (m == 4):
        m = 'April'
    elif (m == 5):
        m = 'May'
    elif (m == 6):
        m = 'June'
    elif (m == 7):
        m = 'July'
    elif (m == 8):
        m = 'August'
    elif (m == 9):
        m = 'September'
    elif (m == 10):
        m = 'October'
    elif (m == 11):
        m = 'November'
    elif (m == 12):
        m = 'December'

    return m


