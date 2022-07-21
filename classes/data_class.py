import pandas as pd # data processing, CSV file I/O (excel)
from rich.console import Console # import rich console
import logging # import logging module
from classes.rich_class import basic_UI_elements # import basic UI elements



logging.info('Data Class Loaded Successfully') # Log data class load success

complete = False # set complete to false
complete1 = False # set complete to false   

class datacollect(): # class for data collection
    
    def csv_to_lists(file_path): # function to convert csv to lists
        
        global complete, complete1 # set global variables
        console = Console() # create console object
        
        try: # try to read csv
            file = file_path # assign file path to file
            df = pd.read_csv(file, usecols = ['Index', 'Name', 'DOB', 'Phone', 'Email', 'Location', 'Extra']) # read csv
            
            index_data = df['Index'].tolist() # assign index data to list
            name_data = df['Name'].tolist() # assign name data to list
            dob_data = df['DOB'].tolist() # assign dob data to list
            phone_data = df['Phone'].tolist() # assign phone data to list
            email_data = df['Email'].tolist() # assign email data to list
            location_data = df['Location'].tolist() # assign location data to list
            extra_data = df['Extra'].tolist() # assign extra data to list
            
            if  complete1 == False: # if complete1 is false
                logging.info('Pd read file successfully') # log file read success
                logging.info('Index, Name, DOB, Phone, Email, Location, Extra lists created successfully') # log lists created successfully
                complete1 = True # set complete1 to true
                return [str(x) for x in index_data], name_data, dob_data, phone_data, email_data, location_data, extra_data # return lists
            
            else: # if complete1 is true
                return [str(x) for x in index_data], name_data, dob_data, phone_data, email_data, location_data, extra_data # return lists
            
        except: # if error
            console.log("[bold red]Error:[/bold red] Data invalid at path: " + file_path, style="red") # print error message
            
            if  complete == False: # if complete is false
                logging.warning("FILE COULD NOT BE READ CORRECTLY", exc_info=True) # log error
                complete = True # set complete to true
                return 'error', 'error', 'error', 'error', 'error', 'error', 'error' # return error
            else: # if complete is true
                return 'error', 'error', 'error', 'error', 'error', 'error', 'error' # return error
    
    
    def finding_search_index(matching_name_index, name_data, dob_data, phone_data, email_data, location_data, extra_data, search_name, condition): # function to find search index
        
        console = Console() # create console object
         
        index = 0 # set index to 0
        index2 = 0 # set index2 to 0
        name_data2 = '' # assign name data to string
        name_data = name_data # assign name data to name_data2
        
        if condition == 'name': # if condition is name
            for i in name_data: # for each name in name_data
                try:
                    i.lower().index(search_name.lower()) # find index of search name in lowercase
                except ValueError: # if error
                    pass # do nothing
                else:
                    matching_name_index.append(index) # append index to matching_name_index
                index += 1 # increment index
                
            if len(matching_name_index) == 0: # if matching_name_index is empty
                console.print("[bold red]Error:[/bold red] Request not found", style="red") # print error message
                logging.error(f"Request not found used {condition}") # log error
                return 'none'
            
            return matching_name_index # return matching_name_index
        
        elif condition == 'dob':    # if condition is dob
            for i in dob_data: # for each dob in dob_data
                try: # try to find index of search name in dob
                    i.lower().index(search_name.lower()) # find index of search name in lowercase
                except ValueError: # if error
                    pass # do nothing
                else: # if no error
                    matching_name_index.append(index) # append index to matching_name_index
                index += 1 # increment index
                
            if len(matching_name_index) == 0: # if matching_name_index is empty
                console.print("[bold red]Error:[/bold red] Request not found", style="red") # print error message
                logging.warning(f"Request not found used {condition}") # log error
                return 'none' # return none
            
            return matching_name_index # return matching_name_index
            
        elif condition == 'phone': # if condition is phone
            for i in phone_data: # for each phone in phone_data
                try: # try to find index of search name in phone
                    i.lower().index(search_name.lower()) # find index of search name in lowercase
                except ValueError: # if error
                    pass # do nothing
                else:
                    matching_name_index.append(index) # append index to matching_name_index
                index += 1 # increment index
                
            if len(matching_name_index) == 0:   # if matching_name_index is empty
                console.print("[bold red]Error:[/bold red] Request not found", style="red") # print error message
                logging.warning(f"Request not found used {condition}") # log error
                return 'none' # return none
            
            return matching_name_index # return matching_name_index
            
        elif condition == 'email': # if condition is email
            for i in email_data: # for each email in email_data
                try: # try to find index of search name in email
                    i.lower().index(search_name.lower()) # find index of search name in lowercase
                except ValueError: # if error
                    pass # do nothing
                else: # if no error
                    matching_name_index.append(index) # append index to matching_name_index
                index += 1 # increment index
                
            if len(matching_name_index) == 0: # if matching_name_index is empty
                console.print("[bold red]Error:[/bold red] Request not found", style="red") # print error message
                logging.warning(f"Request not found used {condition}") # log error
                return 'none' # return none
            
            return matching_name_index # return matching_name_index
            
        elif condition == 'location': # if condition is location
            for i in location_data: # for each location in location_data
                try: # try to find index of search name in location
                    i.lower().index(search_name.lower()) # find index of search name in lowercase
                except ValueError: # if error
                    pass # do nothing
                else:               # if no error
                    matching_name_index.append(index) # append index to matching_name_index
                index += 1 # increment index
                
            if len(matching_name_index) == 0: # if matching_name_index is empty
                console.print("[bold red]Error:[/bold red] Request not found", style="red") # print error message
                logging.warning(f"Request not found used {condition}") # log error
                return 'none' # return none
            
            return matching_name_index   # return matching_name_index
            
        elif condition == 'extra': # if condition is extra
            for i in extra_data: # for each extra in extra_data
                try: # try to find index of search name in extra
                    i.lower().index(search_name.lower()) # find index of search name in lowercase
                except ValueError: # if error
                    pass # do nothing
                else:  # if no error
                    matching_name_index.append(index) # append index to matching_name_index
                index += 1 # increment index
                
            if len(matching_name_index) == 0: # if matching_name_index is empty
                console.print("[bold red]Error:[/bold red] Request not found", style="red") # print error message
                logging.warning(f"Request not found used {condition}") # log error
                return 'none' # return none
            
            return matching_name_index   # return matching_name_index
        
        
        
        
        
        else:
            return 'none'
        
        
        
#file_path = "classes\\test.csv"     

#search_index = 2
#print(datacollect.finding_search_index(index_data, name_data, dob_data, location_data, phone_data, email_data, extra_data, search_index))