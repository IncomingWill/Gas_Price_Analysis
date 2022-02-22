# Title: Gas Price Analysis Program
# Program created by William Schaeffer
# CPS 313
# P. 465, Exercise 14, Gas Price Analysis Program
# 02.08.22

# This program will read a file average gas prices and determine:
    # Average Price Per Year
    # Average Price Per Month
    # Highest and Lowest Prices Per Year
    # Two list of prices, highest to lowest and lowest to highest

# imports for functions

import price_calc

# Main Function

def main():

    price_calc.welcome_function()                           # Call welcome function
    
    year = 1993                                             # initialize start year

    gas_price_file = open('GasPrices.txt')                  # open text.txt

    gas_list = [line.strip() for line in gas_price_file]    # create gas price list from file
    
    gas_list = price_calc.form_gas_price_list(gas_list)     # create nested list[['mm', 'dd', 'yyyy'], 'price']
                                                            # also converts from string to int for date elements and to float for price
    #print(gas_list)                                        #for testing purposes

    for y in range(1993, 2014, 1):                          # for each year starting in 1993 and ending in 2014
        price_calc.avg_min_max_price(gas_list, year)        # call average price function
        year += 1                                           # increment year by 1
        print('\n')
    
    outfile_l_to_h = open('l_to_h_gas.txt', 'w')            # open writefile for lowest to highest
    outfile_h_to_l = open('h_to_l_gas.txt', 'w')            # open writefile for highest to lowest

    price_calc.lowest_to_highest(gas_list, outfile_l_to_h)  # call functions to sort and output to files
    price_calc.highest_to_lowest(gas_list, outfile_h_to_l)

    outfile_l_to_h.close()                                  # close read and write files
    outfile_h_to_l.close()
    gas_price_file.close()                                  

main()                                                      # call main function
