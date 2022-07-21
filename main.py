try: # try
    import os  # import os
    
except: # except
    print("Please install OS module") # print info
    print("using 'pip install os' or 'pip3 install os'") # print info
    
try: # try
    import logging  # import logging module
    import random  # import random module
    import sys  # import sys module
    import time  # import time module

    import pandas  # import pandas module
    import psutil  # import psutil module
    import rich  # import rich module
    
    
except ImportError as e: # except
    os.system('pip install rich') # install rich
    os.system('pip install logging') # install logging
    os.system('pip install sys') # install sys
    os.system('pip install time') # install time
    os.system('pip install random') # install random
    os.system('pip install pandas') # install pandas
    os.system('pip install psutil') # install psutil
    
    print("Please restart the program to continue") # print info
    exit() # exit program


logging.basicConfig(level=logging.INFO,filename='debug\data.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

logging.warning('Program is starting') # log start

from rich import console, syntax
from rich.table import Table

from scripts.accumulator import variable_organizer

text = console.Console() # create console object

def __innit__(): # function to initialize program

    logging.warning('INITIALIZING ALL FILES') # Log initialization

    os.system('cls') # clear screen

    text.print("""[blink]
██████████     █████████   ███████████   █████████         ███████████ █████ ██████   █████ ██████████   ██████████ ███████████  
░░███░░░░███   ███░░░░░███ ░█░░░███░░░█  ███░░░░░███       ░░███░░░░░░█░░███ ░░██████ ░░███ ░░███░░░░███ ░░███░░░░░█░░███░░░░░███ 
 ░███   ░░███ ░███    ░███ ░   ░███  ░  ░███    ░███        ░███   █ ░  ░███  ░███░███ ░███  ░███   ░░███ ░███  █ ░  ░███    ░███ 
░███    ░███ ░███████████     ░███     ░███████████        ░███████    ░███  ░███░░███░███  ░███    ░███ ░██████    ░██████████  
 ░███    ░███ ░███░░░░░███     ░███     ░███░░░░░███        ░███░░░█    ░███  ░███ ░░██████  ░███    ░███ ░███░░█    ░███░░░░░███ 
 ░███    ███  ░███    ░███     ░███     ░███    ░███        ░███  ░     ░███  ░███  ░░█████  ░███    ███  ░███ ░   █ ░███    ░███ 
 ██████████   █████   █████    █████    █████   █████       █████       █████ █████  ░░█████ ██████████   ██████████ █████   █████
░░░░░░░░░░   ░░░░░   ░░░░░    ░░░░░    ░░░░░   ░░░░░       ░░░░░       ░░░░░ ░░░░░    ░░░░░ ░░░░░░░░░░   ░░░░░░░░░░ ░░░░░   ░░░░░ 
""", justify="center", style="red") # print header
    textbox()
    
def restart_program():
    """Restarts the current program, with file objects and descriptors
       cleanup
    """

    try:
        p = psutil.Process(os.getpid())
        for handler in p.get_open_files() + p.connections():
            os.close(handler.fd)
    except Exception as e:
        logging.error(e)

    python = sys.executable
    os.execl(python, python, "\"{}\"".format(sys.argv[0]))

def textbox(): # function to create textbox
    text.print("\nWho do you want to search for?\n__________________________________\n", style='red') # print question top
    text.print("[blink]▐", style="green", end=' ') # print left side of textbox
    search = input("").lower() # ask for input
    
    logging.info(f'User search (Name) entry screen is active') # log user entry
    
    if search == '-e': # if exit
        logging.warning('User requested to exit') # log exit
        
        text.print("Exiting...", style="red", justify="center") # print exit message
        exit() # exit program
    
    elif search == '-c': # if clear
        logging.info('User requested to clear screen') # log clear
        
        os.system('cls') # clear screen
        textbox() # call textbox function
    
    elif search == '-f': # if help
        logging.info('User requested to use filter') # log filter
        
        extra.filter_search() # call filter function
    
    elif search == '-a': # if add
        logging.info('User requested to add a new entry into the database') # log add
        
        extra.add_data() # call add function
    
    elif search == '-d': # if delete
        logging.info('User requested to delete an entry from the database') # log delete
        pass # delete data MAKE THIS HAPPEN --------------------------------------------------------------------------------
    
    elif search == '-r':
        logging.info('User requested to restart the program') # log run
        restart_program()
    
    elif search == '-all': # if all
        
        condition = 'all' # set condition to dob
        search = 'none' # set search to none
             
        s = variable_organizer.data_organizer(search, condition) # call data organizer
        
        textbox() # call textbox function
    
    elif search == 'help': # if help
        text.print('\nTo use help use "-h"', style='green') # print help
        time.sleep(3) # sleep for 3 seconds
        pass
    
    elif search == '-h': # if help
        logging.info('User requested help') # log help
        
        text.print("\n------------Help Menu------------", style="#ff0000", justify="center") # print help menu
        text.print("'-c' is used to clear the screen ", style="#ff4000", justify="center") # print help menu
        text.print("'-e' is used to exit the program ", style="#ff4000", justify="center") # print help menu
        text.print("'-r' is used to reset the program", style="#ff4000", justify="center") # print help menu
        text.print("'-f' is used to filter the data  ", style="#ff4000", justify="center") # print help menu
        text.print("'-a' is used to add new data     ", style="#ff4000", justify="center") # print help menu
        text.print("'-d' is used to remove data      ", style="#ff4000", justify="center") # print help menu
        text.print("'-all' is used to show all data\n", style="#ff4000", justify="center") # print help menu
        
        textbox() # call textbox function
        
    condition = 'name' # set condition to name
    
    s = variable_organizer.data_organizer(search, condition) # call data organizer
    
    if s == 'none': # if error
        time.sleep(1)
        countdown = 4 # set countdown to 4
        for i in range(0,4): # for loop
            text.print(f"Program will restart in {countdown} seconds", style="green", justify="center") # print countdown
            time.sleep(1) # sleep for 1 second
            os.system('cls') # clear screen
            countdown -= 1 # countdown - 1 
        logging.warning('Program got an search error') # log error
        textbox() # call textbox function
    
        
    textbox() # call textbox function 
    

class extra: # class to create extra functions
    def filter_search(): # function to filter data
        logging.info('User requested to filter the data') # log filter
        
        text.print("\nWhat field do you want to search in? (use -h for help)\n__________________________________\n", style="red") # print question top
        text.print("[blink]▐", style="#fff200", end=' ') # print a blinking cursor
        
        field = input("").lower() # ask for input
        
        if field == '-h': # if help
            logging.info('User requested help with filter') # log help
            
            text.print("\nPossible Options:", style="red", justify="center") # print possible options
            text.print("Name\nDOB\nPhone\nEmail\nLocation\nExtra\n", style="bold red", justify="center") # print possible options
            
            extra.filter_search() # call filter function
        
        
        
        elif field == 'name': # if name
            logging.info('User requested to filter by Name') # log filter 
            
            text.print("\nWhat is the date of name?\n__________________________________\n", style="red") # print question top
            text.print("[blink]▐", style="#ff4000", end=' ') # print a blinking cursor
            
            search = input("").lower() # ask for input
            
            condition = 'name' # set condition to dob
             
            s = variable_organizer.data_organizer(search, condition) # call data organizer

            if s == 'none': # if error
                time.sleep(1) # sleep for 1 second
                countdown = 4 # set countdown to 4
                
                for i in range(0,4): # for loop
                    text.print(f"Program will restart in {countdown} seconds", style="green", justify="center") # print countdown
                    os.system('cls') # clear screen
                    time.sleep(1) # sleep for 1 second
                     
                    countdown -= 1 # countdown - 1
                    
                textbox() # call textbox function
            textbox() # call textbox function



        elif field == 'dob':
            logging.info('User requested to filter by DOB') # log filter 
            
            text.print("\nWhat is the date of birth?\n__________________________________\n", style="red") # print question top
            text.print("[blink]▐", style="#ff4000", end=' ') # print a blinking cursor
            
            search = input("").lower() # ask for input
            
            condition = 'dob' # set condition to dob
             
            s = variable_organizer.data_organizer(search, condition) # call data organizer

            if s == 'none': # if error
                time.sleep(1) # sleep for 1 second
                countdown = 4 # set countdown to 4
                
                for i in range(0,4): # for loop
                    text.print(f"Program will restart in {countdown} seconds", style="green", justify="center") # print countdown
                    os.system('cls') # clear screen
                    time.sleep(1) # sleep for 1 second
                     
                    countdown -= 1 # countdown - 1
                    
                textbox() # call textbox function
            textbox() # call textbox function
        
        
        
        elif field == 'phone': # if phone
            logging.info('User requested to filter by phone number') # log filter
            
            text.print("\nWhat is the phone number?\n__________________________________\n", style="red") # print question top
            text.print("[blink]▐", style="#ff4000", end=' ') # print a blinking cursor
            
            search = input("").lower() # ask for input
            
            condition = 'phone' # set condition to phone
            
            s = variable_organizer.data_organizer(search, condition) # call data organizer
            
            if s == 'none': # if error
                time.sleep(1) # sleep for 1 second
                countdown = 4 # set countdown to 4
                
                for i in range(0,4): # for loop
                    text.print(f"Program will restart in {countdown} seconds", style="green", justify="center") # print countdown
                    os.system('cls') # clear screen
                    time.sleep(1) # sleep for 1 second
                     
                    countdown -= 1 # countdown - 1
                    
                textbox() # call textbox function
            textbox() # call textbox function
        
        
                
        elif field == 'email': # if email
            logging.info('User requested to filter by email') # log filter
            
            text.print("\nWhat is the email?\n__________________________________\n", style="red") # print question top
            text.print("[blink]▐", style="#ff4000", end=' ') # print a blinking cursor
            
            search = input("").lower() # ask for input
            
            condition = 'email' # set condition to email
            
            s = variable_organizer.data_organizer(search, condition) # call data organizer
            
            if s == 'none': # if error
                time.sleep(1) # sleep for 1 second
                countdown = 4 # set countdown to 4
                
                for i in range(0,4): # for loop
                    text.print(f"Program will restart in {countdown} seconds", style="green", justify="center") # print countdown
                    os.system('cls') # clear screen
                    time.sleep(1) # sleep for 1 second
                     
                    countdown -= 1 # countdown - 1
                    
                textbox() # call textbox function
            textbox() # call textbox function
        
        
                
        elif field == 'location': # if location
            logging.info('User requested to filter by location') # log filter
            
            text.print("\nWhat is the location?\n__________________________________\n", style="red") # print question top
            text.print("[blink]▐", style="#ff4000", end=' ') # print a blinking cursor
            
            search = input("").lower() # ask for input
            
            condition = 'location' # set condition to location
            
            s = variable_organizer.data_organizer(search, condition) # call data organizer
            
            if s == 'none': # if error
                time.sleep(1) # sleep for 1 second
                countdown = 4 # set countdown to 4
                
                for i in range(0,4): # for loop
                    text.print(f"Program will restart in {countdown} seconds", style="green", justify="center") # print countdown
                    os.system('cls') # clear screen
                    time.sleep(1) # sleep for 1 second
                     
                    countdown -= 1 # countdown - 1
                    
                textbox() # call textbox function
            textbox() # call textbox function
        
        
                
        elif field == '-e': # if error
            textbox() # call textbox function
        
        
             
        elif field == 'extra': # if extra
            logging.info('User requested to filter by extra') # log filter
            text.print("\nHow much is the bank balance?\n__________________________________\n", style="red") # print question top
            text.print("[blink]▐", style="#ff4000", end=' ') # print a blinking cursor
            search = input("").lower() # ask for input
            
            s = variable_organizer.data_organizer(search, 'extra') # call data organizer
            
            if s == 'none': # if error
                time.sleep(1) # sleep for 1 second
                countdown = 4 # set countdown to 4
                
                for i in range(0,4): # for loop
                    text.print(f"Program will restart in {countdown} seconds", style="green", justify="center") # print countdown
                    os.system('cls') # clear screen
                    time.sleep(1) # sleep for 1 second
                     
                    countdown -= 1 # countdown - 1
                    
                textbox() # call textbox function
            textbox() # call textbox function
            
            
                
        else: # if error
            countdown = 5 # set countdown to 5
                
            for i in range(0,5): # for loop
                text.print(f"Invalid input please try again in {countdown}", style="red", justify="center") # print countdown
                time.sleep(1) # sleep for 1 second
                os.system('cls') # clear screen
                countdown -= 1 # countdown - 1
                
            extra.filter_search() # call filter function
        


    def add_data(): # function to add data
        logging.info('Add data Script loaded')  # log add data
        
        text.print("\nWhat is the name? (First Second)\n__________________________________\n", style="red") # print question top
        text.print("[blink]▐", style="#ff4000", end=' ') # print a blinking cursor
        new_name = input("") # ask for input
        
        text.print("\nWhat is the Date Of Birth? (dd/mm/yyyy)\n__________________________________\n", style="red") # print question top
        text.print("[blink]▐", style="#ff4000", end=' ') # print a blinking cursor
        new_dob = input("") # ask for input\
        
        text.print("\nWhat is the phone number? (+### (###) ###-####)\n__________________________________\n", style="red") # print question top
        text.print("[blink]▐", style="#ff4000", end=' ') # print a blinking cursor
        new_phone = input("") # ask for input
        
        text.print("\nWhat is the email? (someone@example.com)\n__________________________________\n", style="red") # print question top
        text.print("[blink]▐", style="#ff4000", end=' ') # print a blinking cursor
        new_email = input("") # ask for input
        
        text.print("\nWhat is the location? (Street Number   Street Name)\n__________________________________\n", style="red") # print question top
        text.print("[blink]▐", style="#ff4000", end=' ') # print a blinking cursor
        new_location = input("") # ask for input
        
        text.print("\nWhat is the bank balance? ($---)\n__________________________________\n", style="red") # print question top
        text.print("[blink]▐", style="#ff4000", end=' ') # print a blinking cursor
        new_extra = input("") # ask for input
        
        extra.add_new_info(new_name, new_dob, new_phone, new_email, new_location, new_extra) # call add new info function
   
        
        
    def add_new_info(new_name, new_dob, new_phone, new_email, new_location, new_extra):    # function to add new info 
        def _count_generator(reader): # function to count generator
            b = reader(1024 * 1024) # read in 1MB
            while b: # while loop
                
                yield b # yield
                b = reader(1024 * 1024) # read in 1MB

        def writenewinfo(): # function to write new info
            f = open('data\\data.csv', 'a+') # open data file
            f.write(f'{count},{new_name},{new_dob},{new_phone},{new_email},{new_location},{new_extra}\n') # write new info
            
            logging.info(f'User requested to add the following data\nIndex: {count}\nName: {new_name}\nDOB: {new_dob}\nPhone: {new_phone}\nEmail: {new_email}\nLocation: {new_location}\nExtra: {new_extra}') # log new info
            
            f.close # close file
            textbox() # call textbox function

        try:
            with open(r'data\\data.csv', 'rb') as fp: # open data file
                logging.info("Sucessfully opened the file") # log file open
                
                c_generator = _count_generator(fp.raw.read) # call count generator
                count = sum(buffer.count(b'\n') for buffer in c_generator) # count each \n
                
                logging.info(f'Total number of lines in the file: {count}') # log count
                
                fp.close() # close file
                
        except FileNotFoundError: # if error
            logging.info("File not found", exc_info=True) # log error
            textbox() # call textbox function
                
        writenewinfo() # call write new info function

__innit__() # call init function
