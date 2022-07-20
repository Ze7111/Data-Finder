from rich.console import Console # import console
from rich.table import Table, Column # import table and column
from time import sleep # import sleep
import random, logging # import modules
from rich.progress import Progress, BarColumn, TextColumn # import progress bar

logging.info('Rich Class Loaded Successfully') # Log the successful load of the rich class

class basic_UI_elements(): # class for basic UI elements
    
    def datafetch(list_elements): # function to fetch data from list    
        
        console = Console() # create console object
        
        time = random.uniform(0.4, 1.5) # generate random time between 0.4 and 1.5 seconds
        data = list_elements # assign list elements to data
        
        logging.info(f'Successfully fetched length of data from list') # log success
        
        if len(data) > 300: # if data is empty
            time = 0.00001
        elif len(data) > 100: # if data is empty
            time = 0.005
        elif len(data) > 50 < 100: # if data is empty
            time = 0.05
        elif len(data) > 10 < 50: # if data is empty
            time = 0.2
        
        pos = 0 # set position to 0
        loc = 0 # set location to 0
        
        logging.info('Successfully set inital values')
        logging.info('Starting to fetch data')
        
        try: # try to fetch data
            pos = data.index('error') + 1 # set position to index of error + 1
            logging.info('Found error in data')
        except: # if error, do nothing
            pass # do nothing
        
        with console.status("[red]Fetching Data Points...", spinner='aesthetic', speed=0.6) as status: # create status bar
            logging.info('Creating status bar')
            
            while data: # while data is not empty
                
                num = data.pop(0) # pop first element from list
                sleep(time) # sleep for time
                
                loc += 1 # increment location
                
                if 'error' in data: # if error in data
                    console.print(f'Received error from server at data point : {pos}', style='red') # print error message
                    logging.warning('FAILED TO FETCH DATA VALUES')
                    return 'error' # return error
                
                console.log(f"[green]Fetched Data Point[/green] {num}") # print data point
                
            logging.info('Data fetch sequence completed')
            
            console.log(f'[bold][red]Done!') # print done message
                
        return 'done' # return done
    
    def foundtable(index_data, name_data, dob_data, location_data, phone_data, email_data, extra_data): # function to create table
        console = Console() # create console object

        table = Table(title="") # create table

        table.add_column("Index", style="cyan", justify="center") # add column
        table.add_column("Name", style="magenta", justify="center") # add column
        table.add_column("DOB", justify="center", style="green") # add column
        table.add_column("Phone", justify="center", style="green") # add column
        table.add_column("Email", justify="center", style="green") # add column
        table.add_column("Location", justify="center", style="green") # add column
        table.add_column("Extra", justify="center", style="green") # add column
         
        logging.info('Successfully created base table') # log success
        
        index = 0 # set index to 0
        
        try: # try to create table
            for i in index_data: # for each index in index_data
                table.add_row(index_data[index], name_data[index], dob_data[index], phone_data[index], email_data[index], location_data[index], extra_data[index]) # add row
                index += 1 # increment index
                indexbeforeerror = index # set indexbeforeerror to index
                logging.info(f'Successfully added data point {index} to table') # log success
                if 'error' in index_data: # if error in index_data
                    console.print(f'Received error from server at data point : {indexbeforeerror}', style='red') # print error message
                    logging.warning('Invalid data points found') # log error
        except: # if error, do nothing
            table.add_row(index_data[index], "None", "None", "None", "None", "None") # add row
            console.print(f"[bold red]Error:[/bold red] Data point {indexbeforeerror+1} and higher is currupted", style="red") # print error message
            
            logging.warning(f'Error: Data point {indexbeforeerror+1} and higher is currupted') # log error
        
        if len(index_data) > 300: # if data is empty
            console.print("[bold green]Data Output", justify="relative")
            logging.warning('Successfully printed LARGE table') # log success
            console.print(table)
            return
        
        basic_UI_elements.datafetch(index_data) # fetch data
        
        console.print("[bold green]Data Output", justify="relative") # print header
        
        console.print(table) # print table
        logging.info('Successfully printed table') # log success
        return 'done' # return done
        






# index_data = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# list_elements = index_data
# basic_UI_elements.datafetch(list_elements)

# index_data = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# name_data = ['John', 'Jane', 'Bob', 'Mary', 'Joe', 'Jill']
# dob_data = ['01/01/2000', '01/01/2000', '01/01/2000', '01/01/2000', '01/01/2000', '01/01/2000']
# phone_data = ['123-456-7890', '123-456-7890', '123-456-7890', '123-456-7890', '123-456-7890', '123-456-7890']
# email_data = ['soe@gmail.com', 'fuia@fojk.copm', 'sadd@fnaa.com', 'soedfg@gmail.com', 'fuiagdf@fojk.copm', 'sagfdd@fnaa.com']
# location_data = ['New York', 'chicago', 'Los Angeles', 'San Francisco', 'Dallas', 'Austin']
# extra_data = ['wanted', 'none', 'wanted', 'none', 'wanted', 'none']

# basic_UI_elements.foundtable(index_data, name_data, dob_data, location_data, phone_data, email_data, extra_data)
    