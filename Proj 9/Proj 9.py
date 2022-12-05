#######################################################################
#    Computer Project #9
#    
#    Program that takes in user input to print out the necessary \n
#    information based on the input that is given
#
#    The first part of the program displays the the menu options \n
#    and the welcome text for the user
#
#    The next part is the open file function that opens the file \n
#    based on the user input
#
#    Next is the read_file that reads the securities file \n
#    and returns the names of the company 
#
#    Next is the add prices function that information for price
#
#    Following that is the get_max_price_of_company function \n
#    that get the max price and the date of the given copmpany 
#
#    Onward is the find_max_company_price that finds the company \n
#    with the highest price 
#
#    Next is the get_avg_price function that gets the average price \n
#    of the given company 
#
#    The last funciton is the display_list function that displays \n
#    a list of strings in 3 columns
#
#    As we go into the main, all the functions are called and menu \n
#    options are displayed for the user
#
#    The user picks between 6 options and gets information based on \n
#    the input given
#
#    To close the program, the user must enter 6
#######################################################################
import csv

# Menu options for the user
MENU = '''\nSelect an option from below:
            (1) Display all companies in the New York Stock Exchange
            (2) Display companies' symbols
            (3) Find max price of a company
            (4) Find the company with the maximum stock price
            (5) Find the average price of a company's stock
            (6) quit
    '''
WELCOME = "Welcome to the New York Stock Exchange.\n"
# Welcomes the user

# Opens the prices abd securities file
def open_file():
    file_input = input("\nEnter the price's filename: ")

    x = 0
    while x == 0:
        try:
            price_file_pointer = open(file_input)
            break
        except:
            print("\nFile not found. Please try again.")
            file_input = input("\nEnter the price's filename: ")

    file_input = input("\nEnter the security's filename: ")
    x = 1
    while x == 1:
        try:
            securities_file_pointer = open(file_input)
            break
        except:
            print("\nFile not found. Please try again.")
            file_input = input("\nEnter the security's filename: ")

    return price_file_pointer, securities_file_pointer
# Returns two file pointers(price and security)


# Reads the securities file pointer to create a set of company \n
# characteristics and a dictionary
def read_file(securities_fp):
    reader = csv.reader(securities_fp)
    next(reader, None)

    sec_dict = {}
    com_names = set()
    for each_line in reader:

        sec_dict[each_line[0]] = [each_line[1], each_line[3],each_line[4], each_line[5], each_line[6], []]

        com_names.add(each_line[1])

    return com_names, sec_dict

# Returns the set of names and dictionary


# Adds the information for price to the dictionary
def add_prices(master_dictionary, prices_file_pointer):
    reader = csv.reader(prices_file_pointer)
    next(reader, None)

    for each_line in reader:
        price_list = [each_line[0], float(each_line[2]), float(
            each_line[3]), float(each_line[4]), float(each_line[5])]

        try:
            value = master_dictionary[each_line[1]]
            value[5].append(price_list)

        except KeyError:
            continue

# Returns nothing


# Gets the max price of a company and the date of the max price
def get_max_price_of_company(master_dictionary, company_symbol):

    if company_symbol in master_dictionary.keys():
        cs = master_dictionary[company_symbol][5]
        if cs == []:
            return None,None

        list = []
        for symbol in cs:
            date = symbol[0]
            high_info = symbol[4]

            my_tup = (high_info, date)

            list.append(my_tup)

        max_list = max(list)

        return max_list
    else:
        return None, None
# Returns the max price and date but returns None if no max exists

# Finds the company with the max price
def find_max_company_price(master_dictionary):

    my_tup = []
    for symbol in master_dictionary:
        if master_dictionary[symbol][5] != []:
            max_price, max_date = get_max_price_of_company(
                master_dictionary, symbol)

            if max_price != None and max_date != None:

                my_tup.append((max_price, symbol))

    max_comp_price = max(my_tup)

    return max_comp_price[1], max_comp_price[0]

# Returns the company and the max price


# Gets the average price of a given company
def get_avg_price_of_company(master_dictionary, company_symbol):

    if company_symbol in master_dictionary.keys():
        cs = master_dictionary[company_symbol][5]

        if cs == []:
            return 0.0

        prices = []
        for price in cs:
            price_val = price[4]

            prices.append(price_val)

            sum_of_prices = sum(prices)

            length_of_cs = len(cs)

            avg = sum_of_prices / length_of_cs

        return round(avg, 2)

    else:
        return 0.0
# Returns the average or returns 0.0 if the comapny doesn't exist \n
# or there is no price data


# Displays a list of strings in 3 columns
def display_list(lst):  # "{:^35s}"
    count = 0
    for i in lst:
        print(f"{i:^35s}", end="")
        count += 1
        if count == 3:
            print()

            count = 0
    print("\n")

# Returns nothing
def main():
    print(WELCOME)

    fp, fp2 = open_file()

    keys_, master_dictionary = read_file(fp2)
    keys = []
    for i in keys_:
        keys.append(i)

    add_prices(master_dictionary, fp)

    print(MENU)
    menu_options = int(input("\nOption: "))

    while menu_options != 6:

# Displays all the companies in the New York Stock Exchange
        if menu_options == 1:
            print("\n{:^105s}".format("Companies in the New York Stock Market from 2010 to 2016"))
            sorted_keys = sorted(keys)
            display_list(sorted_keys)

# Displays the companies symbols
        if menu_options == 2:
            print("\ncompanies' symbols:")
            emp_list = []

            for comp_symbol, list in master_dictionary.items():
                if comp_symbol in master_dictionary:
                    emp_list.append(comp_symbol)

                    emp_list.sort()
            dl = display_list(emp_list)

# Finds max price of a company
        if menu_options == 3:
            max_price_inp = input("\nEnter company symbol for max price: ")

            while True:
                if max_price_inp in master_dictionary:
                    mpc,mpc2 = get_max_price_of_company(master_dictionary, max_price_inp)
                    break
                    

                else:
                    print("\nError: not a company symbol. Please try again.")
                    max_price_inp = input("\nEnter company symbol for max price: ")
                    continue
            
            if mpc == None:
                print("\nThere were no prices.")
            else:
                print("\nThe maximum stock price was ${:.2f} on the date {:s}/\n".format(mpc,mpc2))

# Finds the company with the max price
        if menu_options == 4:
            mcp,mcp2 = find_max_company_price(master_dictionary)

            print("\nThe company with the highest stock price is {:s} with a value of ${:.2f}\n".format(mcp,mcp2))

# Finds the average price of the company's stock
        if menu_options == 5:

            avg_comp_inp = input("\nEnter company symbol for average price: ")
            
            while True:
                if avg_comp_inp in master_dictionary:
                    avg_comp_price = get_avg_price_of_company(master_dictionary,avg_comp_inp)

                    if avg_comp_price == 0:
                        print("\nThere were no prices.")
                    
                    else:
                        print("\nThe average stock price was ${:.2f}.\n".format(avg_comp_price))
                        break
                else:

                    print("\nError: not a company symbol. Please try again.")
                    avg_comp_inp = input("\nEnter company symbol for average price: ")

# Closes the program
        if menu_options == 6:
            quit()

# Repompts user for menu options
        print(MENU)
        menu_options = int(input("\nOption: "))


if __name__ == "__main__":
    main()
